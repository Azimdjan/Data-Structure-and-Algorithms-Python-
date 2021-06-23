def linearSearchUsingWhile(myList,num):
    i = 0
    while True:
        if(myList[i]==num):
            return i
        if(len(myList)-1==i):
            return 'None'
        i+=1

def linearSearchUsingFor(myList,num):
    for n in range(len(myList)):
        if(myList[n] == num):
            return n
    return 'None'


if __name__ == '__main__':
    myList = [1,3,4,6,8,9,15,12,65,98,45,12,32,15]
    print('At index '+str(linearSearchUsingWhile(myList,10)))
    print('At index '+str(linearSearchUsingFor(myList,15)))

