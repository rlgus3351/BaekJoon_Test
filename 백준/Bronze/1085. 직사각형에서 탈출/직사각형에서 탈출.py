x,y,w,h = map(int, input().split())

xgap = x-w if x>w else w-x
ygap = y-h if y>h else h-y
print(min(x,y,xgap, ygap))