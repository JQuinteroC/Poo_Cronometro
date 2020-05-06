from Tiempo import Tiempo 

class Hora(Tiempo):
    def __init__(self):
        Tiempo.__init__(self, 0, 23)