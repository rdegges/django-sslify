# django-sslify

Do you want to force HTTPs across your Django site? You're in the right place!


## Install

To install ``django-sslify``, simply run ``pip install django-sslify`` and
you'll get the latest version installed automatically.


## Usage

Modify your Django ``settings.py`` file, and prepend
``sslify.middleware.SSLifyMiddleware`` to your ``MIDDLEWARE_CLASSES`` setting:

``` python
MIDDLEWARE_CLASSES = (
    'sslify.middleware.SSLifyMiddleware',
    # ...
)
```

**NOTE**: Make sure ``sslify.middleware.SSLifyMiddleware`` is the first
middleware class listed, as this will ensure that if a user makes an unsecure
request (over HTTP), they will be redirected to HTTPs before any actual
processing happens.
