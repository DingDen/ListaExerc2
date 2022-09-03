'''15. Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são: 
m. "Telefonou para a vítima?" 
n. "Esteve no local do crime?" 
o. "Mora perto da vítima?" 
p. "Devia para a vítima?" 
q. "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
Caso contrário, ele será classificado como "Inocente". 
'''

PERG_1 = int(input('Telefonou para a vítima? [1] para SIM ou [2] para NÃO: '))
PERG_2 = int(input('Esteve no local do crime? [1] para SIM ou [2] para NÃO: '))
PERG_3 = int(input('Mora perto da vítima? [1] para SIM ou [2] para NÃO: '))
PERG_4 = int(input('Devia para a vítima? [1] para SIM ou [2] para NÃO: '))
PERG_5 = int(input('Já trabalhou com a vítima? [1] para SIM ou [2] para NÃO: '))

SEQUENCIA = (PERG_1 * PERG_2 * PERG_3 * PERG_4 * PERG_5)
if (SEQUENCIA == 1):
	print('\n\tASSASSINO!')
elif (SEQUENCIA == 2) or (SEQUENCIA == 4):
	print('\n\tCÚMPLICE!')
elif (SEQUENCIA == 8):
	print('\n\tSUSPEITO!')
else:
	print('\n\tINOCENTE!') 
