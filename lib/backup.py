import datetime as dt
import pathlib
import shutil

import numpy as np
import pandas as pd

from lib import config, erro


def bkup():
    # Cria diretório de backup e dados caso não exista
    pathlib.Path(config.ARQ['dadosBkupDir']).mkdir(parents=True, exist_ok=True)
    pathlib.Path(config.ARQ['dadosDir']).mkdir(parents=True, exist_ok=True)

    # Verifica se o arquivo de log existe
    if not pathlib.Path(config.ARQ['log']).exists():
        erro.tipo(1)

    # Verifica se o arquivo de dados não existe
    if not pathlib.Path(config.ARQ['dados']).exists():
        # Indicar qual erro
        erro.tipo(2)

        # Cria um dataframe
        (pd.DataFrame({'Temperatura': np.nan,
                       'Umidade': np.nan,
                       'Luminosidade': np.nan,
                       'Extra': np.nan
                       }, index=[dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')])).to_csv(config.ARQ['dados'],
                                                                                           index_label='Tempo')

    # Faz uma cópia do arquivo de dados e log para BACKUP
    shutil.copy2(config.ARQ['dados'], config.ARQ['dadosBkupDir'] + '/' +
                 dt.datetime.now().strftime('%Y-%m-%dT%H:%M:%S') + '-DAT' + '.csv')

    shutil.copy2(config.ARQ['log'], config.ARQ['dadosBkupDir'] + '/' +
                 dt.datetime.now().strftime('%Y-%m-%dT%H:%M:%S') + '-LOG' + '.csv')
