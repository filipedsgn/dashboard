import config #arquivo de configuração
import datetime #datas e horas
import pandas as pd #planilhas

# Verificar / Definir Timezone


# Criar arquivo csv inicial se não existir


# Fazer backup TODO: arrumar aqui
shutil.copy2(config.CFG['dados'], (config.CFG['backup']).append(datetime.datetime.now()))


# Verificar se as conexões estão corretas

# Verificar se quantos sensores estão conectados (valores zeros contínuos)

#inicializar o app

df = pd.DataFrame()
