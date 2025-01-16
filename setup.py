from setuptools import setup

from passwords import __version__

setup(
    name="django-strong-passwords",
    version=__version__,
    author="Brandon Helwig",
    author_email="django-strong-passwords@brandonhelwig.com",
    description=(
        "A Django reusable app that provides validators and a form "
        "field that checks the strength of a password"
    ),
    long_description=open("README.rst").read(),
    url="https://github.com/brhelwig/django-strong-passwords/",
    license="BSD",
    packages=[
        "passwords",
    ],
    include_package_data=True,
    install_requires=[
        "Django >= 3.2",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Topic :: Utilities",
        "Framework :: Django",
    ],
)
