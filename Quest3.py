'''3. Faça um Programa que leia um número e exiba o dia correspondente da semana. 
(1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.'''

DIA = int(input('Digite um número inteiro no intervalo de 0 a 6 para escolher um dia da semana:\n'))
if DIA == 0:
	print('\tDOMINGO!')
elif DIA == 1:
	print('\tSEGUNDA!')
elif DIA == 2:
	print('\tTERÇA!')
elif DIA == 3:
	print('\tQUARTA!')
elif DIA == 4:
	print('\tQUINTA!')
elif DIA == 5:
	print('\tSEXTA!')
elif DIA == 6:
	print('\tSÁBADO!')
else:
	print('\tVALOR INVÁLIDO!')
