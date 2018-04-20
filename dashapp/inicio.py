#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Primeiro programa a ser executado
import backup, amostragem, alarme

# Verificar / Definir Timezone
# A cada mês criar um arquivo novo de BACKUP
# Verificar se quantos sensores estão conectados (valores zeros contínuos)

# Inicia alarme luminoso
alerta = False
led = alarme.LedIndicador()
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
# app()
