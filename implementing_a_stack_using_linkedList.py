class Node:
    def __init__(self, data):
        self.data = data
        self.Next = None

class Stack:
    def __init__(self):
        self.count = 0
        self.head = None

    def push(self, a):
        b = Node(a)
        if self.head is None:
            self.head = b
        else:
            b.Next = self.head
            self.head = b
        self.count += 1

    def print_out(self):
        current = self.head
        while current:
            print current.data
            current = current.Next

    def pop(self):
        if self.head is None:
            return None
        else:
            popped = self.head.data
            self.head = self.head.Next
            self.count -= 1
            return popped

    def size(self):
        return self.count

    def peak(self):
        max = self.head.data
        current = self.head
        while current.Next:
            if current.Next.data > max:
                max = current.Next.data
            current = current.Next
        return max

