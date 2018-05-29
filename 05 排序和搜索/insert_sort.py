# insert_sort.py

def insert_sort(lst):
    for index in range(1, len(lst)):
        position = index
        current_value = lst[index]

        while position > 0 and lst[position-1] > current_value:
            lst[position] = lst[position-1]
            position -= 1
        
        lst[position] = current_value

    return lst


if __name__ == '__main__':
    l = [23, 18, 40, 9, 52, 66, 37, 99, 87]
    print(insert_sort(l))
        
        