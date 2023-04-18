from setuptools import setup, find_namespace_packages

setup(
    name='litepipe-build',
    version='0.1.0',
    description='Lite-pipe build tools',
    author='Robert Fletcher',
    install_requires=["PySide2", "qtawesome", "PyYAML"],
    find_packages=find_namespace_packages(where="src"),
    package_dir={"": "src"},
    entry_points={
        "console_scripts": [
            "litepipe-build = litepipe.build.__main__:main",

        ]
    }
)
