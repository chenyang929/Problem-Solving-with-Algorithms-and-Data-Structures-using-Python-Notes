# hot_potato.py

from my_queue import Queue


def hot_potato(name_lst, num):
    q = Queue()
    for n in name_lst:
        q.enqueue(n)

    while q.size() > 1:
        for i in range(num):
            q.enqueue(q.dequeue())
        q.dequeue()

    return q.dequeue()


if __name__ == '__main__':
    print(hot_potato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7))
