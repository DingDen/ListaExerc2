'''11. Faça um Programa para um caixa eletrônico. 
O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas.
As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. 
O programa não deve se preocupar com a quantidade de notas existentes na máquina.'''

SAQUE = int(input('\tDigite o valor inteiro do saque: '))
if (SAQUE < 10) and (SAQUE > 600):
	print('O valor mínimo aceito é de 10 reais e o máximo de 600 reais!')
else:
	if(10 <= SAQUE < 50):
		NOTA_DEZ = SAQUE // 10
		NOTA_CINCO = (SAQUE % 10) // 5
		NOTA_UM = (SAQUE % 10 % 5) // 1
		print(f'\tPara um saque de R${SAQUE:.2f} teremos:\n')
		print(f'\tNotas de dez reais: {NOTA_DEZ}\n\tNotas de cinco reais: {NOTA_CINCO}\n\tNotas de um real: {NOTA_UM}')
	
	elif (50 <= SAQUE < 100):
		NOTA_CINQUENTA = SAQUE // 50
		NOTA_DEZ = (SAQUE % 50) // 10
		NOTA_CINCO = (SAQUE % 50 % 10) // 5
		NOTA_UM = (SAQUE % 50 % 10 % 5) // 1
		print(f'\tPara um saque de R${SAQUE:.2f} teremos:\n')
		print(f'\tNotas de cinquenta reais: {NOTA_CINQUENTA}\n\tNotas de dez reais: {NOTA_DEZ}\n\tNotas de cinco reais: {NOTA_CINCO}\n\tNotas de um real: {NOTA_UM}')
	
	else:
		NOTA_CEM = SAQUE // 100
		NOTA_CINQUENTA = (SAQUE % 100) // 50
		NOTA_DEZ = (SAQUE % 100 % 50) // 10
		NOTA_CINCO = (SAQUE % 100 % 50 % 10) // 5
		NOTA_UM = (SAQUE % 100 % 50 % 10 % 5) // 1
		print(f'\tPara um saque de R${SAQUE:.2f} teremos:\n')
		print(f'\tNotas de cem reais: {NOTA_CEM}\n\tNotas de cinquenta reais: {NOTA_CINQUENTA}\n\tNotas de dez reais: {NOTA_DEZ}\n\tNotas de cinco reais: {NOTA_CINCO}\n\tNotas de um real: {NOTA_UM}')
