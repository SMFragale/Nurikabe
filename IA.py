from nurikabe import Nurikabe
import random

def generarCoordenadas(juego: Nurikabe):
    copiaTablero = []
    for fila in juego.tablero:
        copiaTablero.append([j for j in fila])
    copia_nurikabe = Nurikabe(copiaTablero)
    

def generarPosiblesJugadas(filas: int, columnas: int, tablero: list(list)):

    lista = []

    i = random.randint(0, filas)
    j = random.randint(0, columnas)

    while tablero[i][j] != Nurikabe.ISLA or tuple(i,j) in lista:
        i = random.randint(0, filas)
        j = random.randint(0, columnas)

    lista.append(tuple(i,j))
        
    return lista

#Isla de 1
def isla_de_1(juego_fantasma: Nurikabe):
    tablero = juego_fantasma.tablero
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            if type(tablero[i][j]) == int and tablero[i][j] == 1:
                pintarCasilla(juego_fantasma, i-1, j)
                pintarCasilla(juego_fantasma, i, j+1)
                pintarCasilla(juego_fantasma, i+1, j)
                pintarCasilla(juego_fantasma, i, j-1)

#Pintar casilla
def pintarCasilla(juego_fantasma: Nurikabe, i, j):
    tablero = juego_fantasma.tablero
    if i < 0 or j < 0 or j >= juego_fantasma.m or i >= juego_fantasma.n:
        return
    tablero[i][j] = Nurikabe.MAR

#Busca los valores adyacentes a un numero
def adyacente(juego_fantasma: Nurikabe, i, j):
    tablero = juego_fantasma.tablero
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            if type(tablero[i][j]) == int:
                adyAdj(juego_fantasma, i-1, j)
                adyAdj(juego_fantasma, i, j+1)
                adyAdj(juego_fantasma, i+1, j)
                adyAdj(juego_fantasma, i, j-1)

def adyAdj(juego_fantasma: Nurikabe, i, j):
    if i < 0 or j < 0 or j >= juego_fantasma.m or i >= juego_fantasma.n:
        return 
    


#Para cada numero marcar casillas iguales a su numero en todas las direcciones posibles
#Las que al final no queden marcadas son inalcanzables
def casillas_inalcanzables(juego_fantasma: Nurikabe) -> list:
    tablero = juego_fantasma.tablero
    marcadas = {}
    inalcanzables = []
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            if type(tablero[i][j]) == int:
                marcarAlcanzables(i, j, tablero[i][j], tablero, marcadas)
    
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            if marcadas.get(i, j) != True:
                inalcanzables.append((i, j))

    return inalcanzables

def marcarAlcanzables(i:int, j: int, num: int, tablero: list, marcadas: dict):
    if i < 0 or j < 0 or j >= 5 or i >= 5:
        return 
    marcadas[(i,j)] = True
    marcarAlcanzables(i-1, j, num-1, tablero, marcadas)
    marcarAlcanzables(i, j+1, num-1, tablero, marcadas)
    marcarAlcanzables(i+1, j, num-1, tablero, marcadas)
    marcarAlcanzables(i, j-1, num-1, tablero, marcadas)
