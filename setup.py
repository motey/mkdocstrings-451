from setuptools import setup
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="TestProj",
    description="this is a test project to reproduce error https://github.com/mkdocstrings/mkdocstrings/issues/451",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/motey/mkdocstrings-451",
    author="Tim Bleimehl",
    author_email="tim.bleimehl@helmholtz-muenchen.de",
    license="MIT",
    packages=["TestProj"],
    install_requires=[],
    extras_require={
        "docs": ["mkdocs", "mkdocstrings[python]"],
    },
    python_requires=">=3.9",
    zip_safe=False,
    include_package_data=True,
    use_scm_version={
        "root": ".",
        "relative_to": __file__,
        # "local_scheme": "node-and-timestamp"
        "local_scheme": "no-local-version",
        "write_to": "version.py",
    },
    setup_requires=["setuptools_scm"],
)
