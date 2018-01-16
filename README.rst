django-sslify
=============

Do you want to force HTTPs across your Django site? You're in the right place!

.. image:: https://img.shields.io/pypi/v/django-sslify.svg
    :alt: django-sslify Release
    :target: https://pypi.python.org/pypi/django-sslify

.. image:: https://img.shields.io/pypi/dm/django-sslify.svg
    :alt: django-sslify Downloads
    :target: https://pypi.python.org/pypi/django-sslify

.. image:: https://img.shields.io/travis/rdegges/django-sslify.svg
    :alt: django-sslify Build
    :target: https://travis-ci.org/rdegges/django-sslify

.. image:: https://github.com/rdegges/django-sslify/raw/master/assets/guardian-sketch.png
   :alt: Guardian Sketch


Meta
----

- Author: Randall Degges
- Email: r@rdegges.com
- Site: http://www.rdegges.com
- Status: maintained, active


Purpose
-------

Enabling SSL on your Django site should be easy, easy as in *one-line-of-code
easy*.  That's why I wrote ``django-sslify``!

The goal of this project is to make it easy for people to force HTTPS on every
page of their Django site, API, web app, or whatever you're building.  Securing
your site shouldn't be hard.

Using Django 1.8 or later?
--------------------------

This package was written before Django 1.8. If you are using Django 1.8 or later, you do not need this library in order to force HTTPS. Instead, you can just change your ``settings.py`` file to include ``SECURE_SSL_REDIRECT``.

.. code-block:: python

    # in settings.py
    SECURE_SSL_REDIRECT = True

If you are using Heroku, you may need to add ``SECURE_PROXY_SSL_HEADER`` as well.

.. code-block:: python

    # in settings.py
    SECURE_SSL_REDIRECT = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

Django's documentation includes more details about `security settings for HTTPS <https://docs.djangoproject.com/en/dev/topics/security/#ssl-https>`_.

If you are using an older version of Django (1.7 or earlier), then this package is for you.

Installation
------------

To install ``django-sslify``, simply run:

.. code-block:: console

    $ pip install django-sslify

This will install the latest version of the library automatically.

If you're using `Heroku <https://www.heroku.com/>`_, you should add
``django-sslify>=0.2`` to your ``requirements.txt`` file:

.. code-block:: console

    $ echo 'django-sslify>=0.2.0' >> requirements.txt

Once you've done this, the next time you push your code to Heroku this library
will be installed for you automatically.


Usage
-----

To use this library, and force SSL across your Django site, all you need to do
is modify your ``settings.py`` file, and prepend
``sslify.middleware.SSLifyMiddleware`` to your ``MIDDLEWARE_CLASSES`` setting:

.. code-block:: python

    # settings.py

    MIDDLEWARE_CLASSES = (
        'sslify.middleware.SSLifyMiddleware',
        # ...
    )

.. note::
    Make sure ``sslify.middleware.SSLifyMiddleware`` is the first middleware
    class listed, as this will ensure that if a user makes an insecure request
    (*over HTTP*), they will be redirected to HTTPs before any actual
    processing happens.

If you're using Heroku, you should also add the following settings to your
Django settings file:

.. code-block:: python

    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

This ensures that Django will be able to detect a secure connection properly.


Using a Custom SSL Port
***********************

If your site is running on a non-standard SSL port, you can change
``django-sslify``'s default redirection behavior by setting a special variable
in your ``settings.py`` file:

.. code-block:: python

    SSLIFY_PORT = 999


Disabling SSLify
----------------

If you'd like to disable SSLify in certain environments (*for local development,
or running unit tests*), the best way to do it is to modify your settings file
and add the following:

.. code-block:: python

    SSLIFY_DISABLE = True

You can also disable SSLify for certain requests only (*useful for exposing
HTTP-only web hook URLs, etc*) by adding a callable with a single request
parameter to the ``SSLIFY_DISABLE_FOR_REQUEST`` list.  Returning ``True`` from
your callable will disable SSL redirects.

.. code-block:: python

    SSLIFY_DISABLE_FOR_REQUEST = [
        lambda request: request.get_full_path().startswith('/no_ssl_please')
    ]


Notes
-----

This code was initially taken from
`this StackOverflow thread <http://stackoverflow.com/questions/8436666/how-to-make-python-on-heroku-https-only>`_.

This code has been adopted over the years to work on Heroku, and non-Heroku
platforms.

If you're using Heroku, and have no idea how to setup SSL, read
`this great article <https://devcenter.heroku.com/articles/ssl-endpoint>`_
which talks about using the new SSL endpoint addon (*which totally rocks!*).


NGINX + Infinite Redirect
-------------------------

If you're running your Django app behind an Nginx load balancer, and are seeing
infinite redirects, the solution is to add the following line:

.. code-block:: text

    proxy_set_header X-Forwarded-Proto $scheme;

To your ``nginx.conf`` file, inside of the relevant ``location`` blocks.  This
`Stack Overflow thread
<http://stackoverflow.com/questions/23121800/nginx-redirect-loop-with-ssl>`_
might also be useful.


Contributing
------------

This project is only possible due to the amazing contributors who work on it!

If you'd like to improve this library, please send me a pull request! I'm happy
to review and merge pull requests.

The standard contribution workflow should look something like this:

- Fork this project on Github.
- Make some changes in the master branch (*this project is simple, so no need to
  complicate things*).
- Send a pull request when ready.

Also, if you're making changes, please write tests for your changes -- this
project has a full test suite you can easily modify / test.

To run the test suite, you can use the following commands:

.. code-block:: console

    $ cd django-sslify
    $ python setup.py develop
    $ python manage.py test sslify


Change Log
----------

All library changes, in descending order.


Version 0.2.8
*************

**Released January 15, 2018.**

- Adding Django 1.10 compatibility.
- Fixing markup.
- Updating Travis CI for 1.9.

Version 0.2.5
*************

**Released December 28, 2014.**

- Adding in new ``SSLIFY_DISABLE_FOR_REQUEST`` setting which allows a user to
  specify functions that can choose to reject SSL -- this is useful for
  situations where you might want to force SSL site-wide EXCEPT in a few
  circumstances (*webhooks that don't support SSL, for instance*).


Version 0.2.4
*************

**Released on November 23, 2014.**

- Adding the ability to specify a custom SSL port.
- Totally revamping docs.
- Changing project logo / mascot thingy ^^
- Adding new tests for custom SSL ports.
