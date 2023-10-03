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

Once you the public and private keys you need to setup them in ``/@@recaptcha-invisible-controlpanel`` controlpanel

This product is also compatible with collective.easyform, all you need to do is enable ``Recaptcha Invisible`` field in ``/@@easyform-controlpanel`` controlpanel

Usage
------------

Adding a field to an XML model::

    <field name="recaptcha" type="product.recaptcha_invisible.field.RecaptchaInvisibleField">
      <description/>
      <required>False</required>
      <title>recaptcha</title>
    </field>

Adding a field to a Python schema::

    from product.recaptcha_invisible.field import RecaptchaInvisibleField
    recaptcha = RecaptchaInvisibleField(
        title='Recaptcha',
        required=False,
    )

Known issues
------------

The Recaptcha appearence will show a floating right badge. This can cause problems when the recaptcha is displayed inside a Plone modal, in order to avoid this you can always customize the recaptcha with a small css::

    .grecaptcha-badge {
        position: static!important;
    }

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
- 1.x targets Plone 5.2
- 2.x targets Plone 6

