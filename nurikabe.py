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
#Debe haber un solo mar, que no puede contener "piscinas", es decir, áreas de 2X2 de celdas negras.

#Clase que representa el tablero con sus respectivas dimensiones
import Colors
    
def printError(error: str):
    print(f"{Colors.FAIL}{error}{Colors.ENDC}")

class Nurikabe:

    MAR = "M"
    ISLA = "I"

    def __init__(self, n: int, m: int) -> None:
        self.n = n
        self.m = m
        self.tablero = [[self.ISLA for i in range(m)] for j in range(n)]
    
    def __init__(self, tablero: list(list)) -> None:
        self.n = len(tablero[0])
        self.m = len(tablero)
        self.tablero = tablero

    # Imprime el tablero
    def imprimirTablero(self):
        print(end="  ")
        for num in range(5):
            print(f"{num}", end=" ")

        print()

        for i in range(self.n):
            print(i, end=" ")
            for j in range(self.m):
                actual = self.tablero[i][j]
                if actual == self.MAR:
                    print(f"{Colors.OKBLUE}M{Colors.ENDC}", end=" ")
                elif actual == self.ISLA:
                    print(f"{Colors.OKGREEN}I{Colors.ENDC}", end=" ")
                else:
                    print(f"{Colors.BOLD}{actual}{Colors.ENDC}", end=" ")
            print()
    
    # Pinta la celda en la coordenada x, y.
    #Retorna False si el juego continua, True si el juego se acabo
    def pintarCelda(self, x: int, y: int) -> bool:
        if x > self.n or y > self.m or x < 0 or y < 0:
            printError(f"Las coordenadas deben estar en el rango del tablero. x: {self.n}, y: {self.m}")
            return
        if self.tablero[x][y] != self.ISLA:
            printError(f"No se puede pintar mar en esta posicion")
            return
        
        copiaTablero = []
        for fila in self.tablero:
            copiaTablero.append([j for j in fila])

        copiaTablero[x][y] = self.MAR
        #Realizar jugada fantasma

        #Debe haber un solo mar, que no puede contener "piscinas", es decir, áreas de 2X2 de celdas negras.
        if not self.marUnico(x, y, copiaTablero):
            printError("Con esta jugada el mar no seria unico")
            return False
        if self.hayPiscinas(copiaTablero):
            printError("Con esta jugada se genera una piscina")
            return False
        
        #if not self.revisarIslas(copiaTablero):
            #print("Con esta jugada existe una isla incorrecta")
            #return False
        
        self.tablero[x][y] = self.MAR

        if self.verificarTableroLleno():
            print("Victoria! El tablero fue completado correctamente")
            return True
        return False

    
    #Solo debe llamarse cuando el tablero esta lleno. Indica si el jugador gana o pierde
    def verificarTableroLleno(self):
        for i in range(len(self.tablero)):
            for j in range(len(self.tablero[i])):
                if type(self.tablero[i][j]) == int :
                    if not self.islaValidaFinal(i, j):
                        return False
        return True

    #Indica si en un tablero existen piscinas (bloques de MAR de 2x2)
    def hayPiscinas(self, tablero):
        for i in range(len(tablero)):
            for j in range(len(tablero[i])):
                if tablero[i][j] == self.MAR:
                    if i+1 < len(tablero) and j+1 < len(tablero[i]):
                        #Revisa si genera una piscina
                        if tablero[i+1][j] == self.MAR and tablero[i][j+1] == self.MAR and tablero[i+1][j+1] == self.MAR:
                            return True
        return False

    #Indica si el mar de un tablero es unico o no
    def marUnico(self, x, y, tablero):
        marcados = {}
        self.marcarMar(x, y, tablero, marcados)
        for i in range(len(tablero)):
            for j in range(len(tablero[i])):
                if tablero[i][j] == self.MAR:
                    #Para cada casilla de mar, si no esta marcada, significa que esta separada del resto del mar
                    if marcados.get((i,j)) != True:
                        return False
        return True

    #Dada una casilla de MAR, marca todas las casillas de mar conectadas a ella en el diccionario @marcados
    def marcarMar(self, x, y, tablero: list, marcados: dict):
        if x < 0 or y < 0 or x >= len(tablero[0]) or y >= len(tablero) or marcados.get((x,y)) or tablero[x][y] != self.MAR:
            return
        marcados[(x,y)] = True
        self.marcarMar(x+1, y, tablero, marcados) 
        self.marcarMar(x-1, y, tablero, marcados)
        self.marcarMar(x, y+1, tablero, marcados)
        self.marcarMar(x, y-1, tablero, marcados)
    
    #Indica si la isla es valida a nivel general (solo debe llamarse cuando el tablero este lleno)
    def islaValidaFinal(self, x, y):
        if type(self.tablero[x][y]) !=  int:
            return False
        marcados = {}
        casillasIsla = self.contarCasillasIsla(x, y, self.tablero, marcados)
        if(casillasIsla !=  self.tablero[x][y]):
            return False
        return True

    #islaIndefinida indica si ya se marco la casilla con el numero de islas. 
    def contarCasillasIsla(self, x, y, tablero: list, marcados: dict):
        if x < 0 or y < 0 or x >= len(tablero[0]) or y >= len(tablero) or marcados.get((x,y)):
            return 0
        
        if type(tablero[x][y]) != int:
            if tablero[x][y] != "I":
                return 0
            
        marcados[(x,y)] = True
        return 1 + self.contarCasillasIsla(x+1, y, tablero, marcados) + self.contarCasillasIsla(x-1, y, tablero, marcados) + self.contarCasillasIsla(x, y+1, tablero, marcados) + self.contarCasillasIsla(x, y-1, tablero, marcados)
        
    
#Lee un tablero de un archivo y lo devuelve como un objeto Nurikabe
def leerTablero(archivo: str) -> Nurikabe:
    f = open(archivo)
    lineas: list[str] = f.readlines()
    lineas = list(map(lambda linea: linea.strip(), lineas))
    dimensiones = lineas[0].split(",")
    n = int(dimensiones[0])
    m = int(dimensiones[1])
    nkb = Nurikabe(n, m)

    for i in range(1, len(lineas)):
        linea = lineas[i].split(",")
        n = int(linea[1]) - 1
        m = int(linea[2]) - 1
        nkb.tablero[n][m] = int(linea[0])

    return nkb