
    >>> from praticaweb.interface import aggiungiPratica
    >>> from random import random
    >>> data = '10-10-2013'
    >>> numero = int(random()*100000)
    >>> dump = """<?xml version="1.0" encoding="utf-8" ?>
    ... <info>
    ... <Form>frm_permesso_costruire</Form>
    ... <Plomino_Authors>admin</Plomino_Authors>
    ... <anagrafiche></anagrafiche>
    ... <autorizzata_al></autorizzata_al>
    ... <autorizzata_dal></autorizzata_dal>
    ... <data_autorizzazione></data_autorizzazione>
    ... <data_ordinanza></data_ordinanza>
    ... <data_permesso></data_permesso>
    ... <data_pratica>06-02-2014</data_pratica>
    ... <data_protocollo></data_protocollo>
    ... <data_protocollo_autorizzazione></data_protocollo_autorizzazione>
    ... <dichiarazioni_derivazione></dichiarazioni_derivazione>
    ... <documenti></documenti>
    ... <documenti_appendice></documenti_appendice>
    ... <documenti_autorizzazione></documenti_autorizzazione>
    ... <documenti_ordinanza></documenti_ordinanza>
    ... <documenti_pdf></documenti_pdf>
    ... <domicilio_opt></domicilio_opt>
    ... <elenco_altri_intestatari></elenco_altri_intestatari>
    ... <elenco_altri_richiedenti></elenco_altri_richiedenti>
    ... <elenco_civici>
    ... ... <civico_civico>13</civico_civico>
    ... ... <civico_geometry>POINT(7.77113861374921 43.8149272641531)</civico_geometry>
    ... ... <civico_nomevia>CORSO INGLESI</civico_nomevia>
    ... ... <civico_via>299</civico_via>
    ... </elenco_civici>
    ... <elenco_civici>
    ... ... <civico_civico>63</civico_civico>
    ... ... <civico_geometry>POINT(7.78120569729499 43.8181852260154)</civico_geometry>
    ... ... <civico_nomevia>LUNGOMARE TRENTO E TRIESTE</civico_nomevia>
    ... ... <civico_via>504</civico_via>
    ... </elenco_civici>
    ... <elenco_nceu>
    ... ... <nceu_foglio>1</nceu_foglio>
    ... ... <nceu_mappale>1</nceu_mappale>
    ... ... <nceu_sezione>B</nceu_sezione>
    ... ... <nceu_subalterno>1</nceu_subalterno>
    ... </elenco_nceu>
    ... <elenco_nceu>
    ... ... <nceu_foglio>23</nceu_foglio>
    ... ... <nceu_mappale>2</nceu_mappale>
    ... ... <nceu_sezione>A</nceu_sezione>
    ... ... <nceu_subalterno>1</nceu_subalterno>
    ... </elenco_nceu>
    ... <elenco_nct>
    ... ... <nct_foglio>4</nct_foglio>
    ... ... <nct_geometry>POLYGON((7.74864170771224 43.8672671449268,7.74872308218067 43.8672892573442,7.74909898377951 43.8670359541365,7.74894007702183 43.8670919798134,7.74884513358297 43.8671375398054,7.74871369295096 43.8671904749437,7.74861752276268 43.8672592817702,7.74864170771224 43.8672671449268))</nct_geometry>
    ... ... <nct_mappale>3</nct_mappale>
    ... ... <nct_sezione>A</nct_sezione>
    ... </elenco_nct>
    ... <elenco_nct>
    ... ... <nct_foglio>6</nct_foglio>
    ... ... <nct_geometry>POLYGON((7.77710887808802 43.8569946700458,7.7772819501547 43.8570483005458,7.77731097980028 43.8569769831365,7.77735539018048 43.8568634412106,7.77736031911977 43.8568508124419,7.77717102799335 43.8568317748765,7.77716983056935 43.8568803751539,7.77714450399199 43.8569113353093,7.77710887808802 43.8569946700458))</nct_geometry>
    ... ... <nct_mappale>23</nct_mappale>
    ... ... <nct_sezione>A</nct_sezione>
    ... </elenco_nct>
    ... <firstDocument>4b06af46c3ac4178950c4dff5cfc3413</firstDocument>
    ... <fisica_app>Dott.</fisica_app>
    ... <fisica_cap>34073</fisica_cap>
    ... <fisica_cellulare></fisica_cellulare>
    ... <fisica_cf>RSSMRA73T15E125V</fisica_cf>
    ... <fisica_cittadinanza></fisica_cittadinanza>
    ... <fisica_civico>5</fisica_civico>
    ... <fisica_cod_cat_nato>E125</fisica_cod_cat_nato>
    ... <fisica_cognome>ROSSI</fisica_cognome>
    ... <fisica_comune>Grado</fisica_comune>
    ... <fisica_comune_nato>Grado</fisica_comune_nato>
    ... <fisica_data_nato>15/12/1973</fisica_data_nato>
    ... <fisica_domicilio_cap></fisica_domicilio_cap>
    ... <fisica_domicilio_civico></fisica_domicilio_civico>
    ... <fisica_domicilio_comune></fisica_domicilio_comune>
    ... <fisica_domicilio_indirizzo></fisica_domicilio_indirizzo>
    ... <fisica_domicilio_provincia></fisica_domicilio_provincia>
    ... <fisica_email></fisica_email>
    ... <fisica_fax></fisica_fax>
    ... <fisica_indirizzo>Via Buona</fisica_indirizzo>
    ... <fisica_loc></fisica_loc>
    ... <fisica_loc_nato></fisica_loc_nato>
    ... <fisica_nome>MARIO</fisica_nome>
    ... <fisica_pec></fisica_pec>
    ... <fisica_provincia>GO</fisica_provincia>
    ... <fisica_provincia_nato>GO</fisica_provincia_nato>
    ... <fisica_search></fisica_search>
    ... <fisica_sesso>Maschile</fisica_sesso>
    ... <fisica_telefono></fisica_telefono>
    ... <fisica_titolo>Proprietario</fisica_titolo>
    ... <giuridica_cap></giuridica_cap>
    ... <giuridica_cciaa></giuridica_cciaa>
    ... <giuridica_cciaa_numero></giuridica_cciaa_numero>
    ... <giuridica_cellulare></giuridica_cellulare>
    ... <giuridica_cf></giuridica_cf>
    ... <giuridica_civico></giuridica_civico>
    ... <giuridica_comune></giuridica_comune>
    ... <giuridica_denominazione></giuridica_denominazione>
    ... <giuridica_email></giuridica_email>
    ... <giuridica_fax></giuridica_fax>
    ... <giuridica_indirizzo></giuridica_indirizzo>
    ... <giuridica_localita></giuridica_localita>
    ... <giuridica_opt></giuridica_opt>
    ... <giuridica_pec></giuridica_pec>
    ... <giuridica_piva></giuridica_piva>
    ... <giuridica_provincia></giuridica_provincia>
    ... <giuridica_qualita></giuridica_qualita>
    ... <giuridica_search></giuridica_search>
    ... <giuridica_telefono></giuridica_telefono>
    ... <integrazione_autorizzazione></integrazione_autorizzazione>
    ... <iol_tipo_app>permesso</iol_tipo_app>
    ... <iol_tipo_pratica>permesso_costruire</iol_tipo_pratica>
    ... <iol_tipo_richiesta>costruire</iol_tipo_richiesta>
    ... <istruttore></istruttore>
    ... <istruttoria_annotazioni></istruttoria_annotazioni>
    ... <istruttoria_annotazioni_richiedente></istruttoria_annotazioni_richiedente>
    ... <istruttoria_annotazioni_sospensione_richiedente></istruttoria_annotazioni_sospensione_richiedente>
    ... <istruttoria_motivo_sospensione></istruttoria_motivo_sospensione>
    ... <istruttoria_prescrizioni></istruttoria_prescrizioni>
    ... <istruttoria_rigetto_annotazioni></istruttoria_rigetto_annotazioni>
    ... <istruttoria_rigetto_annotazioni_richiedente></istruttoria_rigetto_annotazioni_richiedente>
    ... <istruttoria_rigetto_controdeduzioni></istruttoria_rigetto_controdeduzioni>
    ... <istruttoria_rigetto_motivazione></istruttoria_rigetto_motivazione>
    ... <iter></iter>
    ... <label_autorizzazione></label_autorizzazione>
    ... <label_pratica>12</label_pratica>
    ... <layers></layers>
    ... <linkToParent></linkToParent>
    ... <modello_appendice></modello_appendice>
    ... <modello_autorizzazione></modello_autorizzazione>
    ... <modello_ordinanza></modello_ordinanza>
    ... <modifiche_concessione_originale></modifiche_concessione_originale>
    ... <numero_autorizzazione></numero_autorizzazione>
    ... <numero_ordinanza></numero_ordinanza>
    ... <numero_permesso></numero_permesso>
    ... <numero_pratica>12</numero_pratica>
    ... <numero_proroghe></numero_proroghe>
    ... <numero_protocollo></numero_protocollo>
    ... <numero_protocollo_autorizzazione></numero_protocollo_autorizzazione>
    ... <numero_rinnovi></numero_rinnovi>
    ... <numero_ripristini></numero_ripristini>
    ... <owner>admin</owner>
    ... <progressivo_autorizzazione></progressivo_autorizzazione>
    ... <progressivo_pratica></progressivo_pratica>
    ... <prorogabile>1</prorogabile>
    ... <rigetto_data_protocollo></rigetto_data_protocollo>
    ... <rigetto_data_protocollo_ap></rigetto_data_protocollo_ap>
    ... <rigetto_numero_protocollo></rigetto_numero_protocollo>
    ... <rigetto_numero_protocollo_ap></rigetto_numero_protocollo_ap>
    ... <scripts></scripts>
    ... <search_richiedente> ROSSI MARIO </search_richiedente>
    ... <tipologia_intervento>1</tipologia_intervento>
    ... <tipologia_richiesta>20000</tipologia_richiesta>
    ... <ubicazioni_mappa></ubicazioni_mappa>
    ... <wf_iol></wf_iol>
    ... </info>"""
    >>> result = aggiungiPratica(None, numero, data, dump, replace=1)
    >>> result['success']
    1

