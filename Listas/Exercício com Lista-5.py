# Faça uma lista que pergunte ao usuário um número inteiro.
# Caso o número já exista, não adicione na lista. Ao final exibir todos em ordem crescente

lista = []

while True:
    num = int(input('Adicione um número: '))
    if num == 0:
        break
    elif num in lista:
        print('Já consta esse número na lista, tente outro')
    else:
        lista.append(num)
for cont in lista:
    print(cont)