import pathlib

import pandas as pd

from dashapp import config, inicio


# ERROS
# 1 Não existe arquivo de log de erro (erro.py)
# 2 Arquivo de dados inexistente (amostragem.py)
# 3 Arquivo de BACKUP inexistente (amostragem.py)
# 4 Não foi possível estabelecer conexão com a rede local (inicio.py)

# TODO: adicionar alerta na página principal

def tipo(erro, tempo):
    # Verifica se existe arquivo de log de erros
    if not pathlib.Path(config.CSV['log']).exists():
        inicio.alerta = True
        (pd.DataFrame({'Cod': 1, 'Erro': 'Log de erro criado'
                       }, index=[tempo])).to_csv(config.CSV['log'])

    if erro == 2:
        inicio.alerta = True
        (pd.DataFrame({'Cod': 2, 'Erro': 'Arquivo de dados inexistente'
                       }, index=[tempo])).to_csv(config.CSV['log'], header=False, mode='a')

    elif erro == 3:
        inicio.alerta = True
        (pd.DataFrame({'Cod': 3, 'Erro': 'Arquivo de BACKUP inexistente'
                       }, index=[tempo])).to_csv(config.CSV['log'], header=False, mode='a')

    elif erro == 4:
        inicio.alerta = True
        (pd.DataFrame({'Cod': 4, 'Erro': 'Não foi possível estabelecer comunicação com a rede local'
                       }, index=[tempo])).to.csv(config.CSV['log'], header=False, mode='a')
