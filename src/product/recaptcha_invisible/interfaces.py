# -*- coding: utf-8 -*-
from zope.publisher.interfaces.browser import IDefaultBrowserLayer
from zope.schema.interfaces import ITextLine


class IProductRecaptchaInvisibleLayer(IDefaultBrowserLayer):
    """ Marker interface that defines a browser layer.
    """


class IRecaptchaInvisibleField(ITextLine):
    """ Marker interface for Recaptcha Invisible Field
    """
