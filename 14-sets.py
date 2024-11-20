thisset = {"apple", "banana", "cherry"}

print(thisset)


#Duplicated items
thisset = {"apple", "banana", "cherry", "apple",}
print(thisset)

#Same values
#True = 1
#False = 0
thisset = {"apple", "banana", "cherry", True, 0, False, 1}

print(thisset)

#Length of a set
thisset = {"apple", "banana", "cherry"}

print(len(thisset))

#Creating set with its contructor
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)


#ACCES SET ITEMS ----------------------------------
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

print('banana' in thisset)
print('banana' not in thisset)


#ADD ITEMS -----------------------------------------
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)

