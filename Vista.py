from tkinter import *

class Aplicacion():
    def __init__(self):
        #Configuracion ventana
        root = Tk()
        root.geometry('300x200')
        root.resizable(width=False, height=False)
        root.title('Cronometro')
        #Horas, minutos, segundos y decenas de segundo
        horas = Label(root,text="Horas :", fg='red', width=20, font=("","18"))
        horas.pack()
        minutos = Label(root,text="Minutos :", fg = 'red', width=20, font=("","18"))
        minutos.pack()
        segundos = Label(root,text="Segundos :", fg = 'red', width=20, font=("","18"))
        segundos.pack()
        decimas = Label(root,text="Decimas :", fg = 'red', width=20, font=("","18"))
        decimas.pack()
        #Creacion de frame para poner los botones
        frame = Frame(root)
        btnIniciar=Button(frame,fg ='blue',text='Iniciar',command=iniciar)
        btnIniciar.grid(row=1,column=1)
        btnParar=Button(frame,fg = 'red',text='parar',command=parar)
        btnParar.grid(row=1,column=2)
        btnReiniciar=Button(frame,fg='green',text='Reiniciar',command=reiniciar)
        btnReiniciar.grid(row=1,column=3)

        frame.pack()

#Metodo donde se reinicio el cronometro        
def reiniciar():
    print('Reiniciar')

#Metodo para parar el cronometro    
def parar():
    print('Parar')

#Metodo para iniciar el cronometro    
def iniciar():
    print('Iniciar')

 
