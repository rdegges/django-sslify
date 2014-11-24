django-sslify
=============

Do you want to force HTTPs across your Django site? You're in the right place!

.. image:: http://img.shields.io/pypi/v/django-sslify.svg
    :alt: django-sslify Release
    :target: https://pypi.python.org/pypi/django-sslify

.. image:: http://img.shields.io/pypi/dm/django-sslify.svg
    :alt: django-sslify Downloads
    :target: https://pypi.python.org/pypi/django-sslify

.. image:: http://img.shields.io/travis/rdegges/django-sslify.svg
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


Disabling SSLify
----------------

If you'd like to disable SSLify in certain environments (*for local development,
or running unit tests*), the best way to do it is to modify your settings file
and add the following:

.. code-block:: python

    SSLIFY_DISABLE = True

.. note::
    `django-sslify` is automatically disabled if `settings.DEBUG` is `True`.


Notes
-----

This code was initially taken from
`this StackOverflow thread <http://stackoverflow.com/questions/8436666/how-to-make-python-on-heroku-https-only>`_.

This code has been adopted over the years to work on Heroku, and non-Heroku
platforms.

If you're using Heroku, and have no idea how to setup SSL, read
`this great article <https://devcenter.heroku.com/articles/ssl-endpoint>`_
which talks about using the new SSL endpoint addon (*which totally rocks!*).


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
