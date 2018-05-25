# unorder_list.py
# 节点
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def set_data(self, new_data):
        self.data = new_data

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next


# 无序列表（链表）
class UnorderList:
    def __init__(self):
        self.head = None

    def empty(self):
        return self.head is None
    
    def add(self, item):
        node = Node(item)
        node.set_next(self.head)
        self.head = node

    def append(self, item):
        current = self.head
        if not current:
            self.add(item)
        else:
            while current.get_next():
                current = current.get_next()
            current.set_next(Node(item))

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count

    def search(self, item):
        current = self.head
        found = False
        while current and not found:
            if current.get_data() == item:
                found = True
            current = current.get_next()
        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while current and not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()
        if found:
            if not previous:
                self.head = current.get_next()
            else:
                previous.set_next(current.get_next())


if __name__ == '__main__':
    my_list = UnorderList()
    my_list.add(2)
    my_list.add(4)
    my_list.add(7)
    print(my_list.size())
    print(my_list.search(3))
    my_list.remove(5)
    print(my_list.size())
    my_list.remove(4)
    print(my_list.size())
    my_list.append(8)
    print(my_list.size())



