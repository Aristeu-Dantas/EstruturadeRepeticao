# A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,...
# Faça um programa capaz de gerar a série até o n−ésimo termo. 

# n+1=n+n-1

anterior=0
proximo=1
soma=1

for n in range(0,31):
	print(anterior)
	soma=proximo+anterior
	anterior=proximo
	proximo=soma