.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on pypi or github. It is a comment.

===========================
product.recaptcha_invisible
===========================

Google Recaptcha Invisible support for Plone. Provides a field and a widget ready to be used in zope schemas

Features
--------

- Field
- Widget
- Validator

Translations
------------

This product has been translated into

- Catalan
- Spanish
- English


Installation
------------

Install product.recaptcha_invisible by adding it to your buildout::

    [buildout]

    ...

    eggs =
        product.recaptcha_invisible


and then running ``bin/buildout``

Configuration
------------

After installing the product in your Plone Site you need to register a new Google Recaptcha invisible in https://www.google.com/recaptcha/about/
Once you the public and private keys you need to setup them in `/@@recaptcha-invisible-controlpanel` controlpanel



Classifiers
-----------

Framework

- Plone 5.2
- Plone 6.0

Programming Language

- Python +3.7


License
-------

The project is licensed under the GPLv2.

Compatibility
-------
1.x targets Plone 5.2
2.x targets Plone 6

