import ctypes

class Stack:
    def __init__(self):
        self.count = 0
        self.capacity = 1
        self.array = (self.make_an_array(self.capacity))

    def make_an_array(self, new_capacity):
        return(new_capacity * ctypes.py_object)()

    def resize(self):
        new_capacity = self.capacity * 2
        B = self.make_an_array(new_capacity)
        for i in range(self.count):
            B[i] = self.array[i]
        self.array = B
        self.capacity = new_capacity

    def len(self):
        return self.count

    def push(self, a):
        b = self.len()
        if b == self.capacity:
            self.resize()
        self.array[b] = a
        self.count += 1

    def print_out(self):
        for i in range(self.count):
            print self.array[i]

    def pop(self):
        b = [0] * (self.count - 1)
        for i in range(self.count - 1):
            b[i] = self.array[i]
        self.array = b
        self.count -= 1
        if self.len() == self.capacity/2:
            self.capacity = self.capacity/2

    def peek(self):
        k = self.array[0]
        for i in range(1, self.count):
            if self.array[i] > self.array[i-1]:
                k = self.array[i]
        return k






