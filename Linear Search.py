print("This is linear search")

def linearsearch(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

arr = ['a', 'b', 'c', 'd', 'e', '1', '2', '3', '4', '5']
x = input("Enter the element to search : ")
print("element found at index : " +str(linearsearch(arr, x)))
