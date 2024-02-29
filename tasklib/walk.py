from pathlib import Path


def walk_modules(root):

    root = Path(root)

    if root.name.startswith("Module"):
            yield root

    for dir_ in root.glob("**/*"):
        if dir_.name.startswith("Module"):
            yield dir_


def walk_lessons(root):
    for m in walk_modules(root):
        src = m/'src'
        if src.exists():
            for a in src.iterdir():
                if a.is_dir():
                    yield a
