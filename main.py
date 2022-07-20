import random
matriz=[[0,0,0], [0, 0, 0], [0, 0, 0]]
aciertos = 0
errores = 0
#print(matriz)
#ciclo para las oportunidades
for n in range(0,5):
    for i in range(0,3):
        for j in range(0,3):
            numero = random.randrange(0,2)
            matriz[i][j] = numero
    print(matriz)
    print("en que posicion crees que no haya un hoyo")
    print("fila...")
    fila = input()
    fila = int(fila)
    print("columna...")
    col = input()
    col = int(col)
    #evaluando si cae o no en un hoyo
    if(matriz[fila] [col]==1):
        print("¡la libraste, no hay hoyo!")
        aciertos = aciertos + 1
    else:
        print("¡Ayyyyyy, Caiste!")
    #evaluando si ya gano
    if (aciertos == 3):
        print("¡Ganaste!")
        break
    #evaluando si ya perdio
    if (errores == 3):
        print("¡Perdiste!")
        break