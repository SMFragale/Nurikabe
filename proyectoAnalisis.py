import sys, numpy as np

class bcolors:
    AMARILLO = '\033[93m'
    ENDC = '\033[0m'

if len( sys.argv ) < 2:
    print("No puso el nombre del archivo")
    print("Uso: python3", sys.argv[ 0 ], "input_file" )
    sys.exit( 1 )

if __name__ == "__main__":
    cont, valor, posX, posY = 0,0,0,0
    with open( sys.argv[ 1 ] ) as f:
        linea1 = f.readline()
        filas = linea1[0]
        columnas = linea1[2]
        matriz = np.zeros((int(filas),int(columnas)))
        for line in f:
            for t in line.split(','):
                if cont == 0:
                    valor = t
                elif cont == 1:
                    posX = t
                else:
                    posY = t
                cont += 1
            matriz[int(posX)-1][int(posY)-1] = valor
            cont = 0

    print("NURIKABE GAME")
    for line in matriz:
        for character in line:
            if(character != 0):
                print(f"{bcolors.AMARILLO}{int(character)}{bcolors.ENDC}", end=' ')
            else: 
                print(int(character), end=' ')
        print()
    print("Por favor escriba la fila y columna a elegir: ")
    fila = input("fila: ")
    columna = input("columna: ")