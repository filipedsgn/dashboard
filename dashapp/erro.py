import pathlib
# ERROS
# 1 Não existe arquivo de log de erro (erro.py)
# 2 Arquivo de dados inexistente (novo.py)
# 3 Arquivo de BACKUP inexistente (novo.py)
# 4
# 5
# 6
# 7
# TODO: adicionar alerta na página principal

def erro(erro, tempo):
    # Verifica se existe arquivo de log de erros
    if not pathlib.Path(config.CFG['log']).exists():
        # Cria um log
        (pd.DataFrame({'Cod': 1,
                    'Erro': 'Log de erro criado'
                    }, index=[tempo])).to_csv(config.CFG['log'])

    if erro == 2:
        print('Arquivo de dados inexistente')
        (pd.DataFrame({'Cod': 2, 'Erro': 'Arquivo de dados inexistente'
                       },index=[agora])).to_csv(config.CFG['log'], header=False, mode='a')

    if erro == 3:
        print('Email BACKUP inexistente')
        (pd.DataFrame({'Cod': 3, 'Erro': 'Arquivo de BACKUP inexistente'
                       },index=[agora])).to_csv(config.CFG['log'], header=False, mode='a')

