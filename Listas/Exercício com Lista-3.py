# Crie um programa que leia vários números em uma lista (não perguntar quantidade). Mostre:
# Quantos valores foram digitados
# A lista de valores em ordem decrescente
# Se o valor "5" foi digitado

from random import randint

lista = []
listagem = []
while True:
        num = int(input('Digite um número: '))
        lista.append(num)
        if num ==  0:
             break   
if 5 in lista:
    print('O número 5 aparece!!')
else:
    print('O número 5 não foi digitado.')
      

print(f'Há {len(lista)} índices na lista')
print(f'Ordem decrescente: {lista[::-1]}')
