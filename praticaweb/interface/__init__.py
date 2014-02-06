# -*- extra stuff goes here -*-

from AccessControl import allow_module

def initialize(context):
    """Initializer called when used as a Zope 2 product."""

allow_module('gisweb.utils')

from praticaweb.interface import WSIol

conn = WSIol()

def aggiungiPratica(numero, data, dump, replace=0):
    return conn.aggiungiPratica(numero, data, dump, replace)