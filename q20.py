# Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial
# várias vezes e limitando o fatorial a números inteiros positivos e menores que 16. 

# numerof=int(input('Número de 1 à 16 para fatorar: '))

resultado=1
count=1
rep='S'

while rep=='S':
    # resultado=1
    numerof=int(input('Número de 1 à 16 para fatorar: '))
    if numerof>0 and numerof<16:
        while numerof>=count:
            resultado*=count
            count+=1
        print(resultado)
        rep=input('Deseja continuar?(S/n) ')
    else:
        print('Número inválido!\nInforme um número de 1 à 16.')
        break
else:
    print('Programa encerrado.')
#rep=input('Deseja continuar?(S/n) ')