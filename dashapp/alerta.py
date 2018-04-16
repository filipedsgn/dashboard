from dashapp import config
from RPi import GPIO
from threading import Thread
import time

class LED(Thread):
    def __init__(self):
        super().__init__(self)
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup((config.ALR['ledvm'], config.ALR['ledvr']), GPIO.OUT, initial=GPIO.LOW)


    def run(self):
        While True:
            if alerta == True:
                GPIO.output(config.ALR['ledvm'], GPIO.HIGH)
                time.sleep(1)
                GPIO.output(config.ALR['ledvm'], GPIO.LOW)
                time.sleep(2)

            else:
                GPIO.output(config.ALR['ledvr'], GPIO.HIGH)
                time.sleep(1)
                GPIO.output(config.ALR['ledvr'], GPIO.LOW)
                time.sleep(5)

def email():
    # config.ALR['email']
    pass

def telefone():
    # config.ALR['telefone']
    pass

def dashAlerta():
    pass

alerta = False
led = LED()
led.start()