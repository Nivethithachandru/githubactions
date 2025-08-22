def get_version():
    version = {}
    with open("core/__init__.py") as f:  # or maybe demo/__init__.py
        exec(f.read(), version)
    return version["__version__"]
