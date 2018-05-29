# to_str.py

def to_str(n, base):
    cover_str = '0123456789ABCDEF'
    if n < base:
        return cover_str[n]
    else:
        return to_str(n//base, base) + cover_str[n%base]
    

if __name__ == '__main__':
    print(to_str(20, 8))
    print(to_str(10 ,2))
