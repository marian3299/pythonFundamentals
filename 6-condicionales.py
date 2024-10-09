#if
x = int(input("Ingrese un numero: "))

if x > 10:
    print(x, "es mayor a 10")

#if ... else
number1 = int(input("Ingresa el primer número: "))
number2 = int(input("Ingresa el segundo número: "))
 
if number1 > number2:
    larger_number = number1
else:
    larger_number = number2
 
print("El número más grande es:", larger_number)

#Condicional en una sola linea
if number1 > number2: larger_number = number1
else: larger_number = number2
print("El número más grande es:", larger_number)


#if .. elif .. else
y = int(input("Ingrese un numero: "))

if y > 10:
    print(y, "es mayor a 10")
elif y < 10 and y > 0:
    print(y, "es menor a 10")
else:
     print(y, "es menor a 0")
