import os
from distutils.core import setup
from django_grapesjs import __version__


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name = 'django_grapesjs',
    packages = ['django_grapesjs'],
    version = __version__,
    description = 'A small library for integrating the page builder "grapesjs" into django admin',
    author = 'Mark Burkut',
    author_email = 'burkut888mark@gmail.com',
    url = 'https://github.com/gulliverbms/django_grapesjs',
    long_description=read('README.rst'),
    keywords = ['page builder'],
    classifiers = [
        "Framework :: Django",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Environment :: Web Environment",
    ],
    license='MIT',
    install_requires=read('requirements.txt'),
)
