# Nurikabe

El juego del Nurikabe es un juego de rompecabezas en el cual se soluciona una matriz inicial de n x m celdas. En algunas de
estas vienen números, a estas celdas se les denomina celdas numeradas. Las celdas son inicialmente de color blancas o negras y
las celdas numeradas siempre son blancas y no pueden cambiar su color. Dos celdas del mismo color se consideran "conectadas"
si son adyacentes vertical u horizontalmente, pero no en diagonal. Las células blancas conectadas forman "islas", mientras que
las células negras conectadas forman el "mar".

![Islas](img/Islas.png?raw=true "Islas")

El desafío es pintar cada celda de blanco o negro, sujeto a las siguientes reglas:
- Cada celda numerada es una celda de isla, el número en ella es el número de celdas en esa isla.
- Cada isla deb e contener solamente una celda numerada.
- Debe haber un solo mar, que no puede contener "piscinas", es decir, áreas de 2X2 de celdas negras.

Una posible solucion al tablero de arriba seria:

![Sol](img/Solucion.png?raw=true "Sol")


## El programa:
Para ejecutar el programa se necesita python al menos en su version 3.0

Correr el comando: 
```bash
python juego.py
```
Desde la carpeta del proyecto

### Resultado
```bash
1 I I I 3 
I I I I I 
5 I I I I 
I I I I I 
I 1 I I I 
Indique las coordenadas de una casilla para pintar el MAR siguiendo este formato:
 x,y
Donde 'x' corresponde a fila, 'y' a la columna
Ejemplo: 1,1
Nota: las filas y columnas empiezan desde el indice 0, por lo tanto para un tablero de 5x5 no es valido ingresar algo como: 1,5
```