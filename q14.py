# Faça um programa que peça 10 números inteiros, 
# calcule e mostre a quantidade de números pares e a quantidade de números impares.

par=list()
impar=list()
for i in range(10):
    n=float(input('Informe número inteiro: '))
    if n%2==0:
        par.append(n)
    else:
        impar.append(n)
print(f'{len(par)} numeros pares e {len(impar)} numeros impares')