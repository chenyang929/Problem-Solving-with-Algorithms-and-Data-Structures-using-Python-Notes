# order_list.py
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
        current = self.head
        previous = None
        stop = False
        while current and not stop:
            if current.get_data() > item:
                stop = True
            else:
                previous = current
                current = current.get_next()
        node = Node(item)
        if not previous:
            node.set_next(self.head)
            self.head = node
        else:
            node.set_next(current)
            previous.set_next(node)

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
            elif current.get_data() > item:
                break
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
