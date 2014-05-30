
    >>> from praticaweb.interface import elencoTipologiePratica
    >>> tipoPratiche = elencoTipologiePratica()
    >>> tipoPratiche['success']
    1

    >>> from praticaweb.interface import elencoTipologieIntervento
    >>> out = elencoTipologieIntervento()
    >>> out['success']
    1

    >>> from praticaweb.interface import testAggiungiPratica
    >>> testAggiungiPratica()()
