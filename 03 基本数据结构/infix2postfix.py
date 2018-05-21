# infix2postfix.py

from stack import Stack


def infix2postfix(infix):
    sk = Stack()
    postfix_lst = []
    infix_lst = infix.split()
    pre = dict()
    pre['*'] = 3
    pre['/'] = 3
    pre['+'] = 2
    pre['-'] = 2
    pre['('] = 1
    words = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    for ix in infix_lst:
        if ix in words:
            postfix_lst.append(ix)
        elif ix == '(':
            sk.push(ix)
        elif ix == ')':
            top = sk.pop()
            while top != '(':
                postfix_lst.append(top)
                top = sk.pop()
        elif ix in '+-*/':
            while not sk.empty() and pre[ix] <= pre[sk.peek()]:
                postfix_lst.append(sk.pop())
            sk.push(ix)

    while not sk.empty():
        postfix_lst.append(sk.pop())
    return ' '.join(postfix_lst)


if __name__ == '__main__':
    print(infix2postfix('A * B + C * D'))
    print(infix2postfix('( A + B ) * C - ( D - E ) * ( F + G )'))


