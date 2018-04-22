#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pathlib

from lib import info, captura, backup, config

# Verificar / Definir Timezone
# A cada mês criar um arquivo novo de BACKUP
# Verificar se quantos sensores estão conectados (valores zeros contínuos)

# Cria os diretórios
pathlib.Path(config.ARQ['dadosBkupDir']).mkdir(parents=True, exist_ok=True)

# Led indicativo
led = info.Led()
led.setDaemon(True)
led.start()

# Camera
camera = info.Camera()
camera.setDaemon(True)
camera.start()

# Captura foto
camera.foto()

# Fazer backup
backup.bkup()

# Inicializa a captura de valores
capturar = captura.Iniciar()
capturar.setDaemon(True)
capturar.start()

while True:
    pass

# Inicializa o app
# app()
