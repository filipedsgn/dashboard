import datetime as dt
import pathlib
import time
from threading import Thread

import numpy as np
import pandas as pd

from lib import config, erro
from lib.adc import ads1115


# TODO: adicionar coluna do sensor de gás (MQ-2), e antes de todos para ter preferência de alerta
# TODO: adicionar locking no Thread?


class Iniciar(Thread):
    def __init__(self):
        super().__init__()

        # Verifica se existe arquivo de dados
        if not pathlib.Path(config.ARQ['dados']).exists():
            # Indicar erro caso não exista
            erro.tipo(2)

            # Cria diretório de dados
            pathlib.Path(config.ARQ['dadosDir']).mkdir(parents=True, exist_ok=True)

            # Captura tempo atual
            agora = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            # Cria um dataframe sem valores
            (pd.DataFrame({'c0tem': np.nan,
                           'c0hum': np.nan,
                           'c0lum': np.nan,
                           'c0ext': np.nan
                           }, index=[agora])).to_csv(config.ARQ['dados'])

        # Cria uma instância do objeto do conversor Analógico-Digital
        self.adc = ads1115.ADS1115()

    # Metódo para conversão de valores
    @staticmethod
    def interpolar(valor, min1, max1, min2, max2):
        escala = float(valor - min1) / float(max1 - min1)
        return (escala * (max2 - min2)) + min2

    def run(self):
        while True:
            # Captura o tempo atual
            agora = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            canal = [0] * 4
            # Captura os valores das entradas analógicas do conversor
            for i in range(4):
                canal[i] = self.adc.read_adc(i, gain=config.ADC['ganho'])

            # Adiciona no arquivo de dados os valores lidos
            pd.DataFrame({'c0tem': self.interpolar(canal[config.ADC['tempCH']], *config.ADC['tempConfig']),
                          'c0hum': self.interpolar(canal[config.ADC['humiCH']], *config.ADC['humiConfig']),
                          'c0lum': self.interpolar(canal[config.ADC['lumiCH']], *config.ADC['lumiConfig']),
                          'c0ext': self.interpolar(canal[config.ADC['extrCH']], *config.ADC['extrConfig'])
                          }, index=[agora]).to_csv(config.ARQ['dados'], header=False, mode='a')

            # Intervalo para a próxima amostragem
            time.sleep(config.ADC['amostragem'])
