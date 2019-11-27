a = 5
b = a
print('b='+str(b))
b = 6
print(a)
print(b)

c = 7
x = [a, b, c]
y = x.copy()
y[1] = 9
print(x)
print(y)

