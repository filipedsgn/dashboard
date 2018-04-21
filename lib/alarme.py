import datetime as dt
import subprocess
import time
import pathlib
from threading import Thread

from RPi import GPIO

from lib import config


# TODO: Mudar o nome do arquivo

class Led(Thread):
    def __init__(self):
        super().__init__()
        self.alerta = False
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup((config.ALR['ledvm'], config.ALR['ledvr']), GPIO.OUT, initial=GPIO.LOW)

    def run(self):
        while True:
            if self.alerta is True:
                GPIO.output(config.ALR['ledvm'], GPIO.HIGH)
                time.sleep(1)
                GPIO.output(config.ALR['ledvm'], GPIO.LOW)
                time.sleep(2)

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
        # TODO: salvar em diretorio especifico
        # TODO: deixar em aberto ou singleshots?
        # TODO: fast shutter?
        # TODO: configurar modos

        # Criar diretório de fotos caso não existir
        pathlib.Path(config.FIL['fotos']).mkdir(parents=True, exist_ok=True)

        subprocess.run(['raspistill', '-a', '12', '-md', '1', '-o', config.FIL['fotos'] + '/' +
                        dt.datetime.now().strftime('%Y-%m-%dT%H:%M:%S') + '.jpg', '-n', '-t', '1000'])

        # TODO: implementar isso aqui

    def run(self):
        pass


''''
    def video(self, tempo):
        agora = dt.datetime.now().strftime('%Y-%m-%dT%H:%M:%S')

        subprocess.run(['raspivid', '-a', '12', agora, '.h264', '-n'])
'''

'''
def email():
    # config.ALR['email']
    pass


def telefone():
    # config.ALR['telefone']
    pass


def dash_alerta():
    pass
'''
