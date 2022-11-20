from setuptools import setup, find_packages

VERSION = '1.0.0'
DESCRIPTION = 'Python library for searching books on Libgen.rs'

setup(
    name="libgen-search",
    version=VERSION,
    author="Anhy Krishna Fitiavana",
    author_email="fitiavana.krishna@gmail.com",
    license="MIT License",
    description=DESCRIPTION,
    long_description=open("README.md", "r").read(),
    packages=find_packages(),
    install_requires=["requests", "bs4", "lxml"],
    keywords=["python", "libgen.rs", "scraping", "books"],
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ]
)
