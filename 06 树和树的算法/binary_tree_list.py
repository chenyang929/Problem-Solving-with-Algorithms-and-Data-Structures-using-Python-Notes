# binary_tree_list.py

def binary_tree(r):
    return [r, [], []]

def insert_left(root, branch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1, [branch, t, []])
    else:
        root.insert(1, [branch, [], []])
    return root

def insert_right(root, branch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [branch, [], t])
    else:
        root.insert(2, [branch, [], []])
    return root

def get_root_val(root):
    return root[0]

def set_root_val(root, val):
    root[0] = val

def get_left_child(root):
    return root[1]

def get_right_child(root):
    return root[2]


if __name__ == '__main__':
    tr = binary_tree(3)
    insert_left(tr, 4)
    insert_right(tr,5)
    insert_left(tr, 6)
    insert_right(tr, 7)
    insert_right(tr, 8)
    print(tr)

    l = get_right_child(tr)
    print(l)
    set_root_val(l, 9)
    print(get_right_child(tr))



