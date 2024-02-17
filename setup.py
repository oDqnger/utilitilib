from setuptools import setup, find_packages

with open("/README.md", "r", encoding="utf-8") as f:
    long_desc_md = f.read()   

setup (
    name="PyUtilities",
    version=1.0,
    author="Diman Gal Henege",
    author_email="dimanchansilu@gmail.com",
    description="A python utility package that provides commonly used functionalities or helper methods.",
    long_description=long_desc_md,
    long_description_content_type="text/markdown",
    url="https://github.com/oDqnger/PyUtilities",
    packages=find_packages(),
    license="MIT License",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"
    ],
)