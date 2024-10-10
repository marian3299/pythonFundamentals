lista = [1, 2, 3, 4]
print(lista)

#ACCEDER Y MODIFICAR
a = [90, "Python", 3.87]
print(a[0]) #90
print(a[1]) #Python
print(a[2]) #3.87

a[0] = "New value" #Cambiamos el valor de a[0]
print('a[0]: ', a[0])

print(a[-1]) #Acceder al ultimo elemento usando -1

#Listas anidadas
x = [1, 2, 3, ['p', 'q', [5, 6, 7]]]
print(x[3][0]) #p
print(x[3][2]) #[5, 6, 7]
print(x[3][2][0]) #5

#Elminar elementos
l = [1, 2, 3, 4, 5]
print('l: ', l)
del l[1]
print('l: ', l)

#Acceder usando : -> [inicio:fin]
l = [1, 2, 3, 4, 5, 6]
print(l[0:2]) #[1, 2]
print(l[2:6]) #[3, 4, 5, 6]

l[0:3] = [0, 0, 0]
print(l) #[0, 0, 0, 4, 5, 6]

#Modificar con operador +
l = [1, 2, 3]
l += [4, 5]
print(l) #[1, 2, 3, 4, 5]

#FUNCION len -> retorna la longitud de un objeto
len(l)


#ITERAR LISTAS
lista = [5, 9, 10]
for l in lista:
    print(l)
#5
#9
#10

#enumerate
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
list(enumerate(seasons))
#[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
list(enumerate(seasons, start=1))
#[(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]

#iterar con index
lista = [5, 9, 10]
for index, l in enumerate(lista):
    print(index, l)
#0 5
#1 9
#2 10

#zip
a = [1, 2, 3]
b = ["Uno", "Dos"]
c = zip(a, b)

print(list(c))
# [(1, 'Uno'), (2, 'Dos')]

numeros = [1, 2]
espanol = ["Uno", "Dos"]
ingles = ["One", "Two"]
frances = ["Un", "Deux"]
c = zip(numeros, espanol, ingles, frances)
print(list(c)) #[(1, 'Uno', 'One', 'Un'), (2, 'Dos', 'Two', 'Deux')]

#iterar dos listas
lista1 = [5, 9, 10]
lista2 = ["Jazz", "Rock", "Djent"]
for l1, l2 in zip(lista1, lista2):
    print(l1, l2)
#5 Jazz
#9 Rock
#10 Djents


#SLICING -> my_list[inicio:fin]
list_1 = [1]
list_2 = list_1[:] #Hace una copia del contenido de list_1
list_1[0] = 2
print(list_2) #[1]

my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3]
print(new_list) #[8,6]

#Indices negativos
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:-1]
print(new_list) #[8, 6, 4]

#Omitiendo start
my_list = [10, 8, 6, 4, 2]
new_list = my_list[:3]
print(new_list) #[10, 8, 6]

#Omitiendo end
my_list = [10, 8, 6, 4, 2]
new_list = my_list[3:]
print(new_list) #[4, 2]


#IN y NOT IN
my_list = [0, 3, 12, 8, 2]

print(5 in my_list) #False
print(5 not in my_list) #True
print(12 in my_list) #True
