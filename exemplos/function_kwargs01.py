def func(**kwargs):
    print('Keywords:', kwargs)

if __name__ == '__main__':
    func(a=1, b=42)
    dic = {'a': 1, 'b': 42}
    func(**dic)
