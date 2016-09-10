def divide(n, d):
    try:
        result = n / d
    except ZeroDivisionError as zde:
        print(zde)
    else:
        print('O resultado é:', result)
        return result

if __name__ == '__main__':
    n = int(input('Digite um numerador:'))
    d = int(input('Digite um denominador:'))
    divide(n, d)
