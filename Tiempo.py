class Tiempo():
    def __init__(self, valor, frecuencia):
        self.valor = valor
        self.frecuencia = frecuencia

    def iniciar(self):
        if self.valor < self.frecuencia:
            self.valor += 1
        else:
            self.valor = 0
        return self.valor

    def reiniciar(self):
        self.valor = 0
        return self.valor