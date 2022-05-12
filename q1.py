#Faça um programa que peça uma nota, entre zero e dez. 
# Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido. 

nota=int(input('Entregue uma nota entre zero a dez: '))
while nota<=0 or nota>=10:
    nota=int(input('Entregue uma nota entre zero a dez: '))
else:
    print('Obrigado!')