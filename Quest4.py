'''4. Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. 
A atribuição de conceitos obedece à tabela abaixo:
Média de Aproveitamento Conceito 
  Entre 9.0 e 10.0 (A) 
  Entre 7.5 e 9.0 (B) 
  Entre 6.0 e 7.5 (C) 
  Entre 4.0 e 6.0 (D) 
  Entre 4.0 e zero (E)
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.'''

MEDIA = (NOTA1 + NOTA2) / 2

if (0 <= MEDIA <= 4):
	CONCEITO = 'E'
elif (4 < MEDIA < 6):
	CONCEITO = 'D'
elif (6 <= MEDIA <= 7.5):
	CONCEITO = 'C'
elif (7.5 < MEDIA < 9):
	CONCEITO = 'B'
else:
	CONCEITO = 'A'

print('\n\tNOTA DA 1º AV: ', NOTA1)
print('\tNOTA DA 2º AV: ', NOTA2)
print('\tMÉDIA: ', MEDIA)
print('\tCONCEITO: ', CONCEITO)

if (CONCEITO == 'A') or (CONCEITO == 'B') or (CONCEITO == 'C'):
	print('\tAPROVADO!')
else:
	print('\tREPROVADO!')
