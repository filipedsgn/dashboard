import pathlib

import pandas as pd

from dashapp import config


# ERROS
# 1 Não existe arquivo de log de erro (erro.py)
# 2 Arquivo de dados inexistente (amostragem.py)
# 3 Arquivo de BACKUP inexistente (amostragem.py)

# TODO: adicionar alerta na página principal

def tipo(erro, tempo):
    # Verifica se existe arquivo de log de erros
    if not pathlib.Path(config.CFG['log']).exists():
        # Cria um log
        (pd.DataFrame({'Cod': 1,
                       'Erro': 'Log de erro criado'
                       }, index=[tempo])).to_csv(config.CFG['log'])

    if erro == 2:
        print('Arquivo de dados inexistente')
        (pd.DataFrame({'Cod': 2, 'Erro': 'Arquivo de dados inexistente'
                       }, index=[tempo])).to_csv(config.CFG['log'], header=False, mode='a')

    if erro == 3:
        print('Arquivo de BACKUP inexistente')
        (pd.DataFrame({'Cod': 3, 'Erro': 'Arquivo de BACKUP inexistente'
                       }, index=[tempo])).to_csv(config.CFG['log'], header=False, mode='a')
