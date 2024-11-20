#clear()
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.clear()

print(car) #{}

#copy()
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.copy()

print(x) #{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}


#fromkeys(keys, value=None)
x = ('key1', 'key2', 'key3')
y = 0

thisdict = dict.fromkeys(x, y)

print(thisdict) #{'key1': 0, 'key2': 0, 'key3': 0}


#get(keyname, value=None)
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.get("model")
print(x) #Mustang

y = car.get("price", 15000)
print(y) #1500


#items()
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.items()
print(x) #dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])


#keys()
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.keys()
car["color"] = "white"
print(x) #dict_keys(['brand', 'model', 'year', 'color'])


#pop(keyname, defaultvalue) 
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
deleted_item = car.pop("model")
print(car)
print(deleted_item)


#popitem()
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
poped_item = car.popitem()
print(car)
print(poped_item)


#setdefault(keyname, value=None)
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.setdefault("color", "white")
y = car.setdefault("brand")

print(x)
print(y)
print(car)


#updtae(iterable)
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.update({"color": "White"}) 
print(car)


#values()
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.values()
print(x)