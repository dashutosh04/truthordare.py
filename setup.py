from setuptools import setup, find_packages
import codecs

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

readme = ""
with open("README.md") as f:
    readme = f.read()

VERSION = "0.0.2"
DESCRIPTION = "A Python Package that enables you to fetch data from Truth or Dare API"
LONG_DESCRIPTION = readme

setup(
    name="truthordare.py",
    version=VERSION,
    author="d4rkpoison",
    author_email="ashutoshdas2004@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[requirements],
    keywords=["python", "truth", "dare", "truthordare"],
    classifiers=[
        "Development Status :: 1 - Planning",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
    ],
)
