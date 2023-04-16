list1 = [i for i in range(1,31)]

for _ in range(28):
    num = int(input())
    list1.remove(num)
    
print(min(list1))
print(max(list1))