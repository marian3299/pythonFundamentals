#DECLARACION
tupla = (1, 2, 3)
print(tupla) #(1, 2, 3)

tupla = 1, 2, 3
print(tupla) #(1, 2, 3)


#ACCEDER A DATOS
my_tuple = (1, 10, 100, 1000)

print(my_tuple[0]) #1
print(my_tuple[-1]) #1000
print(my_tuple[1:]) #(10, 100, 1000)
print(my_tuple[:-2]) #(1, 10)

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")


#ACTUALIZAR DATOS
#Modificar datos
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x) #('apple', 'kiwi', 'cherry')

#Agregar datos
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple) #('apple', 'banana', 'cherry', 'orange')

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y #Sumamos las dos tuplas
print(thistuple) #('apple', 'banana', 'cherry', 'orange')

#Eliminar datos
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple) #('banana', 'cherry')


#DESEMPACAR VALORES
fruits = ("apple", "banana", "pinaple")
(data1, data2, data3) = fruits
print(data1)
print(data2)
print(data3)

#Usando *
fruits = ("apple", "banana", "pinaple", "strawberry", "raspberry")
(data1, data2, *list) = fruits
print(data1)
print(data2)
print(list)

fruits = ("apple", "banana", "pinaple", "strawberry", "raspberry")
(data1, *list, data2, data3) = fruits
print(data1)
print(data2)
print(list)
print(data3)


#ITERACION
names = ("Pepito", "Sofia", "Josefina", "Kira")

for name in names:
  print(name)

for i in range(len(names)):
  print(names[i])

c = 0
while c < len(names):
  print(names[c])
  c += 1



#OPERACIONES
#Juntar dos o mas tuplas -> +
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3) #('a', 'b', 'c', 1, 2, 3)

#Multiplicar el contenido de la tupla -> *
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple) #('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')