from setuptools import setup, find_packages

with open("./README.md", "r", encoding="utf-8") as f:
    long_desc_md = f.read()   

setup (
    name="PyUtilities",
    version="0.0.1",
    author="Diman Gal Henege",
    author_email="dimanchansilu@gmail.com",
    description="A python utility package that provides commonly used functionalities or helper methods.",
    long_description=long_desc_md,
    long_description_content_type="text/markdown",
    url="https://github.com/oDqnger/PyUtilities",
    packages=find_packages(),
    requires=[],
    keywords=["python", "helper", "functions", "utility", "utilities", "algorithms", "data types"],
    license="MIT License",
)
