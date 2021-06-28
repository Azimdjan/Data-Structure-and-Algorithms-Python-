from random import randrange
def gcdWithDivision(num1,num2):
    if num1 < num2:
        num1,num2 = num2,num1
    while(num1%num2!=0):
        num1,num2 = num2,num1%num2
    return num2

def gcdWithRecursion(num1,num2):
    if(num1<num2):
        num1,num2 = num2,num1
    if(num2==0):
        return num1
    else:
        return gcdWithRecursion(num2,num1%num2)

def findSum(array):
    if array == []:
        return 0
    return array[0]+findSum(array[1:])

def arrLen(arr):
    if arr == []:
        return 0
    return 1+arrLen(arr[1:])

def findBig(arr):
    if(arr == []):
        return max
    return findBig(arr[1:])

def binarySearch(arr,num,start=0,end=None):
    if(arr == [] or num==None):
        return 'Please enter correctly'
    if end is None:
        end = len(arr)-1
    mid = (start + end)//2
    if(arr[mid] == num):
        return 'Found at index '+str(mid)
    elif arr[mid] > num:
        return binarySearch(arr,num,start,mid-1)
    else:
        return binarySearch(arr,num,mid+1,end)

def quickSort(arr):
    if len(arr)<2:
        return arr
    pivot = arr.pop(randrange(len(arr)))
    less = [i for i in arr if i<=pivot]
    bigger = [i for i in arr if i>pivot]
    return quickSort(less) + [pivot] + quickSort(bigger)

if __name__ == '__main__':
    myList = [15,20,13,14,155,60,70,48,39]
    print(quickSort(myList))
    print(binarySearch(quickSort(myList),60))