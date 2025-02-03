data1 = input()
data2 = input()
a,b,c = map(int, data1)
d,e,f = map(int, data2)

fnum = a * 100 + b * 10 + c
x = fnum * f
y = fnum * e
z = fnum * d
a = x + y * 10 + z * 100
print(x)
print(y)
print(z)
print(a)