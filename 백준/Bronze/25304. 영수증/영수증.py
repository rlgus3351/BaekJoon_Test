price = int(input())
n = int(input())
for i in range(n):
    a,b = map(int, input().split())
    price = price - (a*b)

if(price==0):
    print("Yes")
else:
    print("No")