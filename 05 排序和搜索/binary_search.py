# binary_search.py

# 循环版
def binary_search(lst, item):
    low = 0
    high = len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = lst[mid]
        if item == guess:
            return mid
        elif item > guess:
            low += 1
        else:
            high -= 1
    return -1

# 递归版（内存开销大）
def binary_search1(lst, item, low=0, high=None):
    if high is None:
        high = len(lst) - 1
    if low > high:
        return -1
    else:
        mid = (low + high) // 2
        guess = lst[mid]
        if item == guess:
            return mid
        elif item > guess:
            low += 1
            return binary_search1(lst, item, low, high)
        else:
            high -= 1
            return binary_search1(lst, item, low, high)


if __name__ == '__main__':
    l = [1, 3, 4, 7, 9, 12, 14]
    print(binary_search(l, 12)) # 5
    print(binary_search1(l, 12)) # 5
    print(binary_search(l, 5)) # -1
    print(binary_search1(l, 5)) # -1

        
