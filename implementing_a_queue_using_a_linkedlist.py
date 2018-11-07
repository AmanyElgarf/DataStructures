class Node:
    def __init__(self, data):
        self.data = data
        self.Next = None


class Queue:
    def __init__(self):
        self.count = 0
        self.head = None

    def enqueue(self, a):
        if self.head is None:
            self.head = Node(a)
        else:
            new_node = Node(a)
            current = self.head
            while current.Next:
                current = current.Next
            current.Next = new_node
        self.count += 1

    def display(self):
        current = self.head
        while current:
            print current.data
            current = current.Next

    def dequeue(self):
        if self.head is None:
            return None
        else:
            dequeued = self.head.data
            self.head = self.head.Next
            self.count -= 1
            return dequeued

    def size(self):
        return self.count
