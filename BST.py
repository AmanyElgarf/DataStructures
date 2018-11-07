class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.size = 0
        self.root = None

    def size(self):
        return self.size

    def insert(self, a):
        b = Node(a)
        if self.root is None:
            self.root = b
        else:
            self._insert(b, self.root)
        self.size += 1

    def _insert(self, node, parent):
        if node.data < parent.data:
            if parent.left is None:
                parent.left = node
            else:
                self._insert(node, parent.left)
        else:
            if parent.right is None:
                parent.right = node
            else:
                self._insert(node, parent.right)

    def search(self, a):
        if self.root is None:
            return "Tree is Empty"
        if self.root.data == a:
            return self.root.data
        else:
            self._search(a, self.root)

    def _search(self, a, root):
        if (a > root.data and root.right is None) or (a < root.data and root.left is None):
            return "Not found"
        elif a > root.data:
            if root.right.data == a:
                return root.right.data
            else:
                self._search(a, root.right)
        else:
            if root.left.data == a:
                return root.left.data
            else:
                self._search(a, root.left)





    def display(self):
        print self.root.data
        print self.root.left.data
        print self.root.right.data
        print self.root.right.right.data



object = BST()
object.insert(4)
object.insert(3)
object.insert(5)
object.insert(8)
object.display()
print " "
print object.search(8)
print object.size

