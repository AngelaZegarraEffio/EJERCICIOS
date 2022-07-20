lista = []
numero = int(input("Introduce un número en la lista:"))
while numero>=0:
	lista.append(numero)
	numero = int(input("Introduce un número en la lista:"))

for numero in lista:
	print(numero," ",end="")
