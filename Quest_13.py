'''13. Faça um Programa que peça um número e informe se o número é inteiro ou decimal.'''

NUM = float(input('\tDigite um número real: '))

if (NUM % 1 == 0):
	print('\tO número é inteiro!')
else:
	print('\tO número é decimal!')
