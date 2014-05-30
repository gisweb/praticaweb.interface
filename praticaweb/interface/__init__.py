# -*- extra stuff goes here -*-

def initialize(context):
    """Initializer called when used as a Zope 2 product."""

from AccessControl import allow_module
allow_module('praticaweb.interface')

import os, json
from DateTime import DateTime
from Globals import package_home
product_path = package_home(globals())

from praticaweb.interface import Praticaweb

#def loadPortalSettings(self, tag='Praticaweb'):
    #"""
    #In this way I can define some portal-dependent parameters in portalproperties
    #(i.e. HOST or SPATH)
    #"""
    #if not self:
        #return dict()

    #from Products.CMFCore.utils import getToolByName

    #pp = getToolByName(self ,'portal_properties')

    #if tag in pp.keys():
        #return dict([(k,v) for k,v in pp[tag].propertyItems() if k!='title'])
    #else:
        #return dict()

cfg = json.load(open(os.path.join(product_path, 'praticaweb.json')))

def elencoTipologiePratica():
    conn = Praticaweb(**cfg)
    out = conn.elencoTipologiePratica()
    return out

def elencoTipologieIntervento():
    conn = Praticaweb(**cfg)
    out = conn.elencoTipologieIntervento()
    return out

def testSoggetto():
    conn = Praticaweb(**cfg)
    return conn._tipopratica()
    from praticaweb.test import Soggetto
    return Soggetto()

from praticaweb.test import AggiungiPratica

def testAggiungiPratica():
    return AggiungiPratica()