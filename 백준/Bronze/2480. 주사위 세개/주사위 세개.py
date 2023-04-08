a = input().split()
x = int(a[0])
y = int(a[1])
z = int(a[2])

if x == y == z:
    print(10000+x*1000)
elif x == y:
    print(1000+x*100)
elif x == z:
    print(1000+z*100)
elif y == z:
    print(1000+y*100)
else:
    print(100 * max(x,y,z))