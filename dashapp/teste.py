import time
import Adafruit_ADS1x15
import pandas as pd
import numpy as np

import config

df = pd.read_csv(config.DASH_CONFIG['dados'])

'''
algum código para confirmar tempo
código de confirmação de leitura do arquivo
código de backup do arquivo csv

se precisar de tempo preciso 
dt.datetime.now(pytz.timezone('America/Sao_Paulo'))
mas acho melhor utilizar tempo local do servidor

datetime sem milisegundo
https://stackoverflow.com/questions/7999935/python-datetime-to-string-without-microsecond-component/25320581
'''

# É possível mudar o endereço I2C padrão (0x48) e/ou barramento I2C passando os seguintes parâmentros opcionais:
#adc = Adafruit_ADS1x15.ADS1015(address=0x49, busnum=1)

adc = Adafruit_ADS1x15.ADS1115()

GAIN = 1

while True:
    values = [0]*4

    for i in range(4):
        values[i] = adc.read_adc(i, gain=GAIN)

    #colocar um time sleep aqui

    df = pd.DataFrame()
