from invoke import task
from pathlib import Path

from tasklib.util import *
from tasklib.walk import *
from tasklib.html import *

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
        copy_devcontainer(repo_root, dir_)
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

def _proc_html(f):

    l, m, ls, a = get_lmla(f)

    print("Downloading ", f)
    web_dir = f.parent / '.web'
    web_dir.mkdir(exist_ok=True)

    urls = extract_urls(f.read_text())

    try:
        if not urls or len(urls) < 1:
            # Thre is no link in the recipe text, so it
            # is the text itself.
            download_webpage_assets(f.read_text(), web_dir)
        else:
            download_webpage_assets(urls[0], web_dir)

    except Exception as e:
        print("ERROR: Failed to download ", f)
        print(e)

    # f.rename(web_dir / f.name)


@task 
def fetch_web(ctx, root):
    """Walk the levels looking for html files and download the assets"""
    from researchrobot.openai_tools.completions import openai_one_completion
    root = Path(root)

    for f in root.glob("**/*.html"):
        if '/bin/' in str(f):
            continue

        if '/.web/' in str(f):
            continue

        _proc_html(f)

@task
def proc_web(cts, root):
    """Process the web pages in the .web directories"""
    root = Path(root)

    for f in root.glob("**/.web/"):
        idx = f / "index.html"
        if not idx.exists():
            continue

        print(idx)
        md = html_to_markdown(idx)
        idx.with_suffix('.md').write_text(md)


