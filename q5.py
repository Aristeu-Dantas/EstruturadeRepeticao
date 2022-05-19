#Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais.
# Valide a entrada e permita repetir a operação. 

a=int(input('Informe a população da cidade A: '))
b=int(input('Informe a população da cidade B: '))
crescimento_a=float(input('Informe a taxa de crescimento da cidade A: '))
crescimento_b=float(input('Informe a taxa de crescimento da cidade B: '))
anos=0

while a<b:
    a=a+(a*crescimento_a)
    b=b+(b*crescimento_b)
    anos=anos+1

print("Em {0} anos a população da cidade A irá ultrapassar a cidade B.".format(anos))