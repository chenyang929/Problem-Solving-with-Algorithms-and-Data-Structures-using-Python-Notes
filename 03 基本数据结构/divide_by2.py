# divide_by2.py

from stack import Stack


def divide_by2(decnumber):
    sk = Stack()
    while decnumber > 0:
        decnumber, rem = divmod(decnumber, 2)
        sk.push(rem)

    bin_str = ''
    while not sk.empty():
        bin_str += str(sk.pop())
    return bin_str


if __name__ == '__main__':
    print(divide_by2(233))