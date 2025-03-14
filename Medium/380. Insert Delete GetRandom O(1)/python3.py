import random

class RandomizedSet:
    def __init__(self):
        self.list = []
        self.map = {}

    def search(self, val):
        return val in self.map

    def insert(self, val):
        if self.search(val):
            return False
        self.list.append(val)
        self.map[val] = len(self.list) - 1
        return True

    def remove(self, val):
        if not self.search(val):
            return False
        
        index = self.map[val]
        self.list[index] = self.list[-1]
        self.map[self.list[index]] = index
        self.list.pop()
        del self.map[val]
        
        return True

    def getRandom(self):
        return random.choice(self.list)
