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


def get_lm(dir_=None):

    if dir_ is None:
        p = Path('.')
    else:
        p = Path(dir_)

    parts = str(p.absolute()).split('/')

    l = None
    m = None

    for i, part in enumerate(parts):
        if part.startswith("Level"):
            l = part
        if part.startswith("Module"):
            m = part

    assert l.startswith("Level")
    assert m.startswith("Module")

    return l, m

def get_lmla(dir_=None):
    """Get level, module, lesson, assignment from a directory"""
    if dir_ is None:
        p = Path('.')
    else:
        p = Path(dir_)

    parts = str(p.absolute()).split('/')

    l = None
    m = None
    ls = None
    a = None


    # The lesson is the first directory after 'src',
    # and the assignment is the directory after the lesson.

    for i, part in enumerate(parts):
        if part.startswith("Level"):
            l = part
        if part.startswith("Module"):
            m = part
        if part == "src":
            # The lesson must be a directory
            t = Path('/'.join(parts[:i + 1]))
            if t.is_dir():
                ls = parts[i+1]
        if ls and parts[i] == ls:
            # The assignment must be a directory
            t = Path('/'.join(parts[:i+1]))
            if t.is_dir():
                a = parts[i+1]

    return l, m, ls, a

