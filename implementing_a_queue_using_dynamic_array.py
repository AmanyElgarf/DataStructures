import ctypes

class Queue:
    def __init__(self):
        self.count = 0
        self.capacity = 1
        self.array = self.make_an_array(self.capacity)

    def make_an_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    def resize(self, new_capacity):
        b = self.make_an_array(new_capacity)
        for i in range(self.count):
            b[i] = self.array[i]
        self.array = b
        self.capacity = new_capacity

    def enqueue(self, a):
        if self.capacity == self.size():
            self.resize(self.capacity*2)
        self.array[self.count] = a
        self.count += 1

    def dequeue(self):
        dequeued = self.array[0]
        b = [0] * (self.count - 1)
        for i in range(self.count-1):
            b[i] = self.array[i + 1]
        self.array = b
        self.count -= 1
        if (self.capacity/2) == self.count:
            self.capacity = self.capacity/2
        return dequeued

    def traverse(self, index):
        return self.array[index]

    def size(self):
        return self.count

    def display(self):
        for i in range(self.count):
            print self.array[i]

