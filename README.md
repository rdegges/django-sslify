# django-sslify

Do you want to force HTTPs across your Django site? You're in the right place!


![Use SSL for all the things!](https://github.com/rdegges/django-sslify/raw/master/ssl_all_the_things.jpg)


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


## Notes

This code was taken from [this StackOverflow
thread](http://stackoverflow.com/questions/8436666/how-to-make-python-on-heroku-https-only).

I've only tested this on Heroku, so if it doesn't work for you, please send a
pull request and I'll merge.

If you're using Heroku, and have no idea how to setup SSL, read [this great
article](https://devcenter.heroku.com/articles/ssl-endpoint) which talks about
using the new SSL endpoint addon (which fucking rocks!).


## TODO

- Write unit tests.
