
import os
import shutil
from pathlib import Path
from invoke import task
from textwrap import dedent
import re
import json 
from invoke import task
from pathlib import Path 
from contextlib import contextmanager
import requests


@contextmanager
def change_dir(destination):
    prev_dir = Path.cwd()
    os.chdir(destination)
    try:
        yield
    finally:
        os.chdir(prev_dir)


def copy_dir(from_, base):
    parts = from_.name.split('-')
    level = parts[0]
    module = parts[1]
    to = base / level / module

    shutil.copytree(from_, to )

def walk_modules(root):
    for dir_ in Path(root).glob("**/*"):
        if dir_.name.startswith("Module"):
            yield dir_


def walk_lessons(root):
    for m in walk_modules(root):
        src = m/'src'
        if src.exists():
            for a in src.iterdir():
                if a.is_dir():
                    yield a


def find_java_main_files(start_path):
    """
    Walks through the directory tree starting from start_path and yields the Path
    of each Java source file (.java) that contains a main() method.

    Args:
    - start_path (str or Path): The root directory from which to start searching.
    
    Yields:
    - Path objects pointing to Java files with a main() method.
    """
    start_path = Path(start_path)  # Ensure start_path is a Path object
    pattern = re.compile(r'public\s+static\s+void\s+main\s*\(\s*String\s*\[\s*\]\s+\w+\s*\)')  # Regex to match the main method

    # Walk through the directory tree
    for path in start_path.rglob('*.java'):  # rglob method for recursive globbing
        with open(path, 'r', encoding='utf-8') as file:
            if pattern.search(file.read()):  # Check if the file contains a main() method
                rp = str(path).split('/src/', 1)[-1]
                try:
                    package, clazz = rp.rsplit('/', 1)
                    clazz = clazz.replace('.java','')
                    package = package.replace('/','.')
                    fqn = '.'.join(package.split('.')+[clazz])
                    yield path, package, clazz, fqn
                except ValueError:
                    print("ERROR: Can't process class package", path)

def _move_jars_to_root(root):
    """Actually move the jar files into the lib dir"""
    root = Path(root)

    jars = list(Path(root).glob("**/*.jar"))

    if jars:

        (Path(root) / 'lib').mkdir(exist_ok=True)

        for jar in jars:
            jar.rename(root/"lib"/jar.name)

        (Path(root) / 'lib' / 'jars.txt').write_text('\n'.join([e.name for e in jars])+'\n')

def write_classpath(dir_):
    """Write the eclipse classpath file"""

    dir_ = Path(dir_)

    jf = (dir_/"lib"/"jars.txt")

    if not jf.exists():
        return

    # Do we need this?
    container = dedent(f"""
    <classpathentry kind="con" path="org.eclipse.jdt.launching.JRE_CONTAINER/org.eclipse.jdt.internal.debug.ui.launcher.StandardVMType/JavaSE-1.8">
        <attributes>
            <attribute name="module" value="true"/>
        </attributes>
    </classpathentry>
    """).strip()

    jars_s = ''

    for jar in jf.read_text().splitlines():
        jars_s += f'    <classpathentry kind="lib" path="lib/{jar}"/>\n    '

    cp = dedent(f"""
    <?xml version="1.0" encoding="UTF-8"?>
    <classpath>
        <classpathentry kind="src" path="src"/>
        <classpathentry kind="src" path="images"/>
        <classpathentry kind="output" path="bin"/>
    {jars_s}
    </classpath>
    """).strip()

    (dir_/'.classpath').write_text(cp)

def write_settings(dir_):
    """Write the VSCode settings file"""

    sf = (dir_/".vscode"/"settings.json")

    sf.parent.mkdir(exist_ok=True)

    sf_s = dedent(f"""
    {{
        "java.project.sourcePaths": [
            "images",
            "src"
        ],
        "java.project.outputPath": "bin",
        "java.project.referencedLibraries": [
            "lib/**/*.jar"
        ]
    }}
    """).strip()

    sf.write_text(sf_s+'\n')

def write_gitignore(dir_):
    gi_s = dedent(f"""
    *.class
    bin/*
    !bin/.keep
    .DS_Store
                  
    """).strip()

    (dir_/'.gitignore').write_text(gi_s+'\n')


def write_launch(dir_):
    """Write the VSCode launch.json file"""
    configs = []

    for path, package, clazz, fqn  in find_java_main_files(dir_):
            if clazz not in ('LeagueToken',):
                configs.append(
                    {
                        "type": "java",
                        "name": clazz,
                        "request": "launch",
                        "mainClass": fqn
                    }
                )

    configs = list(sorted(configs, key=lambda e: e['name']))

    lc = {
        "version": "0.2.0",
        "configurations": configs
    }

    (dir_/".vscode"/"launch.json").write_text(json.dumps(lc, indent=4))


def make_dirs(dir_):
    dirs = ['lib','src','images', 'bin']
    for d in dirs:
        p  = dir_/d
        if not p.exists():
            p.mkdir()
            (p/".keep").touch()


def copy_devcontainer(dir_):
    """Copy the devcontainer file from the root into the module"""
    source = Path('./.devcontainer')
    dest = dir_/".devcontainer"

    if not source.exists():
        raise FileNotFoundError(source)

    dest.mkdir(exist_ok=True)

    shutil.copytree(source, dest, dirs_exist_ok=True)

def copy_scripts(dir_):

    source = Path('./scripts')
    dest = dir_/"scripts"

    if not source.exists():
        raise FileNotFoundError(source)

    dest.mkdir(exist_ok=True)

    shutil.copytree(source, dest, dirs_exist_ok=True)

def get_lm(dir_=None):
    
    if dir_ is None:
        p = Path('.')
    else:
        p = Path(dir_)

    _, l, m  = str(p.absolute()).rsplit('/',2)

    assert l.startswith("Level")
    assert m.startswith("Module")

    return l, m


def disable_eclipse(dir_):

    if not (p := Path(dir_)/'.eclipse').exists():
        p.mkdir(parents=True)

    for f in ('.settings', '.classpath', '.project'):
        if ( p:=Path(dir_)/f).exists():
            p.rename(Path(dir_)/'.eclipse'/f)

def make_repo_template(dir_=None, owner="League-Java"):
    """
;/"{{""}}"
    Parameters:
    - owner: str. The username of the repository owner.
    - repo: str. The name of the repository.
   
    """

    l, m = get_lm(dir_)

    repo = f"{l}-{m}"

    github_token = os.environ['GITHUB_TOKEN']


    assert github_token is not None

    url = f"https://api.github.com/repos/{owner}/{repo}"
    headers = {
        "Authorization": f"token {github_token}",
        "Accept": "application/vnd.github.v3+json"
    }
    data = {"is_template": True}

    response = requests.patch(url, headers=headers, json=data)

    if response.status_code == 200:
        print(f"The repository '{repo}' has been successfully turned into a template.")
    else:
        print(f"Failed to turn the repository into a template. Status code: {response.status_code}, Response: {response.text}")



def create_repo(ctx, dir_):

    org = "League-Java"
    l, m = get_lm(dir_)
    repo = f"{l}-{m}"
    url = f'https://github.com/{org}/{repo}.git'

    with ctx.cd(dir_):
        if not (dir_/Path('.git')).exists():
            print(f"Create local repo {repo}")
            ctx.run("git init")
            ctx.run("git add -A")
            ctx.run("git commit -a -m'Initial commit'")
        else:
            print(f"Local repo {repo} exists, updating")
            ctx.run("git add -A", warn=True)
            ctx.run("git commit -a -m'Updating'", warn=True)

        print("Create remote repo")

        if ctx.run(f'gh repo view {url} --json url ',warn=True).failed:
            ctx.run(f'gh repo create {org}/{repo} --public -s . ')
        else:
            print(f"Repo {url} already exists")

        if  ctx.run('git remote -v | grep origin > /dev/null', warn=True).failed:
            print(f"Add remote origin {url}")
            ctx.run(f'git remote add origin {url}')


        print("Push")
        ctx.run("git push -f --set-upstream origin master")


@task 
def update_modules(ctx, root):
    """Update all of the module directories with settings files, scripts, etc. """

    for dir_ in walk_modules(root):
        make_dirs(dir_)
        write_classpath(dir_)
        write_settings(dir_)
        write_gitignore(dir_)
        write_launch(dir_)
        copy_devcontainer(dir_)
        copy_scripts(dir_)
        disable_eclipse(dir_)


@task
def push(ctx, root):
    """Upload the module in the current dir to Github"""

    for dir_ in walk_modules(root): 
        create_repo(ctx, dir_)  
        make_repo_template(dir_)


@task
def hello(ctx):
    c = ctx.run('git remote show origin', warn=True)
    print("!!!!", c.failed)


@task 
def move_pde_assign(ctx, root):
    pde = list(Path(root).glob('**/*.pde'))
    for f in pde:
        new_path = Path(str(f).replace("Level0", "Level0PDE"))
        new_path.parent.mkdir(parents=True, exist_ok=True)
        f.rename(new_path)
