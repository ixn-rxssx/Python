from random import randint

lista = []
positivo = []
zero = []
negativo = []

for i in range(50):
    num = randint(-20, 20)
    lista.append(num)

for  item in lista:
    if item < 0:
        negativo.append(item)
    elif item == 0:
        zero.append(item)
    elif item > 0:
        positivo.append(item)

print(f'Valores da lista: {lista} ')
print(f'Números positivos: {positivo}')
print(f'Contagem de números zeros: {len(zero)}')
print(f'Números negativos: {negativo}')