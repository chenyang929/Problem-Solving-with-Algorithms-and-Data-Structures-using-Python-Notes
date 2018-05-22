# pal_checker.py

from my_deque import Deque


def pal_checker(pal_str):
    dq = Deque()
    for s in pal_str:
        dq.add_front(s)

    equal = True
    while dq.size() > 1 and equal:
        front = dq.remove_front()
        rear = dq.remove_rear()
        if front != rear:
            equal = False
    return equal


if __name__ == '__main__':
    print(pal_checker('radar'))
    print(pal_checker('rader'))
    print(pal_checker('toot'))