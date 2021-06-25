def selectionSort(myList):
    length = len(myList)
    for i in range(length):
        max = myList[0]
        index = 0
        for n in range(length):
            if(max < myList[n]):
                max = myList[n]
                index = n
        temp = myList[length-1]
        myList[length-1] = max
        myList[index] = temp
        length=length-1    

if __name__ == '__main__':
    myList = [23,423,12,34,56,35,1,3,63,34,23]
    print('sorted')
    selectionSort(myList)
    print(myList)