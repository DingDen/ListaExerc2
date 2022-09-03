'''6. Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. 
O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
a. Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
b. Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
c. Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
d. Se o delta for positivo, a equação possui duas raizes reais; informe-as ao usuário; '''

A = float(input('Digite o valor do coeficiente (a) da função do segundo grau: '))
if (A == 0):
	print('\n\tA equação não é do segundo grau!')
else:
	B = float(input('Agora, digite o valor do coeficiente (b): '))
	C = float(input('Por último, digite o valor do coeficiente (c): '))
	DELTA = B**2 - 4*A*C

	if (DELTA < 0):
		print('\n\tA equação não possui raízes reais!')
	elif (DELTA == 0):
		print('\n\tA equação possui apenas uma raiz real!')
	else:
		print('\n\tA equação possui duas raízes reais!')
