# Faça um programa que leia nome e salário de vários funcionários: Os valores devem ser armazenados em 2 vetores
# -Solicite a digitação de um percentual (%) de reajuste e conceda esse reajuste a todos os funcionários
# -Mostre: Nome e salário reajustado de todos

nome = []
salario = []

while True:
    cadastro = input('Cadastrar novo funcionário? (Sim) (Sair): ')
    if cadastro == 'Sair':
         break
    name = input('Nome do funcionário: ')
    sal = float(input('Salário: '))
    nome.append(name)
    salario.append(sal)

correcao = int(input('% a ser corrigido: '))

for i in range (len(salario)):
     corrige = (salario[i] * correcao) / 100
     salario[i] = salario [i] + corrige
     print(f'Salário do funconário: {nome[i]}, com a correção de {correcao}% aplicada, {salario[i]}')    