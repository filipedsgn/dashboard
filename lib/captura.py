import datetime as dt
import time
from threading import Thread

import pandas as pd

from lib import config
from lib.adc import ads1115


# TODO: adicionar coluna do sensor de gás (MQ-2), e antes de todos para ter preferência de alerta

class Iniciar(Thread):
    def __init__(self):
        super().__init__()

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
                canal[i] = self.adc.read_adc(i)

            # Adiciona no arquivo de dados os valores lidos
            pd.DataFrame({'Temperatura': self.interpolar(canal[config.ADC['tempCH']], *config.ADC['tempConfig']),
                          'Umidade': self.interpolar(canal[config.ADC['umidCH']], *config.ADC['umidConfig']),
                          'Luminosidade': self.interpolar(canal[config.ADC['lumiCH']], *config.ADC['lumiConfig']),
                          'Extra': self.interpolar(canal[config.ADC['extrCH']], *config.ADC['extrConfig'])
                          }, index=[agora]).to_csv(config.ARQ['dados'], header=False, mode='a', index_label='Tempo')

            # Intervalo para a próxima amostragem
            time.sleep(config.ADC['amostragem'])
