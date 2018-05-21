# stack.py


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


if __name__ == '__main__':
    s = Stack()

    print(s.empty())
    s.push(4)
    s.push('dog')
    print(s.peek())
    s.push(True)
    print(s.size())
    print(s.empty())
    s.push(8.4)
    print(s.pop())
    print(s.pop())
    print(s.size())
