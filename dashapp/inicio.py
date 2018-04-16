# Primeiro programa a ser executado
from dashapp import backup, amostragem
from threading import Thread

# Verificar / Definir Timezone
# A cada mês criar um arquivo novo de BACKUP
# Verificar se quantos sensores estão conectados (valores zeros contínuos)


# Checar conexão com a internet


# Fazer backup
backup.bkup()

# Inicializa a amostragem
amostragem.iniciar()

# Inicializa o app
#app()


'''
Threading

from threading import Thread

class Th(Thread):
    def __init__(self.num):
        super().__init__(self)
        self.num = num
    
    def run(self):
        print('Hello')
        print(self.num)
        
a = Th(1)
a = start()
'''