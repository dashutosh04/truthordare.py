from setuptools import setup, find_packages
import codecs


VERSION = "0.0.1"
DESCRIPTION = "A Python Package that enables you to fetch data from Truth or Dare API"
LONG_DESCRIPTION = "This package allows you to get data from the truth or dare api with various parameters"

setup(
    name="truthordare.py",
    version=VERSION,
    author="d4rkpoison",
    author_email="ashutoshdas2004@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=["requests>=2.28.1"],
    keywords=["python", "truth", "dare", "truthordare"],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
)
