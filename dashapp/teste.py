import .
import time
import pandas as pd
import datetime

import config

df = pd.read_csv(config.DASH_CONFIG['dados'])


#pd.DataFrame({'c0tem': val[0], 'c0hum': val[1], 'c0lum': val[2], 'c0ext': val[3]}, index=[agora])

'''
algum código para confirmar tempo
código de confirmação de leitura do arquivo
código de backup do arquivo csv

se precisar de tempo preciso 
dt.datetime.now(pytz.timezone('America/Sao_Paulo'))
mas acho melhor utilizar tempo local do servidor
'''
# TODO: salvar de tempos em tempos as amostragens em arquivos.csv
# TODO: ver todo o código em passo a passo pra ver se ta na ordem correta

def amostrar():
    # Verifica se existe arquivo de dados
    if not pathlib.Path(config.CFG['dados']).exists():
        df.to_csv(config.CFG['dados'])

    # Cria uma instância da função do ADC
    adc = ADS1115(config.CFG['endereco', config.CFG['barramento'])

    # Amostra as entradas analógicas do conversor

    with open(config.CFG['dados'], 'a') as dados:
        df.to_csv(dados, header=False)

    # TODO: remover milisegundos
    agora = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    for i in range(4):
        val[i] = adc.read_adc(i, gain=config.CFG['ganho'])

    df2 = pd.DataFrame({'c0tem': val[0],
                        'c0hum': val[1],
                        'c0lum': val[2],
                        'c0ext': val[3]
                        }, index=[agora])

    df2.to_csv(config.CFG['dados'], header=False, mode='a')

    time.sleep(5)