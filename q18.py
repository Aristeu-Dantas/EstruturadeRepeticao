# Faça um programa que, dado um conjunto de N números, 
# determine o menor valor, o maior valor e a soma dos valores. 

lista=list()

for i in range(5):
    n=int(input('Informe um número: '))
    lista.append(n)
lista=sorted(lista)

print(f'Soma dos números: {sum(lista)}')
print(f'Menor número: {lista[0]}')
print(f'Maior número: {lista[-1]}')