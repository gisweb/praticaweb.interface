## Script (Python) "procedimentoPratica"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=docid, cf='', format='json'
##title=
##

from praticaweb.interface import procedimentoPratica

data = procedimentoPratica(docid)

if format=='json':
    from gisweb.utils import json_dumps
    context.REQUEST.RESPONSE.setHeader("Content-type", "application/json")
    print json_dumps(data, customformat='ISO')
    return printed

elif format.endswith('.pt'):
    pt = getattr(context, format[:-3])
    if pt:
        context.REQUEST.RESPONSE.setHeader("Content-type", "text/html")
        print pt(**data).strip()
        return printed

return data
