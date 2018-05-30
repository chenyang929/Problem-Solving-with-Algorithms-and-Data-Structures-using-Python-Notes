# quick_sort.py

def quick_sort(lst):
    if len(lst) < 2:
        return lst
    pivot = lst[0]
    smaller = [item for item in lst[1:] if item < pivot]
    bigger = [item for item in lst[1:] if item > pivot]
    return quick_sort(smaller) + [pivot] + quick_sort(bigger)


if __name__ == '__main__':
    l = l = [23, 18, 40, 9, 52, 66, 37, 99, 87]
    print(quick_sort(l))