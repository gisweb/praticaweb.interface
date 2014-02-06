## Script (Python) "aggiungiPratica"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=replace=0
##title=webservices/ws-iol.php?wsdl#aggiungiPratica
##

from praticaweb.interface import aggiungiPratica

numero = context.getItem('numero_pratica')
data = context.getItem('data_pratica').strftime('%d-%m-%Y')
dump = context.serialDoc(format='xml')


return aggiungiPratica(numero, data, dump, replace=replace)