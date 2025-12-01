#Selection sort : this algo will select the smallest number from unsorted part 
#and add to sorted part

#key Observations : we just stored the index of smallest element from the unsorted part

ls = list(map(int,input("Enter Elements: ").split()))

sortt = -1
mini = 0

for i in range(len(ls)-1):
    mini = i
    for j in range(i+1,len(ls)):
        if ls[mini] > ls[j]:
            mini = j          
        else:
            continue
    ls[i],ls[mini] = ls[mini],ls[i]

print(*ls)