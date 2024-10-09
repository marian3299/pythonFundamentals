#while
counter = 10

while counter > 0:
    print('counter: ', counter)
    counter -= 1

while counter: #Cuando llega a cero se considera False
    print('counter: ', counter)
    counter -= 1

#while... else
x = 5
while x > 0:
    x -=1
    print(x) #4,3,2,1,0
else:
    print("El bucle ha finalizado")

x = 5
while True:
    x -= 1
    print(x) #4, 3, 2, 1, 0
    if x == 0:
        break
else:
    # El print no se ejecuta
    print("Fin del bucle")


#for
for i in range(10):
    print("El valor de i es", i)

for i in "Python":
    print(i)

for i in range(2, 10):
    print("El valor de i es", i)

for i in range(2, 10, 2):
    print("El valor de i es", i)


#for... else
for i in range(5):
    print(i)
else:
    print("else:", i)

#break -> detiene la ejecucion de un for o while
cadena = 'Python'
for letra in cadena:
    if letra == 'h':
        print("Se encontró la h")
        break #Se sale del for
    print(letra)

x = 5
while True:
    x -= 1
    print(x)
    if x == 0:
        break
print("Fin del bucle")

#continue -> Se salta la iteracion y pasa a la siguiente
cadena = 'Python'
for letra in cadena:
    if letra == 'P':
        continue
    print(letra)

x = 5
while x > 0:
    x -= 1
    if x == 3:
        continue
    print(x)

