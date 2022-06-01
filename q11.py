#Altere o programa anterior para mostrar no final a soma dos números. 
a=int(input('Informe um numero inteiro: '))
b=int(input('Informe outro numero inteiro: '))

if a<b:
    for i in range(a,b):
        print(i)
if a>b:
    for i in range(b,a):
        print(i)

print(f'A soma de "a" e "b" é {a+b}')