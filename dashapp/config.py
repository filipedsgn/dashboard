#Arquivo de configuração

# TODO: conferir tabela 3 do datasheet do ADS1115
# Escolha o Ganho:
#  - 2/3 = +/-6.144V
#  -   1 = +/-4.096V
#  -   2 = +/-2.048V
#  -   4 = +/-1.024V
#  -   8 = +/-0.512V
#  -  16 = +/-0.256V
# Padrão 1
#
# Escolha o diretório onde contém os arquivos de dados
# Padrão ~/dashapp/df.csv
#
# Escolha o diretório e o nome do arquivo de BACKUP
# Padrão ~/BACKUP/dashapp/
#
# Escolha o email para o qual será enviado o arquivo de BACKUP
# Padrão nenhum

CFG = {
    'ganho': 1,
    'dados': r'~/dashapp/df.csv',
    'backup': r'~/BACKUP/dashapp/',
    'email': 'nenhum',
}

