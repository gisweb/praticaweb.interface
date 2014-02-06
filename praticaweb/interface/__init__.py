# -*- extra stuff goes here -*-

from AccessControl import allow_module

def initialize(context):
    """Initializer called when used as a Zope 2 product."""

allow_module('gisweb.utils')

from praticaweb.interface import WSIol

def loadPortalSettings(self, tag='Praticaweb'):
    """
    In this way I can define some portal-dependent parameters in portalproperties
    (i.e. HOST or SPATH)
    """
    if not self:
        return dict()

    from Products.CMFCore.utils import getToolByName

    pp = getToolByName(self ,'portal_properties')

    if tag in pp.keys():
        return dict([(k,v) for k,v in pp[tag].propertyItems() if k!='title'])
    else:
        return dict()

def aggiungiPratica(self, numero, data, dump, replace=0):
    pwps = loadPortalSettings(self)
    conn = WSIol(**pwps)
    return conn.aggiungiPratica(numero, data, dump, replace)