import datetime as dt
import pathlib
import time
from threading import Thread

import numpy as np
import pandas as pd

from dashapp import config, conversor, erro

# TODO: adicionar coluna do sensor de gás (MQ-2), e antes de todos para ter preferência de alerta
# TODO: adicionar locking no Thread?



class Iniciar(Thread):
    def __init__(self):
        super().__init__()

        # Verifica se existe arquivo de dados
        if not pathlib.Path(config.CSV['dados']).exists():
            agora = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            # Indicar qual erro e quando aconteceu
            erro.tipo(2, agora)

            # Cria um dataframe
            (pd.DataFrame({'c0tem': np.nan,
                           'c0hum': np.nan,
                           'c0lum': np.nan,
                           'c0ext': np.nan
                           }, index=[agora])).to_csv(config.CSV['dados'])

        self.canal = []
        # Cria uma instância do objeto do conversor Analógico-Digital
        self.adc = conversor.ADS1115(config.CSV['endereco'], config.CSV['barramento'])

    def _interpolar(valor, emin, emax, dmin, dmax):
        eSpan = emax - emin
        dSpan = dmax - dmin
        escala = float(valor - emin) / float(eSpan)

        return dmin + (escala * dSpan)

    def run(self):
        while True:
            # Captura o tempo atual
            agora = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            # Amostra as entradas analógicas do conversor
            for i in range(4):
                self.canal[i] = self.adc.read_adc(i, gain=config.ADC['ganho'])

            (pd.DataFrame({'c0tem': self._interpolar(self.canal[config.ADC['temp']],),
                           'c0hum': self._interpolar(self.canal[config.ADC['humi']],),
                           'c0lum': self._interpolar(self.canal[config.ADC['lumi']],),
                           'c0ext': self._interpolar(self.canal[config.ADC['extr']],)
                           }, index=[agora])).to_csv(config.CSV['dados'], header=False, mode='a')

            time.sleep(5)
