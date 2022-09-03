'''8. Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.'''

DATA = input('Digite a data no formato DD.MM.AAAA (tudo junto como apenas um número de 8 digitos):\n\t')
DIA = int(DATA[0:2])
MES = DATA[2:4]
ANO = int(DATA[4:8])

if (MES == '01') or (MES == '03') or (MES == '05') or (MES == '07') or (MES == '08') or (MES == '10') or (MES == '12'):
	if (DIA != 0) and (DIA <= 31):
		print('\tDATA VÁLIDA!')
	else:
		  print('\tDATA INVÁLIDA!')
elif (MES == '04') or (MES == '06') or (MES == '09') or (MES == '11'):	
	if (DIA != 0) and (DIA <= 30):
		  print('\tDATA VÁLIDA!')
	else:
		  print('\tDATA INVÁLIDA!')
elif (MES == '02'):
	  if (ANO%4 == 0 and ANO%100 != 0) or (ANO%400 == 0):
		  if (DIA != 0) and (DIA <= 29):
			  print('\tDATA VÁLIDA!')
		  else:
			  print('\tDATA INVÁLIDA!')	
	  elif (DIA != 0) and (DIA <= 28):
		  print('\tDATA VÁLIDA!')
	  else:
		  print('\tDATA INVÁLIDA!')
else:
	print('\tDATA INVÁLIDA!')
