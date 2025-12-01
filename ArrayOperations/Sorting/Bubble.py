#Bubble Sort : compares side by side elements and shfit them ,Time complexity O(n^2)
ls = list(map(int,input("Enter the Elements: ").split()))

for i in range(len(ls)):
    for j in range(len(ls)-1-i):
        if ls[j] > ls[j+1]:
            ls[j],ls[j+1] = ls[j+1],ls[j]
        else:
            continue

print(*ls)