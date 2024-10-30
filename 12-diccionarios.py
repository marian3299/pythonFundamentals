#DECLARACION
d1 = {
  "Nombre": "Sara",
  "Edad": 27,
  "Documento": 1003882
}
print(d1)

d2 = dict([
      ('Nombre', 'Sara'),
      ('Edad', 27),
      ('Documento', 1003882),
])
print(d2)


#ACCESO A DATOS
#Values
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x) #Mustang

y = thisdict.get("model")
print(y) #Mustang

all_values = thisdict.values()
print(all_values)

#Keys
thisdict_keys = thisdict.keys()
print(thisdict_keys)

if "model" in thisdict:
    print("'model' is in the dictionary ")



#MANIPULAR DATOS
#Cambiar valores -> dict[key] = new_value / update(dict)
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018
print(thisdict)

thisdict.update({"brand":"Ferrari"})
print(thisdict)

#Agregar valores -> dict[new_key] = new_value / update(dict)
thisdict["color"] = "red"
print(thisdict)

thisdict.update({"engine":"hibrid"})
print(thisdict)



#ITERACION
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# Print the keys
for x in thisdict:
  print(x)

for key in thisdict.keys():
  print(key)

# Print the values
for x in thisdict:
  print(thisdict[x])

for value in thisdict.values():
  print(value)

#Print keys and values
for key, value in thisdict.items():
  print(key, value)



#DICCIONARIOS ANIDADOS
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

#Acceder a items
print(myfamily["child1"]["name"]) #Emil

#Iteracion
for key, obj in myfamily.items():
  print(key)

  for key in obj: 
    print(obj[key])
