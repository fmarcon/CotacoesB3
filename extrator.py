# -*- coding: utf-8 -*-

from glob import glob
import zipfile
from datetime import datetime
import pandas as pd

from layout_b3 import LayoutB3

PATH_ARQUIVOS_ZIP = '/home/fmarcon/Projetos/SeriesHistoricasB3/zip'
PATH_ARQUIVOS_TXT = '/home/fmarcon/Projetos/SeriesHistoricasB3/txt'
PATH_ARQUIVOS_CONSOLIDADOS = '/home/fmarcon/Projetos/SeriesHistoricasB3/consolidados'


def descompactar_arquivos_zip():
    """
    Descompacta os arquivos zip.
    """
    for path_to_zip_file in sorted(glob('%s/*.ZIP' % PATH_ARQUIVOS_ZIP)):
        print(path_to_zip_file)
        with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
            zip_ref.extractall(PATH_ARQUIVOS_TXT)


def gerar_arquivo_final():
    """
    """
    layout = LayoutB3()
    frames = []
    for path_to_txt in glob('%s/*.TXT' % PATH_ARQUIVOS_TXT):
        print(path_to_txt)
        df = pd.read_fwf(path_to_txt, colspecs=layout.get_posicoes())

        # Remove a última linha de cada arquivo
        df.drop(df.tail(1).index, inplace=True) 

        # Remove a primeira linha de cada arquivo
        df.drop(df.head(1).index, inplace=True)

        # Atribui as colunas do layout
        df.columns = layout.get_campos()

        # Filtra somente bolsa normal
        df = df[df['TPMERC']==10]

        # Remove campos não utilizados
        df = df.drop(layout.get_campos_remover(), axis=1)

        # Converte campo de data
        df['DATA'] = df['DATA'].apply(lambda a: datetime.strptime(str(a),'%Y%m%d'))

        frames.append(df)

    result = pd.concat(frames)
    result.to_csv('%s/final.csv' % PATH_ARQUIVOS_CONSOLIDADOS, header=True)
    

def mostrar_dados_finais():
    # dtype = {'DATA': int, 'CODNEG': str, 'PREABE': float, 'PREMAX': float, 'PREMIN': float, 'PREMED': float,
    #           'PREULT': float, 'PREOFC': float, 'PREOFV': float, 'TOTNEG': float, 'QUATOT': float, 'VOLTOT': float,
    #           'FATCOT': float
    # }
    df = pd.read_csv('%s/final.csv' % PATH_ARQUIVOS_CONSOLIDADOS)
    print(df.describe())
    print(df.columns)
    print(df.dtypes)


if __name__ == '__main__':
    #descompactar_arquivos_zip()
    gerar_arquivo_final()
    mostrar_dados_finais()

