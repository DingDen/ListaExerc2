'''7. Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.'''

ANO = int(input('Digite um ano que é válido ao calendário gregoriano: '))
if (ANO%4 == 0) and (ANO%100 != 0):
	print(f'\n\t{ANO} é um ano bissexto!')
elif (ANO%4 == 0) and (ANO%100 == 0) and (ANO%400 == 0):
	print(f'\n\t{ANO} é um ano bissexto!')
else:
	print(f'\n\t{ANO} não é um ano bissexto!')
