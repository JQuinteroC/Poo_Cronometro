from Tiempo import Tiempo 

class Minuto(Tiempo):
    def __init__(self):
        Tiempo.__init__(self, 0, 59)