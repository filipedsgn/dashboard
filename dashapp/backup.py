import shutil
import os
import pathlib

import config


def bkup():
    # Verificar qual se o diretório de Backup foi localizado, senão, informar e criar um novo
    # TODO: conferir se isso aqui tá certo, talvez seja necessário mudar no arquivo de config
    # talvez ele vá criar uma pasta home/pi/BACKUP.. na pasta home (conferir como vai funcionar)
    if not pathlib.Path(config.CFG['backup']).exists():
    os.mkdir(config.CFG['backup'])

    # TODO: arrumar aqui, verificar se tem como fazer cópia direto com pandas
    shutil.copy2(config.CFG['dados'], ((config.CFG['backup']) + str(datetime.datetime.now()) + '.csv'))

    # Enviar email com backup (utilizar biblioteca de email do python)