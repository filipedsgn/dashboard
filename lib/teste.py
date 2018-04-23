# ARQUIVO DE TESTE COM CÓDIGOS DE EXEMPLO

# Banco de dados randomico

'''import pandas as pd
import numpy as np

dataindex = pd.date_range('2018-3-13', periods=100, freq='5S')

temp = pd.DataFrame({'tem': np.random.randint(20, 37, size=100)}, index=dataindex)
umid = pd.DataFrame({'umi': np.random.randint(50, 90, size=100)}, index=dataindex)
lumi = pd.DataFrame({'lum': np.random.randint(400, 1000, size=100)}, index=dataindex)
extr = pd.DataFrame({'ext': np.random.randint(1024, size=100)}, index=dataindex)

df = pd.concat([temp, umid, lumi, extr], axis=1)

df.to_csv('~/Downloads/teste.csv')
'''

# Exemplo Threading
'''
import time
from threading import Thread

class LED(Thread):
        def __init__(self):
            super().__init__()

        def run(self):
            while True:
                if teste == 1:
                    print('teste igual a 1')
                else:
                    print('teste igual a 0')
                time.sleep(1)

teste = 0
ledzinho = LED()
ledzinho.setDaemon(True)
ledzinho.start()
while True:
    teste = not teste
    time.sleep(3)
'''

'''
    pathlib.Path(config.ARQ['dados']).rename(config.ARQ['dadosBkupDir'] + '/DAT-' +
                                             dt.datetime.now().strftime('%Y-%m-%dT%H:%M:%S') + '.csv')

    pathlib.Path(config.ARQ['log']).rename(config.ARQ['dadosBkupDir'] + '/LOG-' +
                                           dt.datetime.now().strftime('%Y-%m-%dT%H:%M:%S') + '.csv')
'''