# bubble_sort.py

def bubble_sort(lst):
    for num in range(len(lst)-1, 0, -1): # 每一轮找出最大值排到后边
        for i in range(num):
            if lst[i] > lst[i+1]:
                temp = lst[i+1]
                lst[i+1] = lst[i]
                lst[i] = temp
    return lst

# 优化版，一旦检测到已经排好序就跳出循环
def short_bubble_sort(lst):
    num = len(lst) - 1
    sorted = False
    while num >= 0 and not sorted:
        sorted = True
        for i in range(num):
            if lst[i] > lst[i+1]:
                sorted = False
                temp = lst[i+1]
                lst[i+1] = lst[i]
                lst[i] = temp
        num -= 1
    return lst


if __name__ == '__main__':
    l = [23, 18, 40, 9, 52, 66, 37, 99, 87]
    print(bubble_sort(l))
    print(short_bubble_sort(l))
    


