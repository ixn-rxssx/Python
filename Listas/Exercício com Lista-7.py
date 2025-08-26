#  Faça um programa que leia vários valores numéricos em uma lista.
#  Mostrar o maior e o menor valor digitado e os índices onde eles estão.
#  Considerar que o número pode ter sido digitado várias vezes


from random import randint

lista = []

for i in range(50):
    num = randint(1,50)
    lista.append(num)
print(lista)