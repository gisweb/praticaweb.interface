# -*- extra stuff goes here -*-

def initialize(context):
    """Initializer called when used as a Zope 2 product."""

from AccessControl import allow_module
allow_module('praticaweb.interface')

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

#### TODO: se posso avere l'oggetto portale e ricavare i settaggi in portal_properties
# posso definire una volta per tutte un oggetto client da usare in tutte le funzioni
# i.e.:
# client = WSIol(**loadPortalSettings(PORTAL))

def aggiungiPratica(self, numero, data, dump, replace=0):
    """ Interroga il metodo aggiungiPratica del servizio """
    pwps = loadPortalSettings(self)
    conn = WSIol(**pwps)
    return conn.aggiungiPratica(numero, data, dump, replace)

def chiama(self, metodo, *args, **kw):
    """ Metodo generico per chiamare un metodo del servizio """
    pwps = loadPortalSettings(self)
    conn = WSIol(**pwps)
    return conn.call(metodo, *args, **kw)