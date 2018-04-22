import datetime as dt
import pathlib

import pandas as pd

from lib import info, config


# ERROS
# 1 Não existe arquivo de log de erro (erro.py)
# 2 Arquivo de dados inexistente (captura.py)

# TODO: adicionar alerta na página principal
# TODO: ver quais erros ainda estão valendo

def tipo(erro):
    # Captura tempo atual para registro de erro
    agora = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Verifica se existe arquivo de log de erros
    if not pathlib.Path(config.ARQ['log']).exists() or erro == 1:
        info.alerta = True
        (pd.DataFrame({'Cod': 1, 'Erro': 'Log de erro criado'
                       }, index=[agora])).to_csv(config.ARQ['log'])

    if erro == 2:
        info.alerta = True
        (pd.DataFrame({'Cod': 2, 'Erro': 'Arquivo de dados inexistente'
                       }, index=[agora])).to_csv(config.ARQ['log'], header=False, mode='a')

    # TODO: implementar
    elif erro == 4:
        info.alerta = True
        (pd.DataFrame({'Cod': 4, 'Erro': 'Não foi possível estabelecer comunicação com a rede local'
                       }, index=[agora])).to.csv(config.ARQ['log'], header=False, mode='a')
