#This is the most effeicent search mechanism 
#but works only when there is sorted and the average between the elements are same

lis = list(map(int,input("Enter Elements: ").split()))
target = int(input("Enter your Target Value: "))
low = 0
high = len(lis)-1

pos = low + (target - lis[low])*(high - low)//(lis[high]-lis[low])
print(pos)

if lis[pos] == target:
    print(f"Target {target} Found at index {pos}")
else:
    print("Position does not have the element.")
    