from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "./docs/README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()


with open("requirements.txt") as f:
    requirements = f.read().splitlines()


VERSION = "0.0.7"
DESCRIPTION = "A Python Package that enables you to fetch data from Truth or Dare API"
LONG_DESCRIPTION = "Please visit https://github.com/iamd4rk/truthordare.py#readme for docs"

setup(
    name="truthordare.py",
    url = "https://github.com/iamd4rk/truthordare.py#readme",
    version=VERSION,
    author="d4rkpoison",
    author_email="ashutoshdas2004@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
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
