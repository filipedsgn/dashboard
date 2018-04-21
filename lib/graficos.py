import pandas as pd
from lib import config


# TODO: ver locais onde tem parenteses encapsulando objetos, desnecessariamente

def tempLinha(tempo):
    if tempo == '2H':
        # TODO: evitar criar variaveis
        df = pd.read_csv(config.CFG['dados'], names=['Temperatura', 'Umidade', 'Luminosidade', 'Extra'],
                         header=0).tail(720)

def humiLinha():

def lumiLinha():

def extrLinha():