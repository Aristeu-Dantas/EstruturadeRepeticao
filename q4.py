# Supondo que a população de um país A seja da ordem de 80.000 habitantes com uma taxa anual de
# crescimento de 3% e que a população de B seja 200.000 habitantes com uma taxa de crescimento de 1.5%. 
# Faça um programa que calcule e escreva o número de anos necessários para que a população do país A 
# ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento. 

a=80000
b=200000
crescimento_a=0.03
crescimento_b=0.015
anos=0

while a<b:
    a=a+(a*crescimento_a)
    b=b+(b*crescimento_b)
    anos=anos+1

print("Em {0} anos a população da cidade A irá ultrapassar a cidade B.".format(anos))