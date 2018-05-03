#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from lib import info, captura, backup, site

# Verificar / Definir Timezone
# A cada mês criar um arquivo novo de BACKUP
# Verificar se quantos sensores estão conectados (valores zeros contínuos)

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

# Inicializa a homepage
siteapp = site.siteAPP()
siteapp.setDaemon(True)
siteapp.start()

# TODO: não precisa desses dois join
while True:
    capturar.join()
    site.join()

# Inicializa o app
# app()
