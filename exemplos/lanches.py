import sys
from random import choice

lanches = ['Hot-Dog', 'X-Salada', 'Tapioca', 'Pizza', 'Batata Frita']
bebidas = ['Coca-Cola', 'Fanta', 'Guaraná', 'Suco de Laranja', 'Cerveja']
numero = input('Digite um número de 0 a 4: ')


if int(numero) > 4:
    print('O número digitado está fora do intervalo.')
    # Experimente digitar -5 e -6
    sys.exit(1)


def bebida():
    return choice(bebidas)


for i in range(3):
    if i == 0:
        print('Primeira refeição: %s + %s' % (lanches[int(numero)], bebida()))
    elif i == 1:
        print('Segunda refeição: %s + %s' % (lanches[int(numero)], bebida()))
    else:
        print('Terceira refeição: %s + %s' % (lanches[int(numero)], bebida()))
