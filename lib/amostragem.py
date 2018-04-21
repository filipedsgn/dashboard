import datetime as dt
import pathlib
import time
from threading import Thread

import numpy as np
import pandas as pd

from lib import config, conversor, erro


# TODO: adicionar coluna do sensor de gás (MQ-2), e antes de todos para ter preferência de alerta
# TODO: adicionar locking no Thread?


class Iniciar(Thread):
    def __init__(self):
        super().__init__()

        # Verifica se existe arquivo de dados
        if not pathlib.Path(config.CSV['dados']).exists():
            # Indicar qual erro
            erro.tipo(2)

            # Cria diretório de dados caso não exista
            pathlib.Path(config.CSV['dadosDir']).mkdir(parents=True, exist_ok=True)

            agora = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            # Cria um dataframe
            (pd.DataFrame({'c0tem': np.nan,
                           'c0hum': np.nan,
                           'c0lum': np.nan,
                           'c0ext': np.nan
                           }, index=[agora])).to_csv(config.CSV['dados'])

        # Cria uma instância do objeto do conversor Analógico-Digital
        self.adc = conversor.ADS1115()

        # Cria variáveis com as configurações
        # TODO: Colocar isso no arquvo de config
        self.tempConf = (config.ADC['nFS'], config.ADC['pFS'], config.ADC['tempMin'], config.ADC['tempMax'])
        self.humiConf = (config.ADC['nFS'], config.ADC['pFS'], config.ADC['humiMin'], config.ADC['humiMax'])
        self.lumiConf = (config.ADC['nFS'], config.ADC['pFS'], config.ADC['lumiMin'], config.ADC['lumiMax'])
        self.extrConf = (config.ADC['nFS'], config.ADC['pFS'], config.ADC['extrMin'], config.ADC['extrMax'])

    @staticmethod
    def interpolar(valor, min1, max1, min2, max2):
        escala = float(valor - min1) / float(max1 - min1)
        return (escala * (max2 - min2)) + min2

    def run(self):
        while True:
            # Captura o tempo atual
            agora = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            canal = [0] * 4
            # Amostra as entradas analógicas do conversor
            for i in range(4):
                canal[i] = self.adc.read_adc(i, gain=config.ADC['ganho'])

            pd.DataFrame({'c0tem': self.interpolar(canal[config.ADC['tempCH']], *self.tempConf),
                          'c0hum': self.interpolar(canal[config.ADC['humiCH']], *self.humiConf),
                          'c0lum': self.interpolar(canal[config.ADC['lumiCH']], *self.humiConf),
                          'c0ext': self.interpolar(canal[config.ADC['extrCH']], *self.extrConf)
                          }, index=[agora]).to_csv(config.CSV['dados'], header=False, mode='a')

            time.sleep(5)
