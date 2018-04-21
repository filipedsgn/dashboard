#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pathlib

from lib import alarme, amostragem, backup, config

# Verificar / Definir Timezone
# A cada mês criar um arquivo novo de BACKUP
# Verificar se quantos sensores estão conectados (valores zeros contínuos)

# Cria os diretórios
pathlib.Path(config.CSV['dadosBkupDir']).mkdir(parents=True, exist_ok=True)

# Inicia led de indicação
led = alarme.Led()
led.setDaemon(True)
led.start()

# Checar conexão com a internet

# Tira foto
camera = alarme.Camera()
camera.setDaemon(True)
camera.start()
camera.foto()

# Fazer backup
backup.bkup()

# Inicializa a amostragem
amostrar = amostragem.Iniciar()
amostrar.setDaemon(True)
amostrar.start()

while True:
    pass

# Inicializa o app
# app()
