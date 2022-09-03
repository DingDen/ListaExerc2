'''12. Faça um Programa que peça um número inteiro e determine se ele é par ou ímpar.'''

NUM = int(input('\tDigite um número inteiro: '))

if (NUM % 2 == 0):
	print(f'\t{NUM} é um número par!')
else:
	print(f'\t{NUM} é um número ímpar!')
