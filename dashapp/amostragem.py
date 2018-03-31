import datetime as dt  # Amostragem do tempo
import pathlib  # Verificar a existência de arquivos
import time  # Pausar por 5 segundos TODO: método mais eficiênte? (possivel solução Threading)

import numpy as np  # Célular vazias do panda TODO: útil?
import pandas as pd  # Manipulação de dados

# TODO: arrumar importação do ADC
from dashapp import ADS1X15, config, erro


# TODO: adicionar coluna do sensor de gás (MQ-2), e antes de todos para ter preferência de alerta

def iniciar():
    # Verifica se existe arquivo de dados
    if not pathlib.Path(config.CFG['dados']).exists():
        agora = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Indicar qual erro e quando aconteceu
        erro.tipo(2, agora)

        # Cria um dataframe
        (pd.DataFrame({'c0tem': np.nan,
                       'c0hum': np.nan,
                       'c0lum': np.nan,
                       'c0ext': np.nan
                       }, index=[agora])).to_csv(config.CFG['dados'])

    # Cria uma instância do objeto do conversor Anaógico-Digital
    adc = ADS1115(config.CFG['endereco'], config.CFG['barramento'])

    while True:
        # Captura o tempo atual
        agora = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Amostra as entradas analógicas do conversor
        for i in range(4):
            val[i] = adc.read_adc(i, gain=config.CFG['ganho'])

        # TODO: verificar possibilidade de encurtar assim como linha 22
        df = pd.DataFrame({'c0tem': val[0],
                           'c0hum': val[1],
                           'c0lum': val[2],
                           'c0ext': val[3]
                           }, index=[agora])

        df.to_csv(config.CFG['dados'], header=False, mode='a')

        time.sleep(5)
