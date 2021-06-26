class Stack :
    def __init__(self) -> None:
        self.stack = []


    def push(self,data):
        self.stack.append(data)

    def pop(self):
        return self.stack.pop()

    def isEmpty(self):
        if len(self.stack)==0:
            return True
        else:
            return False
    def peek(self):
        return self.stack[-1]

if __name__ == '__main__':
    stack = Stack()
    stack.push('1')
    stack.push('2')
    stack.push('3')
    stack.push('4')
    stack.push('5')
    stack.push('6')
    print(stack.peek())
    # print(stack.pop())
    # print(stack.pop())
    # print(stack.pop())
    # print(stack.pop())
    # print(stack.pop())
    # print(stack.pop())
    print(stack.isEmpty)