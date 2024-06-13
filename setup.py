import setuptools

with open("README.md","r",encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "cnnClassifier"
AUTHOR_USER_NAME = "chilled_ice"
AUTHOR_EMAIL = "gurneet222@gmail.com"

setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A CNN Classifier",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/Gurneet1928/chicken-disease",
    project_urls={
        "Bug Tracker": f"https://github.com/Gurneet1928/chicken-disease/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
)