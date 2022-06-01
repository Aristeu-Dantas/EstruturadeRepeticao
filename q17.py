# Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário.
#  Ex.: 5!=5.4.3.2.1=120 

numerof=int(input('Número a fatorar: '))

resultado=1
count=1

while numerof>=count:
    resultado*=count
    count+=1
print(resultado)