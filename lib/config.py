# Arquivo de configuração
# TODO: completar com o restante das configurações

# ------------------------------------------------------
# (ADC) Endereço I2C do ADC
# Padrão: 0x48

# (ADC) Barramento I2C do ADC
# Padrão: 0

# (ADC) Ganho:
# 2/3 = +/-6.144V
# 1 = +/-4.096V
# 2 = +/-2.048V
# 4 = +/-1.024V
# 8 = +/-0.512V
# 16 = +/-0.256V
# Padrão: 1

# (CSV) Diretório onde contém os arquivos de dados
# Padrão: ~/dashboard/dados.csv

# (CSV) Diretório e o nome do arquivo de BACKUP
# Padrão: ~/BACKUP/dashboard/

# (CSV) Diretório e o nome do arquivo de log de erro
# Padrão: ~/dashboard/log.csv

# (ALR) Email para o qual será enviado o arquivo de BACKUP
# Padrão: nenhum

# (ALR) Telefone para o qual será enviado mensagem de alerta
# Padrão: nenhum

# (AMS) Tempo de amostragem do conversor
# Padrão: 5s
# ------------------------------------------------------

# TODO: definindo o barramento é provavel descartar o modulo I2C e seus chamdos
# TODO: arrumar isso aqui
# TODO: não utilizando endereço e barramento

ADC = {
    'endereco': 0x48,
    'barramento': 1,
    'ganho': 1,
    'pFS': 32767,
    'nFS': 32768,
    'tempCH': 0,
    'humiCH': 1,
    'lumiCH': 2,
    'extrCH': 3,
    'tempMin': 0,
    'tempMax': 100,
    'humiMin': 0,
    'humiMax': 100,
    'lumiMin': 0,
    'lumiMax': 1000,
    'extrMin': 0,
    'extrMax': 100,
}

CSV = {
    'dados': r'/home/pi/dashboard/dados.csv',
    'backup': r'/home/pi/BACKUP/dashboard/',
    'log': r'/home/pi/dashboard/log.csv',
}

ALR = {
    'email': 'nenhum',
    'telefone': 'nenhum',
    'ledvm': 23,
    'ledvr': 18,
}

# TODO: utilizado pra alguma coisa?
AMS = {
    'amostragem': '5S'
}

