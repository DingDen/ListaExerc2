'''18. O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira: 
    Até 5 Kg:    File Duplo R$ 4,90 por Kg; 
                 Alcatra R$ 5,90 por Kg; 
                 Picanha R$ 6,90 por Kg.

Acima de 5 Kg:   File Duplo R$ 5,80 por Kg; 
                 Alcatra R$ 6,80 por Kg; 
                 Picanha R$ 7,80 por Kg.
                 
Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente. 
Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. 
Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: 
tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar. 
'''

CARNE = int(input('\n\tEscolha [1] para FILE DUPLO, [2] para ALCATRA e [3] para PICANHA: '))
CKG = int(input('\tQuantos quilos de carne: '))
FORMA_PAG = int(input('\tEscolha [1] para USAR o cartão TABAJARA ou [2] para NÃO usar o cartão: '))

if (FORMA_PAG == 1):
	CARTAO = 'TABAJARA'
	if (CKG <= 5):
		if (CARNE == 1):
			PRECO = (CKG*4.9)*0.95
			DESCONTO = (PRECO / 0.95) - PRECO
			TIPO = 'FILE DUPLO'
		elif (CARNE == 2):
			PRECO = (CKG*5.9)*0.95
			DESCONTO = (PRECO / 0.95) - PRECO
			TIPO = 'ALCATRA'
		else:
			PRECO = (CKG*6.9)*0.95
			DESCONTO = (PRECO / 0.95) - PRECO
			TIPO = 'PICANHA'
	else:
		if (CARNE == 1):	
			PRECO = (CKG*5.8)*0.95
			DESCONTO = (PRECO / 0.95) - PRECO
			TIPO = 'FILE DUPLO'
		elif (CARNE == 2):
			PRECO = (CKG*6.8)*0.95
			DESCONTO = (PRECO / 0.95) - PRECO
			TIPO = 'ALCATRA'
		else:
			PRECO = (CKG*7.8)*0.95
			DESCONTO = (PRECO / 0.95) - PRECO
			TIPO = 'PICANHA'
	print('\n\t----------------NOTA FISCAL----------------')
	print(f'\t\tTipo de carne: {TIPO}\n\t\tQuantidade de carne: {CKG} KG\n\t\tForma de pagamento: {CARTAO}\n\t\tPreço total: R${PRECO:.2f}\n\t\tDesconto: R${DESCONTO:.2f}')
	print('\t-------------------------------------------')
else:
	CARTAO = 'NÃO TABAJARA'
	if (CKG <= 5):
		if (CARNE == 1):
			PRECO = CKG*4.9
			TIPO = 'FILE DUPLO'
		elif (CARNE == 2):
			PRECO = CKG*5.9
			TIPO = 'ALCATRA'
		else:
			PRECO = CKG*6.9
			TIPO = 'PICANHA'
	else:
		if (CARNE == 1):	
			PRECO = CKG*5.8
			TIPO = 'FILE DUPLO'
		elif (CARNE == 2):
			PRECO = CKG*6.8
			TIPO = 'ALCATRA'
		else:
			PRECO = CKG*7.8
			TIPO = 'PICANHA'
	print('\n\t----------------NOTA FISCAL----------------')
	print(f'\t\tTipo de carne: {TIPO}\n\t\tQuantidade de carne: {CKG} KG\n\t\tForma de pagamento: {CARTAO}\n\t\tPreço total: R${PRECO:.2f}\n\t\tDesconto: SEM DESCONTO')
	print('\t-------------------------------------------')
