'''
El juego del Nurikabe es un juego de rompecabezas en el cual se soluciona una matriz inicial de n x m celdas. En algunas de
estas vienen números, a estas celdas se les denomina celdas numeradas. Las celdas son inicialmente de color blancas o negras y
las celdas numeradas siempre son blancas y no pueden cambiar su color. Dos celdas del mismo color se consideran "conectadas"
si son adyacentes vertical u horizontalmente, pero no en diagonal. Las células blancas conectadas forman "islas", mientras que
las células negras conectadas forman el "mar".
'''
#El desafío es pintar cada celda de blanco o negro, sujeto a las siguientes reglas:
#Cada celda numerada es una celda de isla, el número en ella es el número de celdas en esa isla.
#Cada isla debe contener solamente una celda numerada.
#Cada isla debe contener solamente una celda numerada.

#Clase que representa el tablero con sus respectivas dimensiones
class Nurikabe:

    def __init__(self, n: int, m: int) -> None:
        self.n = n
        self.m = m
        self.tablero = [[None for i in range(m)] for j in range(n)]
        print(self.tablero)


#Lee un tablero de un archivo y lo devuelve como un objeto Nurikabe
def leerTablero(archivo: str) -> Nurikabe:
    f = open(archivo)
    lineas: list[str] = f.readlines()
    lineas = list(map(lambda linea: linea.strip(), lineas))
    dimensiones = lineas[0].split(",")
    n = int(dimensiones[0])
    m = int(dimensiones[1])
    nkb = Nurikabe(n, m)

    #Falta configurar el tablero del Nurikabe no entiendo como funciona en el archivo .nkb


    return nkb




nkb: Nurikabe = leerTablero("tablero1.nkb")