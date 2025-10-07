# Assigning and manipulating variables

print(2 == 2)     # True
print(2 != 2)     # False
print(3 / 2)      # 1.5
print(3 // 2)     # 1  (integer division)

print('hola, ' + 'me llamo Samraat')

x = 5
print(x + 3)

y = 2
print(x + y)

x = 'My string'
print(x + ' now has more stuff')

# 这一行如果取消注释，会报错，因为 x 是字符串，y 是整数：
# print(x + y)

print(x + str(y))   # convert int to str
z = '88'
print(x + z)
print(y + int(z))
