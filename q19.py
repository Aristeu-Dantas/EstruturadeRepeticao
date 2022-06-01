# Altere o programa anterior para que ele aceite apenas números entre 0 e 1000. 

lista=list()
n=1
for i in range(5):
    n=int(input('Informe um número: '))
    if n<0 or n>1000:
        print('Número não aceito.')
    else:
        lista.append(n)
lista=sorted(lista)

print(f'Soma dos números: {sum(lista)}')
print(f'Menor número: {lista[0]}')
print(f'Maior número: {lista[-1]}')