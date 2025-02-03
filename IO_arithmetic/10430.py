lst = list(map(int, input().split())) 
A = lst[0]
B = lst[1]
C = lst[2]
print((A+B)%C)
print(((A%C)+(B%C))%C)
print((A*B)%C)
print(((A%C)*(B%C))%C)