#clear()
fruits = {"apple", "banana", "cherry"}
fruits.clear()
print(fruits)

#copy()
fruits = {"apple", "banana", "cherry"}
x = fruits.copy()
print(x)

#difference()
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.difference(y)
print(z)

b = {"blue", "yellow", "banana"}
c = x.difference(y, b)
print(c)

#difference_update()
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.difference_update(y)
print(x)

b = {"blue", "yellow", "banana"}
x.difference_update(y,b)
print(x)

#discard()
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
print(fruits)

#intersection()
x = {"apple", "banana", "cherry"}
y = {"google", "banana", "apple"}
z = x.intersection(y)
print(z)

b = {"blue", "yellow", "banana"}
c = x.intersection(y, b)
print(c)

#intersection_update()
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)

x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}
x.intersection_update(y, z)
print(x)

#isdisjoint()
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}
z = x.isdisjoint(y)
print(z)

#issubset()
x = {"a","b","c"}
y = {"f","e","d","c","b","a"}
z = x.issubset(y)
print(z)

#issuperset()
x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}
z = x.issuperset(y)
print(z)

#pop()
fruits = {"apple", "banana", "cherry"}
x = fruits.pop()
print(x)
print(fruits)

#remove()
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
print(fruits)

#symmetric_difference()
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y) #z = x ^ y
print(z)

#simmetric_difference_update()
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y) # x ^= z
print(x)

#union()
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.union(y) #z = x | y
print(z) 

x = {"a", "b", "c"}
y = {"f", "d", "a"}
z = {"c", "d", "e"}
result = x.union(y, z) #result = x | y | z
print(result)

#update()
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.update(y) # x |= y
print(x)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = {"cherry", "micra", "bluebird"}
x.update(y, z) # x |= y | z
print(x)