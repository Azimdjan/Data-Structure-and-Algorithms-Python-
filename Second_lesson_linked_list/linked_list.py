class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next
    
    def push(self,data):
        if(self.head==None):
            self.head = Node(data)
            print('Data was added!')
            return
        temp = Node(data)
        temp.next = self.head
        self.head = temp
        print('Data was added!')
    
    def pushAtIndex(self,index,data):
        temp = self.head
        if(index < 0 or data==None):
            print('Please enter correctly!')
            return

        if(temp==None):
            self.head = Node(data)
            return

        indexRange = range(index-1)
        if(indexRange==-1):
            node = Node(data)
            node.next = temp
            self.head = node
            return
        elif indexRange==0:
            node = Node(data)
            node.next = temp.next
            self.head.next = node
            return

        for i in indexRange:
            temp = temp.next
        previousNode = temp
        nextNode = temp.next
        newNode = Node(data)
        newNode.next = nextNode
        previousNode.next = newNode
    
    def deleteAtIndex(self,index):
        temp = self.head
        ## At first index
        if index==0:
            self.head = temp.next
            temp = None
            return

        for i in range(index):
            if i==0:
                continue    
            temp = temp.next
        prevNode = temp
        temp = temp.next
        prevNode.next = temp.next
        temp = None
    
    def deleteKey(self,data):
        temp = self.head
        if not temp : 
            return
        if temp.data == data:
            self.head = temp.next
            temp = None
            return
        while temp.data != data:
            prevNode = temp
            temp = temp.next
            if(temp==None):
                return
        if temp == None:
            return
        prevNode.next = temp.next
        temp = None

            

        


if __name__ == "__main__" :
    linkedList = LinkedList()
    linkedList.pushAtIndex(0,"Yakshanba")
    linkedList.pushAtIndex(1,"Shanba")
    linkedList.pushAtIndex(1,"Shanba kechasi")
    linkedList.pushAtIndex(2,"Juma")
    linkedList.printList()
    linkedList.deleteKey('das')
    linkedList.pushAtIndex(5,'data')
    print()
    linkedList.printList()