"""
Teste - Programa Webscrape
"""
import os
import re
import requests
from bs4 import BeautifulSoup

DIRETORIO = r'C:\documento-teste'

# Cria o diretório caso ele não exista.
if not os.path.exists(DIRETORIO):
    os.mkdir(DIRETORIO)

#  Request para a página primária do teste.
PAGINA_PRINCIPAL = 'https://www.gov.br/ans/pt-br/assuntos/' \
                   'prestadores/padrao-para-troca-de-informacao-de-saude-suplementar-2013-tiss'
resposta_principal = requests.get(PAGINA_PRINCIPAL)

#  Recebe o escopo da página e encontra o link que leva à página secundária
ESCOPO_PAGINA_PRINCIPAL = str(resposta_principal.text)
TAG_LINK_PAGINA_SECUNDARIA = str(re.findall('href.+versão', ESCOPO_PAGINA_PRINCIPAL))
link_pagina_secundaria = (re.findall(r"https.+2021", TAG_LINK_PAGINA_SECUNDARIA))
link_pagina_secundaria = link_pagina_secundaria[0]

#  Request para a página secundária
resposta_secundaria = requests.get(link_pagina_secundaria)

#  Recebe o escopo da página e encontra o link do documento
soup = BeautifulSoup(resposta_secundaria.text, "html.parser")
for link in soup.select("a[href$='.pdf']"):
    documentos = link['href']
    if 'padrao' in documentos:
        link_documento = documentos

#  Cria o arquivo pdf dentro do diretório programado
localizacao = os.path.join(DIRETORIO, os.path.basename(link_documento))
resposta_pdf = requests.get(link_documento)
with open(localizacao, 'wb') as f:
    f.write(resposta_pdf.content)
