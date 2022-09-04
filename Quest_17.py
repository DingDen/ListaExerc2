'''17. Uma fruteira está vendendo frutas com a seguinte tabela de preços: 
  Até 5 Kg:     Morango R$ 2,50 por Kg
                Maçã R$ 1,80 por Kg
                
Acima de 5 Kg:  Morango R$ 2,20 por Kg  
                Maçã R$ 1,50 por Kg
                
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. 
Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente. 
'''

KG_MACA = float(input('\tQuantidade, em quilos, de maçã: '))
KG_MORANGO =	float(input('\n\tQuantidade, em quilos, de morango: '))
COMPRA = KG_MACA + KG_MORANGO

if (KG_MACA <= 5) or (KG_MORANGO <= 5) or (COMPRA <= 5):
	TOTAL_COMPRA =  (KG_MACA*1.8) + (KG_MORANGO*2.5) 
else:
	TOTAL_COMPRA = (KG_MACA*1.5) + (KG_MORANGO*2.2)
	if (COMPRA > 8) or (TOTAL_COMPRA > 25):
		TOTAL_COMPRA *= 0.9
print(f'\n\tQuantidade de maçãs: {KG_MACA} KG\n\tQuantidade de morangos: {KG_MORANGO} KG\n\tValor a ser pago: R${TOTAL_COMPRA:.2f}')
