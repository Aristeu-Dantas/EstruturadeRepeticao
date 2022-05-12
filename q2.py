#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, 
# mostrando uma mensagem de erro e voltando a pedir as informações.

login=input('Login: ')
senha=input('Senha: ')
while login==senha:
    print('Login não pode ser igual a senha.\nTente novamente.')
    login=input('Login: ')
    senha=input('Senha: ')
else:
    print('Login feito com sucesso!')