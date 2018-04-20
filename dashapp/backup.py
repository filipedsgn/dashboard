import datetime as dt
import os
import pathlib
import shutil

from . import config, erro


def bkup():
    # Verificar qual se o diretório de Backup foi localizado, senão, informar e criar um novo
    if not pathlib.Path(config.CSV['backup']).exists():
        # Indicar qual erro e quando aconteceu
        erro.tipo(3)
        os.mkdir(config.CSV['backup'])

    # TODO: arrumar aqui, verificar se tem como fazer cópia direto com pandas
    shutil.copy2(config.CSV['dados'],
                 ((config.CSV['backup']) + 'DAT-' + dt.datetime.now().strftime('%Y-%m-%dT%H:%M:%S') + '.csv'))
    shutil.copy2(config.CSV['log'],
                 ((config.CSV['backup']) + 'LOG-' + dt.datetime.now().strftime('%Y-%m-%dT%H:%M:%S') + '.csv'))

    # Enviar email com backup (utilizar biblioteca de email do python)
