from Controlador import Controladors
from Vista import Aplicacion

class programaCronometro():
    def __init__(self):
        v = Aplicacion()
        c = Controladors(v)

def main():
    programaCronometro()
    return 0

if __name__ == '__main__':
    main()
    
