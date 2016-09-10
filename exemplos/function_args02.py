def func(a, b=4, c=42):
    print(a, b, c)

if __name__ == '__main__':
    func(1)
    func(b=5, a=7, c=9)
    func(40, c=9)
