#Funcion input
print("Dime algo...")
anything = input()
print(anything)

#Con argumento
anything = input("Dime lo que sea...")
print("Hmm...", anything, "...¿en serio?")

#Conversion de tipos
#String a number
anything = float(input("Ingresa un número: ")) #float()
something = anything ** 2.0
print(anything, "a la potencia de 2 es", something)

#Number a strig
print("Esto es un string: " + str(something))

x = 1 / 2 + 3 // 3 + 4 ** 2
print(x)