# binary_tree_class.py

class BinaryTree:
    def __init__(self, root):
        self.root = root
        self.left = None
        self.right = None

    def add_left(self, branch):
        b = BinaryTree(branch)
        if not self.left:
            self.left = b
        else:
            b.left = self.left
            self.left = b

    def add_right(self, branch):
        b = BinaryTree(branch)
        if not self.right:
            self.right = b
        else:
            b.right = self.right
            self.right = b
        
    def get_root_val(self):
        return self.root

    def set_root_val(self, val):
        self.root = val

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right
    
    def __str__(self):
        return '<root: {}, left: {}, right: {}>'.format(self.root, self.left, self.right)


if __name__ == '__main__':
    tr = BinaryTree('a')
    tr.add_left('b')
    tr.add_right('c')
    print(tr)
    tr.add_left('e')
    l = tr.get_left()
    print(l)
    l.set_root_val('f')
    print(l)