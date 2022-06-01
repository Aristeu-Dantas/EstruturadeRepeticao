#Faça um programa que receba dois números inteiros e gere os números inteiros que estão 
# no intervalo compreendido por eles. 

a=int(input('Informe um numero inteiro: '))
b=int(input('Informe outro numero inteiro: '))

if a<b:
    for i in range(a,b):
        print(i)
if a>b:
    for i in range(b,a):
        print(i)