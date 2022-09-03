'''14. Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. 
O resultado da operação deve ser acompanhado de uma frase que diga se o número é: 
j. par ou ímpar; 
k. positivo ou negativo; 
l. inteiro ou decimal. 
'''

NUM1 = float(input('Digite um número real (n1): '))
NUM2 = float(input('Digite outro número real (n2): '))

OP = int(input('\tQual operação você deseja utilizar:\n\t[1] para SOMA\n\t[2] para SUBTRAÇÃO (n1 - n2)\n\t[3] para MULTIPLICAÇÃO\n\t[4] para DIVISÃO (n1 / n2)\n\tOPERAÇÃO: '))

if (OP == 1):
	SOMA = NUM1 + NUM2
	if (SOMA % 1 == 0):
		if (SOMA % 2 == 0):
			if (SOMA < 0):
				print(f'\t\t{SOMA} é um número inteiro')
				print(f'\t\tO módulo de {SOMA} é um número par')
				print(f'\t\t{SOMA} é um número negativo')
			else:
				print(f'\t\t{SOMA} é um número inteiro')
				print(f'\t\tO módulo de {SOMA} é um número par')
				print(f'\t\t{SOMA} é um número positivo')
		else:
			if (SOMA < 0):
				print(f'\t\t{SOMA} é um número inteiro')
				print(f'\t\tO módulo de {SOMA} é um número ímpar')
				print(f'\t\t{SOMA} é um número negativo')
			else:
				print(f'\t\t{SOMA} é um número inteiro')
				print(f'\t\tO módulo de {SOMA} é um número ímpar')
				print(f'\t\t{SOMA} é um número positivo')
	else:
		if (SOMA < 0):
			print(f'\t\t{SOMA} é um número decimal')
			print(f'\t\t{SOMA} é um número negativo')
		else:
			print(f'\t\t{SOMA} é um número decimal')
			print(f'\t\t{SOMA} é um número positivo')

elif (OP == 2):
	SUB = NUM1 - NUM2
	if (SUB % 1 == 0):
		if (SUB % 2 == 0):
			if (SUB < 0):
				print(f'\t\t{SUB} é um número inteiro')
				print(f'\t\tO módulo de {SUB} é um número par')
				print(f'\t\t{SUB} é um número negativo')
			else:
				print(f'\t\t{SUB} é um número inteiro')
				print(f'\t\tO módulo de {SUB} é um número par')
				print(f'\t\t{SUB} é um número positivo')
		else:
			if (SUB < 0):
				print(f'\t\t{SUB} é um número inteiro')
				print(f'\t\tO módulo de {SUB} é um número ímpar')
				print(f'\t\t{SUB} é um número negativo')
			else:
				print(f'\t\t{SUB} é um número inteiro')
				print(f'\t\tO módulo de {SUB} é um número ímpar')
				print(f'\t\t{SUB} é um número positivo')
	else:
		if (SUB < 0):
			print(f'\t\t{SUB} é um número decimal')
			print(f'\t\t{SUB} é um número negativo')
		else:
			print(f'\t\t{SUB} é um número decimal')
			print(f'\t\t{SUB} é um número positivo')
elif (OP == 3):
	MULT = NUM1 * NUM2
	if (MULT % 1 == 0):
		if (MULT % 2 == 0):
			if (MULT < 0):
				print(f'\t\t{MULT} é um número inteiro')
				print(f'\t\tO módulo de {MULT} é um número par')
				print(f'\t\t{MULT} é um número negativo')
			else:
				print(f'\t\t{MULT} é um número inteiro')
				print(f'\t\tO módulo de {MULT} é um número par')
				print(f'\t\t{MULT} é um número positivo')
		else:
			if (MULT < 0):
				print(f'\t\t{MULT} é um número inteiro')
				print(f'\t\tO módulo de {MULT} é um número ímpar')
				print(f'\t\t{MULT} é um número negativo')
			else:
				print(f'\t\t{MULT} é um número inteiro')
				print(f'\t\tO módulo de {MULT} é um número ímpar')
				print(f'\t\t{MULT} é um número positivo')
	else:
		if (MULT < 0):
			print(f'\t\t{MULT} é um número decimal')
			print(f'\t{MULT} é um número negativo')
		else:
			print(f'\t\t{MULT} é um número decimal')
			print(f'\t\t{MULT} é um número positivo')
	
else:
	DIV = NUM1 / NUM2
	if (DIV % 1 == 0):
		if (DIV % 2 == 0):
			if (DIV < 0):
				print(f'\t\t{DIV} é um número inteiro')
				print(f'\t\tO módulo de {DIV} é um número par')
				print(f'\t\t{DIV} é um número negativo')
			else:
				print(f'\t\t{DIV} é um número inteiro')
				print(f'\t\tO módulo de {DIV} é um número par')
				print(f'\t\t{DIV} é um número positivo')
		else:
			if (DIV < 0):
				print(f'\t\t{DIV} é um número inteiro')
				print(f'\t\tO módulo de {DIV} é um número ímpar')
				print(f'\t\t{SOMA} é um número negativo')
			else:
				print(f'\t\t{DIV} é um número inteiro')
				print(f'\t\tO módulo de {DIV} é um número ímpar')
				print(f'\t\t{DIV} é um número positivo')
	else:
		if (DIV < 0):
			print(f'\t\t{DIV} é um número decimal')
			print(f'\t\t{DIV} é um número negativo')
		else:
			print(f'\t\t{DIV} é um número decimal')
			print(f'\t\t{DIV} é um número positivo')
