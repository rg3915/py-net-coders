from mycapitalize import _capitalize

palavras = 'joaquim josé da silva xavier'
nome = []

for palavra in palavras.split():
    print(_capitalize(palavra))
    nome.append(_capitalize(palavra))

print(' '.join(nome))
