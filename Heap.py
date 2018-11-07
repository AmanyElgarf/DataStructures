#max heap
import ctypes
class Heap:
    def __init__(self, d):
        self.d = d #no of children
        self.capacity = 1
        self.size = 0
        self.arr = self.make_an_array(self.capacity)

    def make_an_array(self, new_capacity):
        return (ctypes.py_object * new_capacity)()

    def resize(self):
        new_capacity = (self.capacity * 2)
        b = self.make_an_array(new_capacity)
        for i in range(self.size):
            b[i] = self.arr[i]
        self.arr = b
        self.capacity = new_capacity

    def append(self, a):
        if self.size == self.capacity:
            self.resize()
        self.arr[self.size] = a
        self.size += 1

    def get_index(self, a):
        for i in range(self.size):
            if self.arr[i] == a:
                break
        return i

    def swim(self, a, size):
        if size > 1:
            d = self.d
            cIndex = self.get_index(a)
            pIndex1= abs((cIndex+1-2+d))/d
            pIndex = pIndex1 - 1
            p = self.arr[pIndex]
            if a > p:
                self.arr[cIndex], self.arr[pIndex] = self.arr[pIndex], self.arr[cIndex]
                self.swim(a, pIndex1)

    def insert(self, a):
        self.append(a)
        self.swim(a, self.size)

    def display(self):
        print "Heap is"
        for i in range(self.size):
            print self.arr[i]

    def parent_has_childre(self, parent, size):
        d = self.d
        pIndex1 = self.get_index(parent) + 1
        cIndex1 = (pIndex1 - 1) * d + 2
        if cIndex1 <= size:
            return True
        else:
            return False

    def sink(self, parent, size):
        d = self.d
        pIndex = self.get_index(parent)
        while self.parent_has_childre(parent, size):
            pIndex1 = self.get_index(parent) + 1
            cIndex1 = (pIndex1 - 1) * d + 2
            cIndex = cIndex1 - 1
            c = self.arr[cIndex]
            maxC = c
            for j in range(1, d):
                nCIndex1 = (pIndex1 - 1) * d + j + 2
                nCIndex = nCIndex1 - 1
                nC = self.arr[nCIndex]
                if nC > c and nCIndex1 <= size:
                    maxC = nC
                c = nC
            if parent < maxC:
                self.arr[self.get_index(maxC)], self.arr[pIndex] = self.arr[pIndex], self.arr[self.get_index(maxC)]
                pIndex = self.get_index(parent)
            size = size - pIndex - 1

    def heap_sort(self):
        size = self.size
        while size > 1:
            max_index = 0
            lele_index = size - 1
            self.arr[max_index], self.arr[lele_index] = self.arr[lele_index], self.arr[max_index]
            size -= 1
            self.sink(self.arr[max_index], size)






object = Heap(2)
object.insert(3)
object.insert(11)
object.insert(4)
object.insert(5)
object.insert(10)
object.insert(1)
object.insert(55)
object.insert(7)

#object.display()

object.heap_sort()
object.display()





