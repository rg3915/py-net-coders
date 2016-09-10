# python -m doctest minimum.py
'''
>>> minimum(1, 3, -7, 9)
-7
'''


def minimum(*n):
    if n:
        mn = n[0]
        for value in n[1:]:
            if value < mn:
                mn = value
        return mn

if __name__ == '__main__':
    lista = [1, 3, -7, 9]
    print(minimum(*lista))
