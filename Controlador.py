from Vista import Aplicacion
from Cronometro import Cronometro

class Controlador():
    def __init__(self, vista):
        self.app = vista
        self.cronometro = Cronometro()
        #self.app.btnIniciar['command'] = self.iniciar
        self.app.btnIniciar['command'] = self.interruptor
        self.app.btnReiniciar['command'] = self.reiniciar
        self.app.root.mainloop()        

    #Metodo donde se reinicio el cronometro        
    def reiniciar(self):
        self.cronometro.corriendo = False
        self.app.actualizarTiempo(self.cronometro.reiniciar())

    #Metodo para parar el cronometro    
    def interruptor(self):
        if self.cronometro.corriendo:
            self.cronometro.corriendo = False
            self.app.btnIniciar.config(fg ='blue',text='Iniciar')
        else:
            self.cronometro.corriendo = True
            self.app.btnIniciar.config(fg ='red',text='Parar')
            self.iniciar()
        

    #Metodo para iniciar el cronometro  
    def iniciar(self):
        self.app.actualizarTiempo(self.cronometro.iniciar())
        self.app.root.after(100, self.iniciar)