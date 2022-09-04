'''16. Um posto está vendendo combustíveis com a seguinte tabela de descontos: 
r. Álcool: 
s. até 20 litros, desconto de 3% por litro 
t. acima de 20 litros, desconto de 5% por litro 
u. Gasolina: 
v. até 20 litros, desconto de 4% por litro 
w. acima de 20 litros, desconto de 6% por litro 
Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: 
A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90. 
'''

COMB = str(input('Qual o tipo de combustível? [A] para álcool ou [G] para gasolina: '))
LITROS = int(input('Quantos litros de combustível? '))
if (COMB == 'A'):
	NOME = 'Álcool'
	PRECO = 1.9
	if (LITROS <= 20):
		DESCONTO = LITROS*PRECO*0.03
		TOTAL =  (PRECO*LITROS) - DESCONTO
	else:
		DESCONTO = LITROS*PRECO*0.05
		TOTAL = (PRECO*LITROS) - DESCONTO	
else:
	NOME = 'Gasolina'
	PRECO = 2.5
	if (LITROS <= 20):
		DESCONTO = LITROS*PRECO*0.04
		TOTAL = 	(PRECO*LITROS) - DESCONTO
	else:
		DESCONTO = LITROS*PRECO*0.06
		TOTAL = (PRECO*LITROS) - DESCONTO

print(f'\n\t{LITROS} litro(s) vendidos\n\t{COMB}-{NOME}\n\tR${TOTAL:.2f}')
