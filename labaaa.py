import math
n= int(input("N = "))
a= [int(input()) for _ in range(n)]
max_1= None
min_2=None
for i in range(n-1):
    pos=i+1
    p= a[i] * a[i+1]
    if pos%2==0:
        if max_1 is None or p> max_1:
            max_1=p
    else:
        if min_2 is None or p< min_2:
            min_2=p
print("Разность:",max_1 - min_2)