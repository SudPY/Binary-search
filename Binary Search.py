print("This is binary search")
def binarysearch(arr, start, end, x):
    if end >= start:
        mid = start + (end - start)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binarysearch(arr, start, mid-1, x)
        else:
            return binarysearch(arr, mid+1, end, x)
    else:
        return - 1

arr = sorted(['1', '2', '3'])
x = input("Enter the element to search : ")
result = binarysearch(arr, 0, len(arr)-1, x)
if result != -1:
    print("Element is present at index : "+str(result))
else:
    print("Element is not present in array")
