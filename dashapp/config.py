# Arquivo de configuração

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
# Padrão: ~/dashapp/dados.csv

# (CSV) Diretório e o nome do arquivo de BACKUP
# Padrão: ~/BACKUP/dashapp/

# (CSV) Diretório e o nome do arquivo de log de erro
# Padrão: ~/dashapp/log.csv

# (ALR) Email para o qual será enviado o arquivo de BACKUP
# Padrão: nenhum

# (ALR) Telefone para o qual será enviado mensagem de alerta
# Padrão: nenhum

# (AMS) Tempo de amostragem do conversor
# Padrão: 5s
# ------------------------------------------------------

ADC = {
    'endereco': 0x48,
    'barramento': 0,
    'ganho': 1,
}

CSV = {
    'dados': r'~/dashapp/dados.csv',
    'backup': r'~/BACKUP/dashapp/',
    'log': r'~/dashapp/log.csv',
}

ALR = {
    'email': 'nenhum',
    'telefone': 'nenhum'
    'ledvm': 23,
    'ledvr': 18,
    'ledvmdc': ,
    'ledvmfq': ,
    'ledvddc': ,
    'ledvrfq':
}

AMS = {
    'amostragem': '5S'
}

