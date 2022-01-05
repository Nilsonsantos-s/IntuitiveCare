"""
Teste - Programa Extrador de Tabelas
"""
import os
import zipfile
from tabula import read_pdf

FILE = r"C:\documento-teste\padrao-tiss_componente-organizacional_202111.pdf"

# Leitura das tabelas
dfs1 = read_pdf(FILE, pages=114)
dfs2 = read_pdf(FILE, pages=(115, 116, 117, 118, 119))
dfs2_pag120 = read_pdf(FILE, pages=120, multiple_tables=True, area=0)
dfs3 = read_pdf(FILE, pages=120)
nome_tabela = ['quadro-31-pag115.csv', 'quadro-31-pag116.csv',
               'quadro-31-pag117.csv', 'quadro-31-pag118.csv', 'quadro-31-pag119.csv']


def operador_de_arquivo(writing=False, zipping=False, removing=False):
    """
    :param writing: Cria os arquivos csvs
    :param zipping: Realiza a compactação dos arquivos
    :param removing: Remove os arquivos csvs fora da compactação
    """

    if writing is True:
        contador = 0
        for pagina in dfs2:
            pagina.to_csv(nome_tabela[contador])
            contador += 1
        dfs1[0].to_csv("quadro-30.csv")
        dfs2_pag120[0].to_csv("quadro-31-pag120.csv")
        dfs3[0].to_csv("quadro-32.csv")

    if removing is True:
        os.remove('quadro-30.csv')
        for nome in nome_tabela:
            os.remove(nome)
        os.remove('quadro-31-pag120.csv')
        os.remove('quadro-32.csv')

    if zipping is True:
        arquivo_zip = zipfile.ZipFile('Teste_Nilson.zip', 'w', zipfile.ZIP_DEFLATED)
        arquivo_zip.write('quadro-30.csv')
        for nome in nome_tabela:
            arquivo_zip.write(nome)
        arquivo_zip.write('quadro-31-pag120.csv')
        arquivo_zip.write('quadro-32.csv')
        arquivo_zip.close()


operador_de_arquivo(writing=True)

operador_de_arquivo(zipping=True)

operador_de_arquivo(removing=True)
