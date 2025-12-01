#Linear search : searching elements one by one takes 0(n) time complexity
lis = list(map(int,input("Enter the elements : ").split()))
n = int(input("Enter the element: "))

for i in range(len(lis)):
    if n == lis[i]:
        print(f"Element {n} is at {i} index")
        break
    else:
        if i == len(lis)-1:
            print("Element is not there in the Array")
        else:
            continue