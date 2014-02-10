# -*- coding: utf-8 -*-


urljoin = lambda *parts: '/'.join(parts)

from urlparse import urlunparse

import os.path

from datetime import datetime
from lxml import etree
from XmlDict import XmlDictConfig

from suds.client import Client

####                                                             #### UTILS ####



def deep_normalize(d):
    """ Normalize content of object returned from functions and methods """
    if 'sudsobject' in str(d.__class__):
        d = deep_normalize(dict(d))
    else:
        for k,v in d.iteritems():
            if 'sudsobject' in str(v.__class__):
                #print k, v, '%s' % v.__class__
                r = deep_normalize(dict(v))
                d[k] = r
            elif isinstance(v, dict):
                r = deep_normalize(v)
                d[k] = r
            elif isinstance(v, list):
                d[k] = [deep_normalize(i) for i in v]
            elif isinstance(v, datetime):
                # per problemi di permessi sugli oggetti datetime trasformo
                # in DateTime di Zope
                d[k] = DateTime(v.isoformat())
    return d


class SudsBase(object):
    """ Base class for interfacing to Suds web services """

    SCHEME = 'http'
    HOST = 'iol.praticaweb.it'
    PORT = ''
    SPATH = 'webservices'
    timeout = 180
    testinfo = False

    def __init__(self, service, **kw):
        for k,v in kw.items():
            setattr(self, k, v)
        self.url = urlunparse((
            self.SCHEME,
            ':'.join([loc for loc in (self.HOST, self.PORT, ) if loc]),
            os.path.join(self.SPATH, service),
            '',
            # trick for by-passing cache during development
            '' if not self.testinfo else 'x=1',
            '',
        ))

        self.client = Client(self.url, location=self.url, timeout=self.timeout)
        self.client.set_options(cache=None)

    def parse_response(self, res):
        """ Custom response parsing """
        return deep_normalize(dict(res))
        #if 'sudsobject' in str(res.__class__):
            #return deep_normalize(dict(res))
        #else:
            #if res:
                #encres = res.encode('utf-8')
                #parser = etree.XMLParser(ns_clean=True, recover=True, encoding='utf-8')
                #root = etree.fromstring(encres, parser=parser)
                #xmldict = XmlDictConfig(root)
                #return dict(xmldict)

    def compileTemplate(self, name, **kw):
        """ Generic XML helper """
        xml = self.client.factory.create(name)
        # a quanto pare iride ha qualche problema con i valori settati a None
        # come è di default per cui i valori non forniti li setto a '' (stringa vuota)
        for k,v in dict(xml).items():
            # considero gli oggetti semplici
            if v == None:
                xml[k] = kw.get(k) or ''
            # qui ho considerato che la struttura o contiene oggetti semplici (vedi sopra)
            # o contiene oggetti ArrayOf<something>-like.
            elif k in kw and kw[k]:
                # l'elemento k di kw a questo punto sarà una lista di dizionari
                for o in kw[k]:
                    xml[k][xml[k].__keylist__[0]].append(self.build_xml(str(v).split('\n')[0][8:-2], **o))
        return xml

    def compileTemplateAsDict(self, name, **kw):
        """
        Helper for getting a dictionary with keys loaded from the correspondent
        xml-like object
        """
        xml = self.client.factory.create(name)
        obj = dict()
        for k in dict(xml):
            obj[k] = kw.get(k) or ''
        return obj

    def call(self, methodname, *args, **kw):
        """ Standardize the output """
        service = getattr(self.client.service, methodname)
        out = dict(success=0, service=methodname)
        if self.testinfo: t0 = datetime.now()

        try:
            res = service(*args, **kw)
        except Exception as err:
            out['message'] = '%s' % err
            # for debug purposes in case of exception reasons are in input data
            out['request'] = deep_normalize(dict(request))
        else:
            if res:
                out['result'] = self.parse_response(res)
                if any([i in out['result'] for i in ('Errore', 'cod_err', )]):
                    out['request'] = deep_normalize(dict(request))
                else:
                    out['success'] = 1
            else:
                out['success'] = 1
            if self.testinfo:
                # for backward compatibility with python 2.6
                total_seconds = lambda x: x.seconds + x.microseconds*10**-6
                out['time_elapsed'] = total_seconds(datetime.now()-t0)

        return out


class WSIol(SudsBase):

    def __init__(self, **kw):
        SudsBase.__init__(self, 'ws-iol.php?wsdl', **kw)

    def aggiungiPratica(self, numero, data, dump, replace=0):
        """
        Parametri:
        numero: (stringa) numero della pratica generato in fase di salvataggio
        data:   (stringa) data di presentazione
        dump :  (stringa) stringa *json*/xml con il dump del document
        replace: flag (opzionale) se settato a 1 forza la sostituzione di una Pratica esistente
        """

        return self.call('aggiungiPratica', numero=numero, data=data, dump=dump)