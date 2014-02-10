# -*- extra stuff goes here -*-

def initialize(context):
    """Initializer called when used as a Zope 2 product."""

from AccessControl import allow_module
allow_module('praticaweb.interface')

from configobj import ConfigObj
import os
from DateTime import DateTime
from Globals import package_home
product_path = package_home(globals())

from praticaweb.interface import WSIol

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

conf = ConfigObj(os.path.join(product_path, 'praticaweb.cfg'), create_empty=True)
try:
    conn = WSIol(**conf)
except:
    conn = None

def aggiungiPratica(numero, data, dump, replace=0):
    """ Interroga il metodo aggiungiPratica del servizio """
    return conn.aggiungiPratica(numero, data, dump, replace)

def chiama(metodo, *args, **kw):
    """ Metodo generico per chiamare un metodo del servizio """
    return conn.call(metodo, *args, **kw)

def procedimentoPratica(docid):
    """
    Shortcut per ricavare le informazioni del procedimento direttamente a partire
    da una pratica.
    """

    # 1. si ricava la lista dei procedimenti in capo al mittente attraverso il CF
    try:
        res_procedimenti = chiama('procedimentoPratica', docid=docid)
    except Exception as err:
        errmsg = str(err)
        errtype = type(err)
        res_procedimenti = dict(success=0, message='%s: %s' % (errtype, errmsg))
        res_procedimenti['result'] = dict(
            IdIter = 0,
            Descrizione = 'DEMO',
            Responsabile = 'Nome Responsabile',
            DataInizio = DateTime()-15,
            DataFine = DateTime()+15,
            StatoProcedimento = 'STATO'
        )

    if res_procedimenti['success']:
        if not res_procedimenti['result'].get('Errore'):
            # 2. si filtra i procedimenti trovati in base al parametro IdDocumento
            flt_res = [rec['TestataProcedimento'] \
                for rec in res_procedimenti['result']['Procedimenti']['Procedimento'] \
                    if rec['EstremiDocumento']['IdDocumento']==docid] or [{}]
            res_procedimenti['result'] = flt_res[0]
            return res_procedimenti
        else:
            return res_procedimenti
    else:
        return res_procedimenti