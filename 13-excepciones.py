#TRY...EXCEPT
a=5
b='hola'

try:
    c=a/b
    print(c)
except ZeroDivisionError:
    print("No se puede dividir entre cero")
except TypeError:
    print('Ambos valores deben de ser numeros')


a=5
b='hola'

try:
    c=a/b
    print(c)
except Exception as ex:
    print("Ha ocurrido un error al dividir", type(ex))


#TRY..EXCEPT..ELSE
try:
    x = 2/0
except:
    print("Entra en except, ha ocurrido una excepción")
else:
    print("Entra en else, no ha ocurrido ninguna excepción")

try:
    # La división puede realizarse sin problema
    x = 2/2
except:
    print("Entra en except, ha ocurrido una excepción")
else:
    print("Entra en else, no ha ocurrido ninguna excepción")


#FINALLY
try:
    # Forzamos excepción
    x = 2/0
except:
    # Se entra ya que ha habido una excepción
    print("Entra en except, ha ocurrido una excepción")
finally:
    # También entra porque finally es ejecutado siempre
    print("Entra en finally, se ejecuta el bloque finally")


#raise
x = -1
if x < 0:
  raise Exception("Sorry, no numbers below zero")


x = "hello"
if not type(x) is int:
  raise TypeError("Only integers are allowed")


 

try:
    value = input("Ingresa un valor: ")
    print(value/value)
except ValueError:
    print("Entrada incorrecta...")
except ZeroDivisionError:
    print("Entrada errónea...")
except TypeError:
    print("Entrada muy errónea...")
except:
    print("¡Buuu!")