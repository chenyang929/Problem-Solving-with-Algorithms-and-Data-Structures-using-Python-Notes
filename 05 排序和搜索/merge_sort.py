# merge_sort.py

def merge_sort(lst):
    if len(lst) == 1:
        return lst
    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]
    l1 = merge_sort(left)
    r1 = merge_sort(right)

    return merge(l1, r1)


def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        for i in range(len(left)):
            if left[0] <= right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
    result += left
    result += right
    return result

if __name__ == '__main__':
    l = [23, 18, 40, 9, 52, 66, 37, 99, 87]
    print(merge_sort(l))