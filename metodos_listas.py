#METODO sort()
z = [10,5,7,2,9]
z.sort()
print(z)

z.sort(reverse=True)
print(z)

def myFunc(e):
  return len(e)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']

cars.sort(key=myFunc)
print(cars)


#METODO reverse()
fruits = ['apple', 'banana', 'cherry']
fruits.reverse()
print(fruits)


#METODO append()
l = [1, 2]
l.append(3)
print(l) #[1, 2, 3]


#METODO insert()
l = [1, 3]
l.insert(1, 2)
print(l) #[1, 2, 3]