#newlist = [expression for item in iterable if condition == True]
squares = [x**2 for x in range(10)]
print(squares) #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

squares = [x**2 for x in range(11) if x%2 == 0]
print(squares) #[0, 4, 16, 36, 64, 100]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
fruitsWithA = [x for x in fruits if "a" in x]
print(fruitsWithA) #['apple', 'banana', 'mango']

uppercaswFruits = [x.upper() for x in fruits]
print(uppercaswFruits) #['APPLE', 'BANANA', 'CHERRY', 'KIWI', 'MANGO']

helloList = ["hello" for x in fruits]
print(helloList) #['hello', 'hello', 'hello', 'hello', 'hello']

listWithoutBanana = [x if x != "banana" else "orange" for x in fruits]
print(listWithoutBanana) #['apple', 'orange', 'cherry', 'kiwi', 'mango']

twoDimensionalList = [[i for i in range(2)] for j in range(5)]
print(twoDimensionalList) #[[0, 1], [0, 1], [0, 1], [0, 1], [0, 1]]
