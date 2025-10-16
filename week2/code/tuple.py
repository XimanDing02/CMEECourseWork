# tuple.py
# Only code in here, understanding of the code are in readme file.
MyTuple = ("a", "b", "c")
print(MyTuple)

print(type(MyTuple))

MyTuple[0]
print(len(MyTuple))

FoodWeb=[('a','b'),('a','c'),('b','c'),('c','c')]
print(FoodWeb)

print(FoodWeb[0])

print(FoodWeb[0][0])

FoodWeb[0] = ("bbb","ccc") 

a = (1, 2, []) 
print(a)

a[2].append(1000)
print(a)

a[2].append(1000)
print(a)

a[2].append((100,10))
print(a)

a = (1, 2, 3)

b = a + (4, 5, 6)
print(b)

c = b[1:]
print(c)

b = b[1:]
print(b)

a = ("1", 2, True)
print(a)
