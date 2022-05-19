#Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. 
# Depois modifique o programa para que ele mostre os números um ao lado do outro. 


for a in range(1,21):
    print('Pulando linha: {0}'.format(a))
print('Na mesma linha: {0}'.format(list(range(1,21))))