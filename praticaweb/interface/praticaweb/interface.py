# -*- coding: utf-8 -*-

urljoin = lambda *parts: '/'.join(parts)

from urlparse import urlunparse

import os.path

from copy import copy
from datetime import datetime
#from lxml import etree
#from XmlDict import XmlDictConfig

from suds.client import Client

####                                                             #### UTILS ####


def deep_normalize(obj):
    """ Normalize content of object returned from functions and methods """
    if 'sudsobject' in str(obj.__class__):
        obj = deep_normalize(dict(obj))
    elif isinstance(obj, dict):
        for k,v in obj.iteritems():
            if 'sudsobject' in str(v.__class__):
                #print k, v, '%s' % v.__class__
                r = deep_normalize(dict(v))
                obj[k] = r
            elif isinstance(v, dict):
                r = deep_normalize(v)
                obj[k] = r
            elif isinstance(v, (list, tuple, )):
                obj[k] = [deep_normalize(i) for i in v]
            elif isinstance(v, datetime):
                # per problemi di permessi sugli oggetti datetime trasformo
                # in DateTime di Zope
                obj[k] = DateTime(v.isoformat())
    elif isinstance(obj, (list, tuple, )):
        obj = [deep_normalize(i) for i in obj]

    return obj


class SudsBase(object):
    """ Base class for interfacing to Suds web services """

    SCHEME = 'http'
    HOST = '' # something like: 'iol.praticaweb.it' or '192.168.1.20'
    PORT = ''
    SPATH = 'webservices'
    SERVICE = '' # something like: 'ws-iol.php?wsdl'
    timeout = 180
    testinfo = False
    fail = -1

    def __init__(self, **kw):
        for k,v in kw.items():
            setattr(self, k, v)
        trick = ''
        if self.testinfo:
            value = datetime.now().strftime('%S')
            trick = 'x=%s' % value
        self.url = urlunparse((
            self.SCHEME,
            ':'.join([loc for loc in (self.HOST, self.PORT, ) if loc]),
            os.path.join(self.SPATH, self.SERVICE),
            '',
            # trick for by-passing cache during development
            trick,
            '',
        ))
        self.setClient()

    def setClient(self):
        self.client = Client(self.url, location=self.url, timeout=self.timeout)
        self.client.set_options(cache=None)

    def _compileTemplate(self, xml, **kw):
        # a quanto pare iride ha qualche problema con i valori settati a None
        # come è di default per cui i valori non forniti li setto a '' (stringa vuota)
        for k,v in dict(xml).items():
            # considero gli oggetti semplici
            if v == None:
                xml[k] = kw.get(k) or ''
            # qui ho considerato che la struttura o contiene oggetti semplici (vedi sopra)
            # o contiene oggetti ArrayOf<something>-like.
            elif k in kw and kw[k]:
                default_stringed_value = str(v).split('\n')[0]
                if default_stringed_value.startswith('ArrayOf'):
                    # l'elemento k di kw a questo punto sarà una lista di dizionari
                    for obj in kw[k]:
                        xml[k][xml[k].__keylist__[0]].append(self.compileTemplate(default_stringed_value[8:-2], **obj))
                else:
                    raise NotImplementedError(default_stringed_value)
        return xml

    def compileTemplate(self, name, **kw):
        """ """
        xml = self.client.factory.create(name)
        return self._compileTemplate(xml, **kw)

    def templateCompiler(self, name, *objs):
        """ """
        tmp = self.client.factory.create(name)
        for obj in objs:
            xml = copy(tmp)
            yield self._compileTemplate(xml, **obj)

    def compileTemplateAsDict(self, name, **kw):
        """ Helper for getting a dictionary with keys loaded from the correspondent
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
        out = dict(success=self.fail)
        if self.testinfo: t0 = datetime.now()
        if self.testinfo: out['method'] = methodname

        try:
            res = service(*args, **kw)
        except Exception as err:
            out['message'] = '%s' % err
            # for debug purposes in case of exception reasons are in input data
            out['request'] = deep_normalize(dict(kw))
        else:
            out.update(deep_normalize(dict(res)))
            if self.testinfo:
                # for backward compatibility with python 2.6
                total_seconds = lambda x: x.seconds + x.microseconds*10**-6
                out['time_elapsed'] = total_seconds(datetime.now()-t0)

        return out


class Praticaweb(SudsBase):
    """ Main webservice """

    def __init__(self, **kw):
        SudsBase.__init__(self, **kw)

    def _get_validation(self):
        """ Helper for building validation string """
        # Any character at the moment is accepted
        return 'test'

    def call(self, methodname, *args, **kw):
        """ """
        if not 'validation' in kw:
            kw['validation'] = self._get_validation()
        return SudsBase.call(self, methodname, *args, **kw)

    def _soggetto(self, **kw):
        """ """
        return self.compileTemplate('soggetto', **kw)

    def _soggetti(self, *args):
        """
        args: dictionaries
        """
        soggetti = self.compileTemplate('soggetti')
        soggetto_compiler = self.templateCompiler('soggetto', *args)
        for arg in args:
            soggetti.append(soggetto_compiler.next())
        return soggetti

    def _particella(self, **kw):
        return self.compileTemplate('particella', **kw)

    def _particelle(self, xml, *objs):
        particella_compiler = self.templateCompiler('particella', *objs)
        for obj in objs:
            xml.append(particella_compiler.next())
        return xml

    def _particelleterreni(self, *objs):
        particelle = self.compileTemplate('particelleterreni')
        return self._particelle(xml, *objs)

    def _particelleurbano(self, *objs):
        particelle = self.compileTemplate('particelleurbano')
        return self._particelle(xml, *objs)

    def _indirizzo(self, **kw):
        return self.compileTemplate('indirizzo', **kw)

    def _indirizzo(self, *objs):
        indirizzi = self.compileTemplate('indirizzi')
        indirizzo_compiler = self.templateCompiler('indirizzo', *objs)
        for obj in objs:
            indirizzi.append(indirizzo_compiler.next())
        return indirizzi

    def elencoTipologiePratica(self):
        """ Metodo che elenca le tipologie di pratica """
        return self.call('elencoTipologiePratica')

    def elencoTipologieIntervento(self):
        """ Metodo che elenca le tipologie di intervento delle pratiche """
        return self.call('elencoTipologieIntervento')

    def aggiungiPratica(self, **kw):
        """ Metodo che aggiunge una istanza di pratica edilizia al software
        Praticaweb 2.0, restituisce la chiave primaria della pratica
        parts:
            tipo: tns:tipopratica
            intervento: tns:tipointervento
            oggetto: xsd:string
            note: xsd:string
            destinazione_uso: xsd:string
            soggetti: tsn:soggetti
            particelle_terreni: tns:particelleterreni
            particelle_urbano: tns:particelleurbano
            indirizzi: tns:indirizzi
            validation: xsd:string
        """
        pass