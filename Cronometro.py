from Hora import Hora
from Minuto import Minuto
from Segundo import Segundo
from Decima import Decima

class Cronometro(object):
    def __init__(self):
        self.horas = Hora()
        self.minutos = Minuto()
        self.segundos = Segundo()
        self.decimas = Decima()
        self.corriendo = False

    def iniciar(self):
        if self.corriendo:
            if self.decimas.iniciar() == 0:
                if self.segundos.iniciar() == 0:
                    if self.minutos.iniciar() == 0:
                        self.horas.iniciar()
        return self.decimas.valor, self.segundos.valor, self.minutos.valor, self.horas.valor

    def reiniciar(self):    
        return self.decimas.reiniciar(), self.segundos.reiniciar(), self.minutos.reiniciar(), self.horas.reiniciar()