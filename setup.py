def get_version():
    version = {}
    with open("core/__init__.py") as f:
        exec(f.read(), version)
    return version["0.1.0"]
