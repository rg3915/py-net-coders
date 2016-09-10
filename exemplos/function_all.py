def func(a, b, c=7, *args, **kwargs):
    print('a, b, c:', a, b, c)
    print('args:', args)
    for i in args:
        print(i)
    print('kwargs:', kwargs)
    for k in kwargs:
        print(k, kwargs[k])

if __name__ == '__main__':
    func(1, 2, 3, *(5, 7, 9), **{'A': 'a', 'B': 'b'})
