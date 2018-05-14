#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from lib import info, captura, backup, site

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
siteapp = site.siteApp()
siteapp.setDaemon(True)
siteapp.start()

# Executar programa indefinidamente
while True:
    capturar.join()
    site.join()
