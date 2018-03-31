import . # Importar outros módulos contidos no diretório
import shutil # Realizar cópias dos arquivos para BACKUP
import os # Criar diretórios
import pathlib # Verificar a existência de arquivos
import datetime as dt # Amostragem do tempo

# TODO: BACKUP mensal / semanal / diário

def bkup():
    # Verificar qual se o diretório de Backup foi localizado, senão, informar e criar um novo
    if not pathlib.Path(config.CFG['backup']).exists():
        agora = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Indicar qual erro e quando aconteceu
        erro(3, agora)
        os.mkdir(config.CFG['backup'])

    # TODO: arrumar aqui, verificar se tem como fazer cópia direto com pandas
    shutil.copy2(config.CFG['dados'], ((config.CFG['backup']) + str(datetime.datetime.now()) + '.csv'))
    shutil.copy2(config.CFG['log'], ((config.CFG['backup']) + 'LOG-' + str(datetime.datetime.now()) + '.csv'))

    # Enviar email com backup (utilizar biblioteca de email do python)