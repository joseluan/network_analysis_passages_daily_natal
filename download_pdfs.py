import requests


#r = requests.get('https://natal.rn.gov.br/transparenciaapi/files/uploads/docs/2bb833eb07703e09eeb9dd52c8fd0f42.pdf')

links = {
    '2019': [
        'https://natal.rn.gov.br/transparenciaapi/files/uploads/docs/2bb833eb07703e09eeb9dd52c8fd0f42.pdf',
        'https://natal.rn.gov.br/transparenciaapi/files/uploads/docs/f3ae537d5ab746554c1f31aadb192bbd.pdf',
        'https://natal.rn.gov.br/transparenciaapi/files/uploads/docs/edbd5b8c642655d6dc742d02507b0f2d.pdf'
    ],
    '2020': [
        'https://natal.rn.gov.br/transparenciaapi/files/uploads/docs/b5fb4928b84b772a2c20d40151c3493e.pdf',
        'http://natal.rn.gov.br//transparenciaapi/files/uploads/docs/76bce0b69eaec551f2b6653efeadfce4.pdf',
        'http://natal.rn.gov.br//transparenciaapi/files/uploads/docs/f882f3db72e628f8023dae71361a3e03.pdf',
        'http://natal.rn.gov.br//transparenciaapi/files/uploads/docs/4d98288ab619ae6b9a44c8239808389d.pdf',
        'http://natal.rn.gov.br//transparenciaapi/files/uploads/docs/caf0c7e4eda8973976e77b4b0a43ef5b.pdf',
        'http://natal.rn.gov.br//transparenciaapi/files/uploads/docs/0f99e5a6024063ddb9ac1bc4d6555a3b.pdf',
        'http://natal.rn.gov.br//transparenciaapi/files/uploads/docs/05c713117738d8565ddcf312700248f2.pdf',
        'http://natal.rn.gov.br//transparenciaapi/files/uploads/docs/2d2e3da7fe60ed1d5b5229477242e1cb.pdf'
    ],
    '2021': [
        'http://natal.rn.gov.br//transparenciaapi/files/uploads/docs/2dd6453637dce1406d53123add2b155d.pdf',        
    ],

}

for ano in links:
    cont = 0
    for link in links[ano]:
        r = requests.get(link)
        arq = open(f'{ano}_{cont}.pdf', 'wb')
        arq.write(r.content)
        arq.close()
        cont += 1        