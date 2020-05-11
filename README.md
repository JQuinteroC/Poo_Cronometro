# Cronometro y Paradigma Orientado a Objetos
## Requerimientos
Se solicita un cronometro que pueda iniciar o reiniciar el conteo midiendo horas, minutos, segundos y decimas de segundo que sea realizado en python 3.7 con interfaz grafica y el paradigma orientado a objetos

## Desarrollo
Nuestra propuesta fue hacer uso del modelo MVC, por ser de los más adecuado para el manejo de interfaces.

Usar la libreria [Tkinter](https://docs.python.org/2/library/tk.html) que viene incluidad en el entorno de python y se especializa en el construccion de GUI.

<p align="center">
  <img src="https://github.com/JQuinteroC/Poo_Cronometro/blob/master/UML/Programa.png" alt="GUI">
</p>

El modelado de nuestra solución se baso en crear una clase padre Tiempo, que les da la estructura base a las clases Hora, Minuto, Segundo y Decima, donde todas se diferencias en el número al cual su contador debe retornar a cero (por ejemplo Segundo tiene una frecuencia de 60, pero Decima de 10). 
![Modelo UML](/UML/uml1.png 'Modelo UML')
Estas cuatro clases componen a la clase Cronometro que tiene la facultad de iniciar o reiniciar el conteo del cronometro. La clase Cronometro es la que se comunica con el controlador del MVC

### Programadores
**[Jose Quintero Cañizalez](https://github.com/JQuinteroC) - *20181020061*** y **[Cristhian Camilo Martinez](https://github.com/Moitas500) - *20181020021***
