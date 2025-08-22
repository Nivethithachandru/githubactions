from setuptools import setup, find_packages

def get_version():
    version = {}
    with open("core/__init__.py") as f:  # Use "demo/__init__.py" if using demo
        exec(f.read(), version)
    return version["__version__"]

setup(
    name="django-project",  # Replace with your actual project name
    version=get_version(),
    packages=find_packages(),
    include_package_data=True,
    install_requires=open("requirements.txt").read().splitlines(),
)
