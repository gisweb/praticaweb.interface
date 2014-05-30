from populate import rndgenerate, namegenerate, da_du_ma, boolgenerate, \
    numbergenerate, dategenerate, rndselection

from .. import elencoTipologiePratica, elencoTipologieIntervento

class BaseType(dict):
    """ """

    template = {}

    def __init__(self, *args, **kw):
        dict.__init__(self, *[self._filterkeys(**a) for a in args], **self._filterkeys(**kw))
        if kw.get('populate') in (None, True, ):
            self.populate()
        assert all(k in self.template for k in self) or not self.template, "Error"

    def _filterkeys(self, **kw):
        """ """
        return dict([(k,v) for k,v in kw.items() if not self.template or k in self.keys()])

    def populate(self):
        """ """

    def __call__(self):
        return dict(self)

class Soggetto(BaseType):
    """ """

    template = {
        "albo": "xsd:string",
        "albonumero": "xsd:string",
        "alboprov": "xsd:string",
        "app": "xsd:string",
        "cap": "xsd:string",
        "capd": "xsd:string",
        "ccia": "xsd:string",
        "cciaprov": "xsd:string",
        "cedile": "xsd:string",
        "cedileprov": "xsd:string",
        "codfis": "xsd:string",
        "cognome": "xsd:string",
        "collaudatore": "xsd:int",
        "collaudatore_ca": "xsd:int",
        "comunato": "xsd:string",
        "comune": "xsd:string",
        "comuned": "xsd:string",
        "comunicazioni": "xsd:int",
        "concessionario": "xsd:int",
        "datanato": "xsd:date",
        "direttore": "xsd:boolean",
        "economia_diretta": "xsd:boolean",
        "email": "xsd:string",
        "esecutore": "xsd:boolean",
        "geologo": "xsd:boolean",
        "inail": "xsd:string",
        "inailprov": "xsd:string",
        "indirizzo": "xsd:string",
        "inps": "xsd:string",
        "inpsprov": "xsd:string",
        "nome": "xsd:string",
        "note": "xsd:string",
        "pec": "xsd:string",
        "piva": "xsd:string",
        "progettista": "xsd:boolean",
        "progettista_ca": "xsd:boolean",
        "proprietario": "xsd:boolean",
        "prov": "xsd:string",
        "provd": "xsd:string",
        "provnato": "xsd:string",
        "ragsoc": "xsd:string",
        "richiedente": "xsd:int",
        "sede": "xsd:string",
        "sesso": "xsd:string",
        "sicurezza": "xsd:boolean",
        "telefono": "xsd:string",
        "titolo": "xsd:string",
        "titolo_note": "xsd:string",
        "titolod": "xsd:string",
        "titolod_note": "xsd:string",
        "voltura": "xsd:boolean",
    }

    def populate(self):
        for k,v in filter(lambda c: c[0] not in self, self.template.items()):
            if 'cognome' in k:
                self[k] = namegenerate('LAST')
            elif 'nome' in k:
                self[k] = namegenerate()
            elif k == 'ragsoc' or k.startswith('inail'):
                self[k] = da_du_ma(5)
            elif k.startswith('ccia') or k.startswith('albo'):
                self[k] = str(numbergenerate(digits=6, negative=False))
            elif ('mail' in k or 'pec' in k):
                self[k] = '%s@example.com' % da_du_ma(4)
            elif 'sesso' in k:
                self[k] = 'M' if boolgenerate() else 'F'
            elif k in ('piva', 'codfis', ):
                # TODO
                self[k] = ""
            elif k in ('comune', 'comunato', 'comuned', ):
                # TODO
                self[k] = ""
            elif k.startswith('cap'):
                # TODO
                self[k] = str(numbergenerate(digits=4, negative=False))
            elif k.startswith('prov'):
                # TODO
                self[k] = ""
            elif k == 'telefono':
                prefix = numbergenerate(digits=4, negative=False)
                number = numbergenerate(digits=9, negative=False)
                self[k] = '%s/%s' % (prefix, number, )
            elif v.startswith('xsd:string'):
                parts = v.split(':')
                length = 20 if len(parts)<3 else int(parts[-1])
                self[k] = rndgenerate(length=length, prefix=False)
            elif v.startswith('xsd:boolean'):
                self[k] = boolgenerate()
            elif v.startswith('xsd:int'):
                self[k] = numbergenerate(digits=3, negative=False)
            elif v.startswith('xsd:date'):
                self[k] = dategenerate(s=-80*365, e=-20*365, format="%d/%m/%Y")

class Particella(BaseType):
    """ """

    template = {
        "sezione": "xsd:string",
        "foglio": "xsd:string",
        "mappale": "xsd:string",
        "sub": "xsd:string"
    }

    def populate(self):
        for k,v in filter(lambda c: c[0] not in self, self.template.items()):
            self[k] = str(numbergenerate(digits=3, negative=False))

class Indirizzo(BaseType):
    """ """

    template = {
        "via": "xsd:string",
        "civico": "xsd:string",
        "interno": "xsd:string"
    }

    def populate(self):
        for k,v in filter(lambda c: c[0] not in self, self.template.items()):
            if k == 'via':
                self[k] = rndgenerate(length=20, prefix=False)
            else:
                self[k] = str(numbergenerate(digits=2, negative=False))

class AggiungiPratica(BaseType):
    """ """

    template = {
        "tipo": "xsd:int",
        "intervento": "xsd:int",
        "oggetto": "xsd:string",
        "note": "xsd:string",
        "destinazione_uso": "xsd:string",
        "soggetti": "tns:soggetti",
        "particelle_terreni": "tns:particelleterreni",
        "particelle_urbano": "tns:particelleurbano",
        "indirizzi": "tns:indirizzi",
        #"validation": "xsd:string", # NO, gestito a parte in _get_validation
    }

    def populate(self):
        for k,v in filter(lambda c: c[0] not in self, self.template.items()):
            if k == 'tipo':
                tipi = map(lambda el: el[0], elencoTipologiePratica()['elenco'])
                self[k] = rndselection(vals=tipi, n=1)
            elif k == 'intervento':
                tipi = map(lambda el: el[0], elencoTipologieIntervento()['elenco'])
                self[k] = rndselection(vals=tipi, n=1)
            elif k == 'soggetti':
                self[k] = map(lambda x: dict(Soggetto()), range(rndselection(vals=range(1, 6))))
            elif k in ('particelle_terreni', 'particelle_urbano', ):
                self[k] = map(lambda x: dict(Particella()), range(rndselection(vals=range(1, 6))))
            elif k == 'indirizzi':
                self[k] = map(lambda x: dict(Indirizzo()), range(rndselection(vals=range(1, 6))))