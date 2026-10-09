import math
n=int(input())
a= [int(input()) for _ in range(n)]
ps_pl=1
ps_mn=1
for i in range(n):
    if i%2 ==0 and a[i] > 0:
        ps_pl *= a[i]
    if i % 2 != 0 and a[i] <0:
        ps_mn *= a[i]
print(ps_pl - ps_mn)

