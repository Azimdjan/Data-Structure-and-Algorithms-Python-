def binarySearchUsingWhile(myList, num):
    L = 0
    H = len(myList)-1
    while(L<=H):
        m = (L+H)//2
        if(myList[m] == num):
            return m
        elif (myList[m] > num):
            H = m - 1
        else:
            L = m + 1
    return 'Not found!'




if __name__ == '__main__':
    myList = [1,3,4,6,8,9,15,17,65,98,100,120,132,150]
    print("At index "+str(binarySearchUsingWhile(myList,120)))