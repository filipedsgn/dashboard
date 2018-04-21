import datetime as dt
import pathlib

import numpy as np
import pandas as pd

from lib import config, erro


# TODO: deletar erro do diretório de BACKUP do arquivo erro.py

def bkup():
    # Cria diretório de backup de dados caso não exista
    pathlib.Path(config.CSV['dadosBkupDir']).mkdir(parents=True, exist_ok=True)

    # Cria diretório de backup de fotos caso não exista
    pathlib.Path(config.CSV['fotosBkupDir']).mkdir(parents=True, exist_ok=True)

    # Verifica se o arquivo de log existe
    if not pathlib.Path(config.CSV['log']).exists():
        erro.tipo(1)

    if pathlib.Path(config.CSV['dados']).exists():
        # Faz uma cópia do arquivo de dados para BACKUP
        pathlib.Path(config.CSV['dados']).rename(config.CSV['dadosBkupDir' + '/DAT-' +
                                                            dt.datetime.now().strftime('%Y-%m-%dT%H:%M:%S') + '.csv'])
        # TODO: adicionar o tipo de erro

    else:
        # Indicar qual erro
        erro.tipo(2)

        # Cria diretório de dados caso não exista
        pathlib.Path(config.CSV['dadosDir']).mkdir(parents=True, exist_ok=True)

        agora = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Cria um dataframe
        (pd.DataFrame({'c0tem': np.nan,
                       'c0hum': np.nan,
                       'c0lum': np.nan,
                       'c0ext': np.nan
                       }, index=[agora])).to_csv(config.CSV['dados'])

    # Faz uma cópia do arquivo de log para BACKUP
    pathlib.Path(config.CSV['log']).rename(config.CSV['dadosBkupDir' + '/LOG-' +
                                                      dt.datetime.now().strftime('%Y-%m-%dT%H:%M:%S') + '.csv'])

    # TODO: adicionar multiplas cópias das fotos

    # Enviar email com backup (utilizar biblioteca de email do python)


'''shutil.copy2(config.CSV['dados'],
             ((config.CSV['dadosBkupDir']) + 'DAT-' + dt.datetime.now().strftime('%Y-%m-%dT%H:%M:%S') + '.csv'))

if pathlib.Path(config.CSV['log']).exists():
shutil.copy2(config.CSV['log'],
             ((config.CSV['dadosBkupDir']) + 'LOG-' + dt.datetime.now().strftime('%Y-%m-%dT%H:%M:%S') + '.csv'))
'''
