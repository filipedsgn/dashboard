# Arquivo de configuração

# TODO: escolher a quantidade de conversores
# TODO: conferir tabela 3 do datasheet do ADS1115
# TODO: configurações de IP

# Endereço I2C do ADC
# Padrão: 0x48

# Barramento I2C do ADC
# Padrão: 0

#Ganho:
#  - 2/3 = +/-6.144V
#  -   1 = +/-4.096V
#  -   2 = +/-2.048V
#  -   4 = +/-1.024V
#  -   8 = +/-0.512V
#  -  16 = +/-0.256V
# Padrão: 1

# Diretório onde contém os arquivos de dados
# Padrão: /dashapp/dados.csv

# Diretório e o nome do arquivo de BACKUP
# Padrão: /BACKUP/dashapp/

# Diretório e o nome do arquivo de log de erro
# Padrão: /dashapp/log.csv

# Email para o qual será enviado o arquivo de BACKUP
# Padrão: nenhum

# Telefone para o qual será enviado mensagem de alerta
# Padrão: nenhum

CFG = {
    'endereco': 0x48,
    'barramento': 0,
    'ganho': 1,
    'dados': r'dashapp/dados.csv',
    'backup': r'BACKUP/dashapp/',
    'log': r'dashapp/log.csv',
    'email': 'nenhum',
    'telefone': 'nenhum'
}
