a = input().split()
h = int(a[0])
m = int(a[1])

if(m<45):
    if(h>0):
        h-=1
        m+=60
        m=m-45
    else:
        h=23
        m+=60
        m=m-45
else:
    m= m-45
print(h, m)