# ARQUIVO DE LIXEIRA E TESTE

# pd.DataFrame({'c0tem': val[0], 'c0hum': val[1], 'c0lum': val[2], 'c0ext': val[3]}, index=[agora])

# Teste para criação de arquivo csv

import pandas as pd
import numpy as np

dataindex = pd.date_range('2018-3-13', periods=100, freq='5S')

temp = pd.DataFrame({'tem': np.random.randint(20, 37, size=100)}, index=dataindex)
umid = pd.DataFrame({'umi': np.random.randint(50, 90, size=100)}, index=dataindex)
lumi = pd.DataFrame({'lum': np.random.randint(400, 1000, size=100)}, index=dataindex)
extr = pd.DataFrame({'ext': np.random.randint(1024, size=100)}, index=dataindex)

df = pd.concat([temp, umid, lumi, extr], axis=1)

df.to_csv('~/Downloads/teste.csv')