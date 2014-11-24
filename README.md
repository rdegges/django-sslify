# django-sslify

Do you want to force HTTPs across your Django site? You're in the right place!

![django-sslify release](http://img.shields.io/pypi/v/django-sslify.svg)
![django-sslify downloads](http://img.shields.io/pypi/dm/django-sslify.svg)
![django-sslify build](http://img.shields.io/travis/rdegges/django-sslify.svg)

![guardian sketch](https://github.com/rdegges/django-sslify/raw/master/assets/guardian-sketch.png)


## Meta

- Author: Randall Degges
- Email: r@rdegges.com
- Site: http://www.rdegges.com
- Status: maintained, active


## Purpose

Enabling SSL on your Django site should be easy, easy as in *one-line-of-code
easy*.  That's why I wrote `django-sslify`!

The goal of this project is to make it easy for people to force HTTPS on every
page of their Django site, API, web app, or whatever you're building.  Securing
your site shouldn't be hard.


## Install

To install `django-sslify`, simply run `pip install django-sslify` and
you'll get the latest version installed automatically.

If you're using Heroku, you should add: `django-sslify>=0.2` to your
`requirements.txt` file in the root of your project directory.


## Usage

Modify your Django `settings.py` file, and prepend
`sslify.middleware.SSLifyMiddleware` to your `MIDDLEWARE_CLASSES` setting:

``` python
MIDDLEWARE_CLASSES = (
    'sslify.middleware.SSLifyMiddleware',
    # ...
)
```

**NOTE**: Make sure `sslify.middleware.SSLifyMiddleware` is the first
middleware class listed, as this will ensure that if a user makes an insecure
request (over HTTP), they will be redirected to HTTPs before any actual
processing happens.

If you're using Heroku, you should also add the following settings to your
Django settings file:

``` python
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
```

This ensures that Django will be able to detect a secure connection properly.


### Disabling SSLify

If you'd like to disable SSLify in certain environments (for local development,
or running unit tests), the best way to do it is to modify your settings file
and add the following:

``` python
SSLIFY_DISABLE = True
```

Note that SSLify is automatically disabled if DEBUG is True.


## Notes

This code was taken from
[this StackOverflow thread](http://stackoverflow.com/questions/8436666/how-to-make-python-on-heroku-https-only).

I've only tested this on Heroku, so if it doesn't work for you, please send a
pull request and I'll merge.

If you're using Heroku, and have no idea how to setup SSL, read
[this great article](https://devcenter.heroku.com/articles/ssl-endpoint) which
talks about using the new SSL endpoint addon (*which fucking rocks!*).


## Tests

[![Build Status](https://secure.travis-ci.org/rdegges/django-sslify.png?branch=master)](http://travis-ci.org/rdegges/django-sslify)

Want to run the tests? No problem:

``` bash
$ git clone git://github.com/rdegges/django-sslify.git
$ cd django-sslify
$ python setup.py develop
...
$ python manage.py test sslify

.
----------------------------------------------------------------------
Ran 1 tests in 0.000s

OK
Creating test database for alias 'default'...
Destroying test database for alias 'default'...
```
