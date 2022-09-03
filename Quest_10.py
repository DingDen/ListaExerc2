'''10. Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:
e. A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada; 
f. A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada; 
g. A mensagem "Aprovado com Distinção", se a média for igual a 10.
'''

NOTA1 = float(input('Digite sua nota da 1AV: '))
NOTA2 = float(input('Digite sua nota da 2AV: '))
NOTA3 = float(input('Digite sua nota da 3AV: '))
MEDIA = (NOTA1 + NOTA2 + NOTA3) / 3

if (MEDIA == 10):
	print(f'\n\tAPROVADO COM DISTINÇÃO ------ Média: {MEDIA:.1f}')			
elif (MEDIA < 7):
	print(f'\n\tREPROVADO ------ Média: {MEDIA:.1f}')
else:
	print(f'\n\tAPROVADO ------ Média: {MEDIA:.1f}')
