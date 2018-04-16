from dashapp import config
from RPi import GPIO
import time


# TODO: configurar esses LED em uma função?
class LED(object):
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup((config.ALR['ledvm'], config.ALR['ledvr']), GPIO.OUT, initial=GPIO.LOW)


    def ledVM(self):
        GPIO.output(config.ALR['ledvm'], GPIO.HIGH)
        GPIO.output(config.ALR['ledvm'], GPIO.LOW)


    def ledVERDE():

        GPIO.output(config.ALR['ledvr'], GPIO.HIGH)
        GPIO.output(config.ALR['ledvr'], GPIO.LOW)

def email():
    # config.ALR['email']
    pass

def telefone():
    # config.ALR['telefone']
    pass

def dashAlerta():
    pass