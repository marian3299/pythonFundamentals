def message():
    print("Hello world")

message()


def hello(name):
    print("Hola", name)

hello("Mariana") 

def suma(a,b):
    return a + b

result = suma(3,2)
print(result)


def introduction(first_name, last_name):
    print("Hola, mi nombre es", first_name, last_name)
 
introduction(first_name = "James", last_name = "Bond")
introduction(last_name = "Skywalker", first_name = "Luke")


def resta(a,b,c=2):
    return a-b-c

result = resta(10,4)
print(result)


def numero_par(num):
    if(num % 2 == 0):
        return True

print(numero_par(4))
print(numero_par(5))


def sumaArgs(*args):
    s=0
    for arg in args:
        s += arg
    
    return s

print(sumaArgs(1,2,3,4)) #10
print(sumaArgs(12,20,-5,3,9)) #39



def suma(**kwargs):
    s = 0
    for key, value in kwargs.items():
        print(key, "=", value)
        s += value
    return s
    
print(suma(a=3, b=10, c=3))