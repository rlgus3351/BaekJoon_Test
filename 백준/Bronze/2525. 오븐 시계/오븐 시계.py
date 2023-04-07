a = input().split()
b = int(input())
h = int(a[0])
m = int(a[1])

if((m+b)<60):
    m = m+b
else:
    m = m+b    
    h+=m//60
    m = m%60
    if(h>23):
        h-=24
        
print(h,m)
    