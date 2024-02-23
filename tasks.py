
import os
import shutil
from pathlib import Path
from invoke import task
from textwrap import dedent

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

@task(help={'root':"Directory with original source modules"})
def copy_dirs(ctx, root, to):
    """
    Task to restructure directories.
    """
    
    # Iterate through all items in the current directory
    for item in Path(root).glob('Level*-Module*'):
        if item.is_dir():
            print(item)
            copy_dir(item, Path(to ))

@task()
def jarlist(ctx, root):
    for dir_ in Path(root).glob("**/*"):
        if dir_.is_dir():
            jar_files = list(dir_.glob("*.jar"))
            if jar_files:
                print( dir_, jar_files)
                (Path(dir_) / 'lib').mkdir(exist_ok=True)
                
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
        jars_s += f'    <classpathentry kind="lib" path="libs/{jar}"/>\n    '

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


@task 
def walk(ctx, root):
    for dir_ in walk_modules(root):
        write_settings(dir_)

