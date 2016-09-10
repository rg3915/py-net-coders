def func(*args):
    print('Positional:', args)

if __name__ == '__main__':
    lista = [-1, 100, 0, 2, 3, 4]
    func(lista)
    func(*lista)
