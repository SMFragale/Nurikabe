from time import sleep
from itertools import combinations
from nurikabe import leerTablero
from nurikabe import Nurikabe
import copy
import os

clear = lambda: os.system('cls')
    
# Lista con todas pas posibles combinaciones de soluciones
# Una solucion es una serie de coordenadas a marcar como mar
def generarPosiblesJugadas(juego_fantasma: Nurikabe):
    tablero = juego_fantasma.tablero
    casillasIsla = []

    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
             if tablero[i][j] == Nurikabe.ISLA:
                 casillasIsla.append((i,j))

    numCasillasMarcar = contarCasillasIsla(juego_fantasma) - juego_fantasma.casillasIslaReq

    jugadas = list(combinations(casillasIsla, numCasillasMarcar))

    return jugadas

# Numero de casillas isla en el tablero
def contarCasillasIsla(juego_fantasma: Nurikabe):
    tablero = juego_fantasma.tablero
    numeroCasillasIsla = 0
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
             if tablero[i][j] == Nurikabe.ISLA or type(tablero[i][j]) == int:
                 numeroCasillasIsla += 1
    
    return numeroCasillasIsla

# Isla de 1
def isla_de_1(juego_fantasma: Nurikabe):
    tablero = juego_fantasma.tablero
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            if type(tablero[i][j]) == int and tablero[i][j] == 1:
                pintarCasilla(juego_fantasma, i-1, j)
                pintarCasilla(juego_fantasma, i, j+1)
                pintarCasilla(juego_fantasma, i+1, j)
                pintarCasilla(juego_fantasma, i, j-1)

# Pintar casilla
def pintarCasilla(juego_fantasma: Nurikabe, i, j):
    tablero = juego_fantasma.tablero
    if i < 0 or j < 0 or j >= juego_fantasma.m or i >= juego_fantasma.n:
        return
    tablero[i][j] = Nurikabe.MAR

# Busca los valores adyacentes a un numero
def adyacente(juego_fantasma: Nurikabe):
    tablero = juego_fantasma.tablero
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            if type(tablero[i][j]) == int:
                adyAdj(juego_fantasma, i-1, j, 0, i, j)
                adyAdj(juego_fantasma, i, j+1, 0, i, j)
                adyAdj(juego_fantasma, i+1, j, 0, i, j)
                adyAdj(juego_fantasma, i, j-1, 0, i, j)

# Revisa el adyacente del adyacente para verificar si es mar 
def adyAdj(juego_fantasma: Nurikabe, i: int, j: int, cont: int, x: int, y: int):
    tablero = juego_fantasma.tablero
    mar = False
    if i < 0 or j < 0 or j >= juego_fantasma.m or i >= juego_fantasma.n:
        return
    if cont < 1:
        mar = adyAdj(juego_fantasma, i-1, j, 1, x, y)
        if mar == True:
            tablero[i][j] = Nurikabe.MAR
        mar = adyAdj(juego_fantasma, i, j+1, 1, x, y)
        if mar == True:
            tablero[i][j] = Nurikabe.MAR
        mar = adyAdj(juego_fantasma, i+1, j, 1, x, y)
        if mar == True:
            tablero[i][j] = Nurikabe.MAR
        mar = adyAdj(juego_fantasma, i, j-1, 1, x, y)
        if mar == True:
            tablero[i][j] = Nurikabe.MAR
    else:
        if type(tablero[i][j]) == int and (i != x or j != y):
            return True
        


# Para cada numero marcar casillas iguales a su numero en todas las direcciones posibles
# Las que al final no queden marcadas son inalcanzables
def casillas_inalcanzables(juego_fantasma: Nurikabe):
    tablero = juego_fantasma.tablero
    marcadas = {}
    inalcanzables = []
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            if type(tablero[i][j]) == int:
                marcarAlcanzables(i, j, tablero[i][j], tablero, marcadas)
    
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            if marcadas.get((i, j)) != True:
                pintarCasilla(juego_fantasma, i, j)
                #inalcanzables.append((i, j))

def marcarAlcanzables(i:int, j: int, num: int, tablero: list, marcadas: dict):
    if i < 0 or j < 0 or j >= 5 or i >= 5 or num <= 0:
        return 
    marcadas[(i,j)] = True
    marcarAlcanzables(i-1, j, num-1, tablero, marcadas)
    marcarAlcanzables(i, j+1, num-1, tablero, marcadas)
    marcarAlcanzables(i+1, j, num-1, tablero, marcadas)
    marcarAlcanzables(i, j-1, num-1, tablero, marcadas)


def encontrarSol(juego_fantasma: Nurikabe, jugadas_posibles: list):

    sol_es_valida = False
    comb_valida = -1

    for i in range(len(jugadas_posibles)):
        copia_nurikabe = copy.deepcopy(juego_fantasma)
        for j in range(len(jugadas_posibles[i])):
            if j == len(jugadas_posibles[i]) - 1:
                sol_es_valida = copia_nurikabe.pintarCeldaSinTexto(jugadas_posibles[i][j][0], jugadas_posibles[i][j][1])
            else:
                pintarCasilla(copia_nurikabe, jugadas_posibles[i][j][0], jugadas_posibles[i][j][1])
        if sol_es_valida:
            comb_valida = i
            break
    
    if sol_es_valida:
        return comb_valida
    else:
        return -1

def jugarIA(soluciones_posibles: list, sol_correcta: int, juego_fantasma: Nurikabe):
    for i in range(len(soluciones_posibles[sol_correcta])):
        sleep(1)
        print("----")
        pintarCasilla(juego_fantasma, soluciones_posibles[sol_correcta][i][0], soluciones_posibles[sol_correcta][i][1])
        juego_fantasma.imprimirTablero()

    print("JUEGO FINALIZADO")

        
def main():
    clear()
    nkb: Nurikabe = leerTablero("tablero1.nkb")
    print("Casillas ", nkb.casillasIslaReq)

    # Buscar sol 

    print("Filtro 1. Islas de 1")

    isla_de_1(nkb)

    print("Filtro 2. Casillas adyacentes")
    adyacente(nkb)

    print("Filtro 3. Casillas inalcanzables")
    casillas_inalcanzables(nkb)

    nkb.imprimirTablero()

    posibles_jugadas = generarPosiblesJugadas(nkb)
    sol = encontrarSol(nkb, posibles_jugadas)

    if sol == -1:
        print("No se encontró solución para este tablero")
        return

    jugarIA(posibles_jugadas, sol, nkb)
    # ---------

if __name__ == "__main__":
    main()
