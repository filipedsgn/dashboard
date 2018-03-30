import .
import time
import pathlib
import pandas as pd
import datetime as dt

# Importa as configurações
import config

# TODO: colocar em um arquivo novo?
# TODO: Timestamp.now() milisegundos não vai criar coisas separadas
# TODO: adicionar coluna do sensor de gás (MQ-2), e antes de todos para ter preferência de alerta

agora = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

d = {'c0tem': pd.Series(values[0], index=[agora]),
     'c0hum': pd.Series(values[1], index=[agora]),
     'c0lum': pd.Series(values[2], index=[agora]),
     'c0ext': pd.Series(values[3], index=[agora])
     }

df = pd.DataFrame(d, name='dados sensoriais')

# TODO: salvar de tempos em tempos as amostragens em arquivos.csv

def amostrar():
      #Verifica se existe arquivo de dados
      if not pathlib.Path(config.CFG['dados']).exists():
            df =


      # Cria uma instância da função do ADC
      adc = ADS1115(config.CFG['endereco', config.CFG['barramento'])

      # Amostra as entradas analógicas do conversor


      while True:

            # TODO: remover milisegundos
            agora = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            for i in range(4):
                  values[i] = adc.read_adc(i, gain=config.CFG['ganho'])

            df.append(pd.DataFrame({'c0tem': pd.Series(values[0], index=[agora]),
                                    'c0hum': pd.Series(values[1], index=[agora]),
                                    'c0lum': pd.Series(values[2], index=[agora]),
                                    'c0ext': pd.Series(values[3], index=[agora])
                                    }), ignore_index=True))

            time.sleep(5)