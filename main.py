from Controlador import Controlador
from Vista import Aplicacion

class programaCronometro():
    def __init__(self):
        v = Aplicacion()
        c = Controlador(v)

def main():
    programaCronometro()
    return 0

if __name__ == '__main__':
    main()
    
