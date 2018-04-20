import datetime as dt
import subprocess
import time
from threading import Thread

from RPi import GPIO

from . import config, inicio


# TODO: Mudar o nome do arquivo

class LedIndicador(Thread):
    def __init__(self):
        super().__init__()
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup((config.ALR['ledvm'], config.ALR['ledvr']), GPIO.OUT, initial=GPIO.LOW)

    def run(self):
        while True:
            if inicio.alerta is True:
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
        agora = dt.datetime.now().strftime('%Y-%m-%dT%H:%M:%S')

        subprocess.run(['raspistill', '-a', '12', agora, '.jpg', '-n'])

    # TODO: implementar isso aqui


'''
    def video(self):
        agora = dt.datetime.now().strftime('%Y-%m-%dT%H:%M:%S')

        subprocess.run(['raspivid', '-a', '12', agora, '.h264', '-n'])
'''


def email():
    # config.ALR['email']
    pass


def telefone():
    # config.ALR['telefone']
    pass


def dash_alerta():
    pass
