#Binary search used in sorted data, It takes o(log(n)) time complexity.
def binary(front,rear):
    while front <= rear:
        mid = ((front+rear)//2)
        if list1[mid] == n:
            print(f"Element {n} is at index {mid}.")
            return
        elif n < list1[mid]:
            rear = mid-1
        elif n > list1[mid]:
            front = mid+1
    return -1    

list1 = list(map(int,input("Enter the Elements : ").split()))
n = int(input("Enter the Number you Want: "))
front = 0
rear = len(list1)-1

result = binary(front,rear)

if result == -1:
    print("Does not there in array")
else:
    print(result)