# Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial
# várias vezes e limitando o fatorial a números inteiros positivos e menores que 16. 

#Definindo resposta de continuação
rep='S'
#Lógica para perguntar várias vezes
while rep=='S':
    resultado=1
    count=1
    numerof=int(input('Número de 1 à 16 para fatorar: '))
    if numerof>0 and numerof<16:#Determinção de limite 1 à 16
        while numerof>=count:#Lógica de fatoração
            resultado*=count
            count+=1
        print(resultado)
        rep=input('Deseja continuar?(S/n) ')
    else:
        print('Número inválido!\nInforme um número de 1 à 16.')
        break
else:
    print('Programa encerrado.')
