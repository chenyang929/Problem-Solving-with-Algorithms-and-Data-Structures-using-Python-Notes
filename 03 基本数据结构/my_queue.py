# my_queue.py
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


if __name__ == '__main__':
    q = Queue()
    print(q.empty())

    q.enqueue(4)
    q.enqueue('dog')
    q.enqueue(True)

    print(q.size())
    print(q.empty())

    q.enqueue(8.4)

    print(q.dequeue())
    print(q.dequeue())

    print(q.size())