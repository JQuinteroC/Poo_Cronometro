from tkinter import *

class Aplicacion():
    def __init__(self):
        #Configuracion ventana
        self.root = Tk()
        self.root.geometry('300x200')
        self.root.resizable(width=False, height=False)
        self.root.title('Cronometro')

        #Horas, minutos, segundos y decenas de segundo
        self.horas = Label(self.root,text="Horas :", fg='red', width=20, font=("","18"))
        self.horas.pack()
        self.minutos = Label(self.root,text="Minutos :", fg = 'red', width=20, font=("","18"))
        self.minutos.pack()
        self.segundos = Label(self.root,text="Segundos :", fg = 'red', width=20, font=("","18"))
        self.segundos.pack()
        self.decimas = Label(self.root,text="Decimas :", fg = 'red', width=20, font=("","18"))
        self.decimas.pack()

        #Creacion de frame para poner los botones
        frame = Frame(self.root)
        self.btnIniciar=Button(frame,fg ='blue',text='Iniciar')
        self.btnIniciar.grid(row=1,column=1)
      #  self.btnParar=Button(frame,fg = 'red',text='parar')
      #  self.btnParar.grid(row=1,column=2)
        self.btnReiniciar=Button(frame,fg='green',text='Reiniciar')
        self.btnReiniciar.grid(row=1,column=3)
        frame.pack()

    def actualizarTiempo(self, tiempo):
        formato = '{0:02}'
        self.horas['text'] = 'Horas: ' + formato.format(tiempo[3])
        self.minutos['text'] = 'Minutos: ' + formato.format(tiempo[2])
        self.segundos['text'] = 'Segundos: ' + formato.format(tiempo[1])
        self.decimas['text'] = 'Decimas: ' + formato.format(tiempo[0])