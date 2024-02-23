
import os
import shutil
from pathlib import Path
from invoke import task
from textwrap import dedent
import re
import json 

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

def copy_dirs(ctx, root, to):
    """
    Task to restructure directories.
    """
    
    # Iterate through all items in the current directory
    for item in Path(root).glob('Level*-Module*'):
        if item.is_dir():
            print(item)
            copy_dir(item, Path(to ))


def jarlist(ctx, root):
    for dir_ in Path(root).glob("**/*"):
        if dir_.is_dir():
            jar_files = list(dir_.glob("*.jar"))
            if jar_files:
                print( dir_, jar_files)
                (Path(dir_) / 'lib').mkdir(exist_ok=True)

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


@task 
def walk(ctx, root):
    for dir_ in walk_modules(root):
        make_dirs(dir_)
        write_classpath(dir_)
        write_settings(dir_)
        write_gitignore(dir_)
        write_launch(dir_)


@task
def walk_mains(ctz, root):
    for m in walk_modules(root):
        print("\n----", m)
        
