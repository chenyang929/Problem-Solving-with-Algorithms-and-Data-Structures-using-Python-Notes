# hash_table.py

class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, data):
        hash_value = self.hash_func(key)
        if self.slots[hash_value] is None:
            self.slots[hash_value] = key
            self.data[hash_value] = data
        else:
            if self.slots[hash_value] == key:
                self.data[hash_value] = data
            else:
                next_slot = self.re_hash_func(key)
                while self.slots[next_slot] and self.slots[next_slot] != key:
                    next_slot = self.re_hash_func(next_slot)
                if self.slots[next_slot] is None:
                    self.slots[next_slot] = key
                    self.data[next_slot] = data
                else:
                    self.data[next_slot] = data

    def get(self, key):
        data = None
        hash_value = self.hash_func(key)
        if self.slots[hash_value] == key:
            data = self.data[hash_value]
        else:
            next_solt = self.re_hash_func(key)
            while self.slots[next_solt] and self.slots[next_solt] != key:
                next_solt = self.re_hash_func(next_solt)
            if self.slots[next_solt] == key:
                data = self.data[next_solt]
        return data

    def hash_func(self, key):
        return key % self.size

    def re_hash_func(self, key):
        return (key + 1) % self.size

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)

if __name__ == '__main__':
    H=HashTable()
    H[54]="cat"
    H[26]="dog"
    H[93]="lion"
    H[17]="tiger"
    H[77]="bird"
    H[31]="cow"
    H[44]="goat"
    H[55]="pig"
    H[20]="chicken"
    print(H.slots)
    print(H.data)
    print(H[20])
    print(H[17])
    H[20] = 'duck'
    print(H[20])
    print(H.data)
    print(H[99])
    