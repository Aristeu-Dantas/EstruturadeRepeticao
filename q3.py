#Faça um programa que leia e valide as seguintes informações:
#    Nome: maior que 3 caracteres;
#    Idade: entre 0 e 150;
#    Salário: maior que zero;
#    Sexo: 'f' ou 'm';
#    Estado Civil: 's', 'c', 'v', 'd'; 


nome=str(input('Nome: '))
while (len(nome)<=3):
    nome=str(input('Nome: '))

