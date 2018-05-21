# postfix_eval.py

from stack import Stack


def postfix_eval(postfix):
    sk = Stack()
    postfix_lst = postfix.split()
    for px in postfix_lst:
        if px.isdigit():
            sk.push(int(px))
        elif px in '+-*/':
            second = sk.pop()
            first = sk.pop()
            sk.push(do_math(px, first, second))
    return sk.pop()


def do_math(symbol, fst, sec):
    if symbol == '+':
        result = fst + sec
    elif symbol == '-':
        result = fst - sec
    elif symbol == '*':
        result = fst * sec
    else:
        result = fst / sec
    return result


if __name__ == '__main__':
    print(postfix_eval('2 3 5 * +'))
    print(postfix_eval('2 3 + 5 1 - *'))
