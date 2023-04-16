
class Queue:
    #initialization queue
    def __init__(self, capacity = None):
        self.items = []
        if capacity == None:
            self.capacity = 100
        else:
            self.capacity = capacity
    
    #check empty
    def isEmpty(self):
        return self.items == []

    #add tail in queue
    def enQueue(self, value):
        if len(self.items) > self.capacity:
            print("Queue is full. Overflow condition!")
        else:
            self.items.append(value)
    
    #remove head in queue
    def deQueue(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            ele = self.items[0]
            del self.items[0]
            return ele
    
    #length queue
    def size(self):
        return len(self.items)

#Double-ended queue(Hàng đợi 2 đầu)    
class doubleQueue(Queue):

    #Add tail in queue
    def insertAtTail(self, value):
        if len(self.items) >= (self.capacity):
            print("Queue is full. Overflow condition!")
        else:
            self.items.append(value)
    
    #delete tail in queue
    def deleteFromTail(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            elem = self.items[len(self.items)-1]
            del self.items[len(self.items)-1]
            return elem
    
    #insert head in queue
    def insertAtHead(self, value):
        if len(self.items) > self.capacity:
            #print("Queue is full. Overflow condition!")
            del self.items[len(self.items)-1]
        self.items.insert(0,value)
    
    #delete head in queue
    def deleteFromHead(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            elem = self.items[0]
            del self.items[0]
            return elem

    #Get head in queue
    def getHead(self):
        return self.items[0]
    
    #get tail in queue
    def getTail(self):
        return self.items[len(self.items)-1]
    


q=Queue()
q.enQueue(4)
q.enQueue('dog')
q.enQueue(True)
print(q.size())
print(q.deQueue())
print(q.deQueue())
print(q.deQueue())
print(q.isEmpty())
