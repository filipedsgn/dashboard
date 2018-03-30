#teste adicionando dados ao dataset
df = {'c0temp': pd.Series(values[0], index=[pd.Timestamp.now()]),
      'c0hum': pd.Series(values[1], index = [pd.Timestamp.now()]),
      'c0lum': pd.Series(values[2], index=[pd.Timestamp.now()]),
      }