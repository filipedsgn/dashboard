import datetime as dt
import pathlib

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

        # Cria diretório de dados caso não exista
        pathlib.Path(config.ARQ['dadosDir']).mkdir(parents=True, exist_ok=True)

        # Cria um dataframe
        (pd.DataFrame({'c0tem': np.nan,
                       'c0hum': np.nan,
                       'c0lum': np.nan,
                       'c0ext': np.nan
                       }, index=[dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')])).to_csv(config.ARQ['dados'])

    # Faz uma cópia do arquivo de dados e log para BACKUP
    pathlib.Path(config.ARQ['dados']).rename(config.ARQ['dadosBkupDir'] + '/DAT-' +
                                             dt.datetime.now().strftime('%Y-%m-%dT%H:%M:%S') + '.csv')

    pathlib.Path(config.ARQ['log']).rename(config.ARQ['dadosBkupDir'] + '/LOG-' +
                                           dt.datetime.now().strftime('%Y-%m-%dT%H:%M:%S') + '.csv')
