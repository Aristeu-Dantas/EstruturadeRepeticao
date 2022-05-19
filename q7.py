#Faça um programa que leia 5 números e informe o maior número. 

n1=int(input('Informe o número 1: '))
n2=int(input('Informe o número 2: '))
n3=int(input('Informe o número 3: '))
n4=int(input('Informe o número 4: '))
n5=int(input('Informe o número 5: '))

lista=[n1,n2,n3,n4,n5]
lista.sort(reverse=True)

print(f'O maior número é o {lista[0]}')