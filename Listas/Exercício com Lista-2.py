# Faça um programa que gere um vetor de números aleatórios. Após a geração peça ao
# usuário um valor inteiro a pesquisar. Percorra o vetor gerado e mostre o número de
# corrências do valor digitado pelo usuário. 

from random import randint

num = []
cont = 0

for i in range(50):
    aleatorio = randint(1,10)
    num.append(aleatorio)

pesquisa = int(input('Pesquise por um número de 1 á 10:'))

for n in num:
    if pesquisa == n:
        cont += 1
print(f'Vezes que o número {pesquisa} apareceu: {cont} ')
print(num)