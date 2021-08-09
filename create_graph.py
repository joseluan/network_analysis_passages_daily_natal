import re
from tika import parser  
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from unidecode import unidecode
#4814.8

ano = 2020
valor_geral = 0.0
qtd_pdfs = 8
G = nx.MultiDiGraph()
raw = ''
for i in range(0,qtd_pdfs):
    parsed_pdf = parser.from_file(f'{ano}_{i}.pdf')
    data = unidecode(parsed_pdf['content'])
    viagens_regex = re.finditer(
        r'(?P<nome>[^\d]+)(?P<data_inicio>[\d|\/|\.]{2,})[^\d]+(?P<data_fim>[\d|\/|\.]{2,})\s+(?P<valor>[\.|\d|\,]+)\s+(?P<destino>[^-]+\s+-\s+.+)',
        data
    )
    for viagem in viagens_regex:
        nome = viagem.group('nome').strip()
        data_inicio = viagem.group('data_inicio').strip()
        data_fim = viagem.group('data_fim').strip()
        valor = viagem.group('valor').strip()
        valor_geral += float(valor.replace('.', '').replace(',', '.'))
        destino = viagem.group('destino').split('-')
        destino_ida = destino[0].strip()
        destino_ida = re.sub(r'[^\w]', ' ', destino_ida)[0:4].strip()
        destino_volta = destino[1].strip()
        destino_volta = re.sub(r'[^\w]', ' ', destino_volta)
        if '.' in destino_volta[0:15]:
            destino_volta = destino_volta.strip().split('.')[0].strip()
        else:
            destino_volta = destino_volta.strip().split(' ')[0].strip()
        
        destino_volta = destino_volta[0:4]
        G.add_edge(destino_ida, destino_volta)
        #raw += f'{nome} {data_inicio} {data_fim} {valor} {destino_ida} {destino_volta}\n'


fig, ax = plt.subplots(1, 1,figsize=(10,8))
nx.draw_networkx(G, ax=ax,node_size=1000,pos=nx.circular_layout(G))
plt.axis("off")
#plt.show()
print(valor_geral)