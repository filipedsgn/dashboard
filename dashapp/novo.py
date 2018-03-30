import .
import pathlib
import pandas as pd

# Importa as configurações
import config


def amostrar():
      #Verifica se existe arquivo de dados
      if not pathlib.Path(config.CFG['dados']).exists():
            df =


      # Cria uma instância da função do ADC
      adc = ADS1x15()

      # Amostra as entradas analógicas do conversor


      while True:
            for i in range(4):
                  values[i] = adc.read_adc(i, gain=config.CFG['ganho'])

            df = {'c0temp': pd.Series(values[0], index=[pd.Timestamp.now()]),
                  'c0hum': pd.Series(values[1], index = [pd.Timestamp.now()]),
                  'c0lum': pd.Series(values[2], index=[pd.Timestamp.now()]),
                  }