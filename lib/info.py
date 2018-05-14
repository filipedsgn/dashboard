import datetime as dt
import pathlib
import subprocess
import time
from threading import Thread

from RPi import GPIO

from lib import config


class Led(Thread):
    def __init__(self):
        super().__init__()
        # Inicia alerta desligado
        self.alerta = False
        # Configura pinos IO padrão BCM
        GPIO.setmode(GPIO.BCM)
        # Desabilita avisos das conexões de pinos
        GPIO.setwarnings(False)
        # Define os pinos dos LEDS como saída e inicio em nível baixo
        GPIO.setup((config.ALR['ledvm'], config.ALR['ledvr']), GPIO.OUT, initial=GPIO.LOW)

    def run(self):
        # Executar interminavelmente
        while True:
            # Se o alerta estiver ligado, ativa o led vermelho
            if self.alerta is True:
                GPIO.output(config.ALR['ledvm'], GPIO.HIGH)
                time.sleep(1)
                GPIO.output(config.ALR['ledvm'], GPIO.LOW)
                time.sleep(2)

            # Caso contrário, led verde ativo
            else:
                GPIO.output(config.ALR['ledvr'], GPIO.HIGH)
                time.sleep(1)
                GPIO.output(config.ALR['ledvr'], GPIO.LOW)
                time.sleep(5)


class Camera(Thread):
    def __init__(self):
        super().__init__()

    @staticmethod
    def foto():
        # Criar diretório de fotos caso não existir
        pathlib.Path(config.ARQ['fotos']).mkdir(parents=True, exist_ok=True)

        # Tira foto
        subprocess.run(['raspistill', '-a', '12', '-md', '1', '-o', config.ARQ['fotos'] + '/' +
                        dt.datetime.now().strftime('%Y-%m-%dT%H:%M:%S') + '.jpg', '-n', '-t', '1000'])

    def run(self):
        pass
