from invoke import task
from pathlib import Path

from tasklib.util import *
from tasklib.walk import *

repo_root = Path(__file__).parent


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
        #copy_scripts(dir_)
        disable_eclipse(dir_)



#
# Push to the final module repos. 
#


@task
def push(ctx, root, build_dir=None):
    """Upload the module in the current dir to Github"""


    if build_dir is None:
        build_dir = repo_root / "_build"


    build_dir = Path(build_dir)

    for dir_ in walk_modules(root): 
        create_repo(ctx, dir_, build_dir)  
        #make_repo_template(dir_)


#
# Misc
#

@task
def hello(ctx):
    print(Path(__file__).parent)


@task 
def move_pde_assign(ctx, root):
    pde = list(Path(root).glob('**/*.pde'))
    for f in pde:
        new_path = Path(str(f).replace("Level0", "Level0PDE"))
        new_path.parent.mkdir(parents=True, exist_ok=True)
        f.rename(new_path)


@task 
def foo(ctx):
    from sresearchrobot.openai_tools.completions import openai_one_completion

