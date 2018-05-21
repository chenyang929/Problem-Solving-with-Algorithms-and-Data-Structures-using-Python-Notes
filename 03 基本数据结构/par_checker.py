# par_checker.py

from stack import Stack


def par_checker(symbol_str):
    sk = Stack()
    balanced = True
    for symbol in symbol_str:
        if symbol in '([{':
            sk.push(symbol)
        elif symbol in ')]}':
            if sk.empty():
                balanced = False
                break
            top = sk.pop()
            if not matches(top, symbol):
                balanced = False
    if sk.empty() and balanced:
        print('match')
    else:
        print('no match')


def matches(start, end):
    starts = "([{"
    ends = ")]}"
    return starts.index(start) == ends.index(end)


if __name__ == '__main__':
    par_checker('{{([][])}()}')
    par_checker('[{()]')
    par_checker('[{()}])')


