"""django-sslify package information."""


VERSION = (0, 2, 7)


def get_version():
    """returns a pep compliant version number"""
    return '.'.join(str(i) for i in VERSION)


__version__ = get_version()
