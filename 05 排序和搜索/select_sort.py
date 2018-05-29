# select_sort.py

def select_sort(lst):
    for num in range(len(lst)-1, 0, -1):
        max_index = 0
        for i in range(1, num+1):   # 注意这里是1到num+1
            if lst[i] > lst[max_index]:
                max_index = i

        temp = lst[num]
        lst[num] = lst[max_index]
        lst[max_index] = temp
    return lst


if __name__ == '__main__':
    l = [23, 18, 40, 9, 52, 66, 37, 99, 87]
    print(select_sort(l))


