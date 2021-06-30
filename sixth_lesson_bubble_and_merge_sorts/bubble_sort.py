def bubleSort(myList):
    for i in range(len(myList)):
        for j in range(len(myList)-i-1):
            if myList[j]>myList[j+1]:
                ##swap(myList[j],myList[j+1])
                myList[j],myList[j+1] = myList[j+1],myList[j]

if __name__ == '__main__':
    myList = [23,32,21,11,22,333,211,31,122,31,12,54,3]
    bubleSort(myList)
    print(myList)