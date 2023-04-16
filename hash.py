class hashFunction:
    def __init__(self, size = None):
        if size == None:
            self.size = 10000
        else:
            self.size = size
        self.hashTable = [None]*self.size


    def totalStrings(self, string):
        total = 0
        for i in string:
            total += ord(i)
        return total

