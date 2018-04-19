# Primeiro programa a ser executado
from dashapp import backup, amostragem, alarme

# Verificar / Definir Timezone
# A cada mês criar um arquivo novo de BACKUP
# Verificar se quantos sensores estão conectados (valores zeros contínuos)

# Inicia alarme luminoso
alerta = False
led = alarme.LEDIndicador()
led.setDaemon(True)
led.start()

# Checar conexão com a internet


# Fazer backup
backup.bkup()

# Inicializa a amostragem
amostrar = amostragem.Iniciar()
amostrar.setDaemon(True)
amostrar.start()

# Inicializa o app
#app()
