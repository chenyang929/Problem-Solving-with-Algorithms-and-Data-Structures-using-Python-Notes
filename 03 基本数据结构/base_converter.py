# base_converter.py

from stack import Stack


def base_converter(decnumber, base):
    sk = Stack()
    while decnumber > 0:
        decnumber, rem = divmod(decnumber, base)
        sk.push(rem)

    bin_str = ''
    digits = '0123456789ABCDEF'
    while not sk.empty():
        bin_str += digits[sk.pop()]
    return bin_str


if __name__ == '__main__':
    print(base_converter(233, 2))
    print(base_converter(233, 8))
    print(base_converter(233, 10))
    print(base_converter(233, 16))
