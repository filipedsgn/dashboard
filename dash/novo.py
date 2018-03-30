#teste adicionando dados ao dataset

import Adafruit_ADS1x15

adc = Adafruit_ADS1x15.ADS1115()

GAIN = 1

for i in range(4):
      values[i] = adc.read_adc(i, gain=GAIN)

while True:
      df = {'c0temp': pd.Series(values[0], index=[pd.Timestamp.now()]),
            'c0hum': pd.Series(values[1], index = [pd.Timestamp.now()]),
            'c0lum': pd.Series(values[2], index=[pd.Timestamp.now()]),
            }