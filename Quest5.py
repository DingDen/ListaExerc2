'''5. Faça um Programa que peça os 3 lados de um triângulo. 
O programa deverá informar se os valores podem ser um triângulo. 
Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.'''

L1 = float(input('Digite a medida de um dos lados do triângulo: '))
L2 = float(input('Agora, do outro lado: '))
L3 = float(input('E agora do último lado: '))

if (L1 + L2 > L3) and (L2 + L3 > L1) and (L1 + L3 > L2):
	print('\n\tEsses valores formam um triângulo!')
	
	if (L1 == L2) and (L1 == L3):
		print('\tTRIÂNGULO EQUILÁTERO!')
	elif (L1 != L2) and (L1 != L3) and (L2 != L3):
		print('\tTRIÂNGULO ESCALENO!')
	else:
		print('\tTRIÂNGULO ISÓSCELES!')
else:
	print('\n\tEsses valores não formam um triângulo!')
