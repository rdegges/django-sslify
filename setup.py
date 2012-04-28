from os.path import abspath, dirname, join, normpath

from setuptools import find_packages, setup


setup(

    # Basic package information:
    name = 'django-sslify',
    version = '0.1',
    packages = find_packages(),

    # Packaging options:
    zip_safe = False,
    include_package_data = True,

    # Package dependencies:
    install_requires = ['Django>=1.0'],

    # Metadata for PyPI:
    author = 'Randall Degges',
    author_email = 'rdegges@gmail.com',
    license = 'UNLICENSE',
    url = 'https://github.com/rdegges/django-sslify',
    keywords = 'django ssl https middleware',
    description = 'Force SSL on your Django site.',
    long_description = open(normpath(join(dirname(abspath(__file__)),
        'README.md'))).read()

)
