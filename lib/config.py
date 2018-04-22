# Arquivo de configuração
# TODO: completar com o restante das configurações

# ------------------------------------------------------
# (ADC) Ganho:
# 2/3 = +/-6.144V
# 1 = +/-4.096V
# 2 = +/-2.048V
# 4 = +/-1.024V
# 8 = +/-0.512V
# 16 = +/-0.256V
# Padrão: 1

# (ADC - amostragem) Intervalo em segundos de cada amostragem
# Padrão: 5

# (ADC - tempCH) Canal do ADC conectado ao sensor de temperatura
# Padrão: 0

# (ADC - humiCH) Canal do ADC conectado ao sensor de humidade
# Padrão: 1

# (ADC - lumiCH) Canal do ADC conectado ao sensor de luminosidade
# Padrão: 2

# (ADC - extrCH) Canal do ADC conectado ao sensor extra
# Padrão: 3

# TODO: arrumar aqui os limites do adc
# (ADC - tempConfig) Parâmetros de configuração ADC da temperatura
# min_ADC - max_ADC - min_temp - max_temp
# Padrão: (0, 100, 0, 100)

# (ADC - humiConfig) Parâmetros de configuração ADC da humidade
# min_ADC - max_ADC - min_humi - max_humi
# Padrão: (0, 100, 0, 100)

# (ADC - lumiConfig) Parâmetros de configuração ADC da luminosidade
# min_ADC - max_ADC - min_lumi - max_lumi
# Padrão: (0, 100, 0, 100)

# (ADC - extrConfig) Parâmetros de configuração ADC da extra
# min_ADC - max_ADC - min_extr - max_extr
# Padrão: (0, 100, 0, 100)

# (ALR - email) Email para o qual será enviado o arquivo de BACKUP
# Padrão: nenhum

# (ALR - telefone) Telefone para o qual será enviado mensagem de alerta
# Padrão: nenhum

# (ALR - ledvm) pino de saída do LED vermelho (padrão GPIO.BCM)
# Padrão: 23

# (ALR - ledvr) pino de saída do LED verde (padrão GPIO.BCM)
# Padrão: 18

# (ARQ - dadosDir) Diretório onde contem o arquivo de dados
# Padrão: /home/pi/dashboard/DADOS

# (ARQ - dados) Arquivo de dados
# Padrão: /home/pi/dashboard/DADOS/dados.csv

# (ARQ - log) Diretório e o nome do arquivo de log de erro
# Padrão: /home/pi/dashboard/DADOS/log.csv

# (ARQ - fotos) Diretório de fotos
# Padrão: /home/pi/dashboard/FOTOS

# (ARQ - dadosBkupDir) Diretório de backup de dados
# Padrão: /home/pi/BACKUP/dashboard/dados
# ------------------------------------------------------

# Algo do conversor
#'pFS': 32767,
#'nFS': 32768,


# TODO: configurar ganho

ADC = {
    'amostragem': 5,
    'tempCH': 0,
    'humiCH': 1,
    'lumiCH': 2,
    'extrCH': 3,
    'tempConfig': (0, 32767, 0, 100),
    'humiConfig': (0, 32767, 0, 100),
    'lumiConfig': (0, 32767, 0, 100),
    'extrConfig': (0, 32737, 0, 100),
}

ALR = {
    'email': 'nenhum',
    'telefone': 'nenhum',
    'ledvm': 23,
    'ledvr': 18,
}

ARQ = {
    'dadosDir': r'/home/pi/dashboard/DADOS',
    'dados': r'/home/pi/dashboard/DADOS/dados.csv',
    'log': r'/home/pi/dashboard/DADOS/log.csv',
    'fotos': r'/home/pi/dashboard/FOTOS',
    'dadosBkupDir': r'/home/pi/BACKUP/dashboard/dados'
}
