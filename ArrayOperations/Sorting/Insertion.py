#Insertion sort : Select a part and sort it
ls = list(map(int,input("Enter the list: ").split()))

for i in range(1,len(ls)):
    for j in range(i,-1,-1):
        if ls[i] < ls[j]:
            ls[i],ls[j] = ls[j],ls[i]
        else:
            continue

print(*ls)