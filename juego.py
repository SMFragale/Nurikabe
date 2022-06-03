import os
from nurikabe import Nurikabe
from nurikabe import leerTablero

clear = lambda: os.system('cls')


def main():
    clear()
    nkb: Nurikabe = leerTablero("tablero1.nkb")
    juegoTerminado = False
    print("Casillas ", nkb.casillasIslaReq)
    while not juegoTerminado:
        nkb.imprimirTablero()
        print("Indique las coordenadas de una casilla para pintar el MAR siguiendo este formato:\n x,y") 
        print("Donde 'x' corresponde a fila, 'y' a la columna")
        print("Ejemplo: 1,1")
        print("Nota: las filas y columnas empiezan desde el indice 0, por lo tanto para un tablero de 5x5 no es valido ingresar algo como: 1,5")
        entrada = input()
        entrada = entrada.split(",")
        try:
            x = int(entrada[0])
            y = int(entrada[1])
        except:
            print("Error en las entradas")
            continue
        finally:
            clear()
        juegoTerminado = nkb.pintarCelda(x, y)
        print()

if __name__ == "__main__":
    main()
    