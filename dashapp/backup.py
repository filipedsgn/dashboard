import datetime as dt  # Amostragem do tempo
import os  # Criar diretórios
import pathlib  # Verificar a existência de arquivos
import shutil  # Realizar cópias dos arquivos para BACKUP

from dashapp import config, erro


def bkup():
    # Verificar qual se o diretório de Backup foi localizado, senão, informar e criar um novo
    if not pathlib.Path(config.CFG['backup']).exists():
        agora = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Indicar qual erro e quando aconteceu
        erro.tipo(3, agora)
        os.mkdir(config.CFG['backup'])

    # TODO: arrumar aqui, verificar se tem como fazer cópia direto com pandas
    shutil.copy2(config.CFG['dados'],
                 ((config.CFG['backup']) + 'DAT-' + str(dt.datetime.now().strftime('%Y-%m-%dT%H:%M:%S')) + '.csv'))
    shutil.copy2(config.CFG['log'],
                 ((config.CFG['backup']) + 'LOG-' + str(dt.datetime.now().strftime('%Y-%m-%dT%H:%M:%S')) + '.csv'))

    # Enviar email com backup (utilizar biblioteca de email do python)
