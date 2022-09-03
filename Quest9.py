'''9. Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.'''

NUM = (input('\tDigite um número inteiro menor que 1000: '))
if (int(NUM) > 999):
	print('\tUse apenas números inteiros menores que 1000!')
else:
	if (int(NUM) < 10):
		UNIDADE = NUM[0:1]
		
		if (UNIDADE == '1'):
			TERMO = 'unidade'
		else:
			TERMO = 'unidades'	
		print(f'\t{UNIDADE} {TERMO}')

	elif (10 <= int(NUM) < 100):
		DEZENA = NUM[0:1]
		UNIDADE = NUM[1:2]
		
		if (DEZENA == '1') and (UNIDADE == '1'):
			TERMO = 'dezena'
			TERMO_U = 'unidade'
		elif (DEZENA == '1') and (UNIDADE != '1'):
			TERMO = 'dezena'
			TERMO_U = 'unidades'
		elif (int(DEZENA) > 1) and (UNIDADE == '1'):
			TERMO = 'dezenas'
			TERMO_U = 'unidade'
		else:
			TERMO = 'dezenas'
			TERMO_U = 'unidades'
		print(f'\t{DEZENA} {TERMO} e {UNIDADE} {TERMO_U}')

	else:
		CENTENA = NUM[0:1]
		DEZENA = NUM[1:2]
		UNIDADE = NUM[2:3]
		
		if (CENTENA == '1') and (DEZENA == '1') and (UNIDADE == '1'):
			TERMO = 'centena'
			TERMO_D = 'dezena'
			TERMO_U = 'unidade'		
		elif (CENTENA == '1') and (DEZENA != '1') and (UNIDADE != '1'):
			TERMO = 'centena'
			TERMO_D = 'dezenas'
			TERMO_U = 'unidades'
		elif (CENTENA == '1') and (DEZENA == '1') and (UNIDADE != '1'):
			TERMO = 'centena'
			TERMO_D = 'dezena'
			TERMO_U = 'unidades'
		elif (CENTENA == '1') and (DEZENA != '1') and (UNIDADE == '1'):
			TERMO = 'centena'
			TERMO_D = 'dezenas'
			TERMO_U = 'unidade'
		elif (int(CENTENA) > 1) and (DEZENA == '1') and (UNIDADE == '1'):
			TERMO = 'centenas'
			TERMO_D = 'dezena'
			TERMO_U = 'unidade'
		elif (int(CENTENA) > 1) and (DEZENA != '1') and (UNIDADE == '1'):
			TERMO = 'centenas'
			TERMO_D = 'dezenas'
			TERMO_U = 'unidade'
		elif (int(CENTENA) > 1) and (DEZENA == '1') and (UNIDADE != '1'):
			TERMO = 'centenas'
			TERMO_D = 'dezena'
			TERMO_U = 'unidades'
		else:
			TERMO = 'centenas'
			TERMO_D = 'dezenas'
			TERMO_U = 'unidades'
		print(f'\t{CENTENA} {TERMO}, {DEZENA} {TERMO_D} e {UNIDADE} {TERMO_U}')
