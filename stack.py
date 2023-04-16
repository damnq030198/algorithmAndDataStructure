class Stack:
    #initialization stack
    def __init__(self):
        self.items = []
        self.capacity = 100
    
    #The stack check empty 
    def isEmpty(self):
        self.items == []
    
    # the stack check full 
    def isFull(self):
        return (self.capacity -1) <= len(self.items)

    #add element in stack 
    def push(self,value):
        if self.isFull() == True:
            print("Stack is full. Overflow condition!")
        else:
            self.items.append(value)

    #get element in stack
    def pop(self):
        if self.isEmpty() == True:
            print("Stack is empty. Underflow condition!")
        else:
            elem = self.items[len(self.items)-1]
            del self.items[len(self.items)-1]
            return elem
            
    
    #get top element in stack
    def top(self):
        return self.items[0]
    
    #get size
    def size(self):
        return len(self.items)

    #display stack
    def displayStack(self):
        for i in range(len(self.items)):
            print(self.items[i])
    
s = Stack()
print(s.isEmpty())
s.push(4)
s.push('dog')
print(s.top())
s.push(True)
print(s.size())
print(s.isEmpty())
s.push(8.4)
print(s.pop())
print(s.pop())
print(s.size())
s.displayStack()
print(s.isFull())

