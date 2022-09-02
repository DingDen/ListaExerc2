'''2.Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, 
que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, 
mas não é descontado (é a empresa que deposita). 
O Salário Líquido corresponde ao Salário Bruto menos os descontos. 
O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
◦ Desconto do IR:
◦ Salário Bruto até 900 (inclusive) - isento
◦ Salário Bruto até 1500 (inclusive) - desconto de 5%
◦ Salário Bruto até 2500 (inclusive) - desconto de 10%
◦ Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo.'''

VALOR_HORA = float(input('Digite o valor da sua hora: '))
HORA_MES = int(input('Digite a quantidade de horas trabalhadas no mês: '))
SALARIO_BRUTO = VALOR_HORA*HORA_MES
FGTS = SALARIO_BRUTO*0.11
SIND = SALARIO_BRUTO*0.03

if SALARIO_BRUTO <= 900:
	IR = 'Isento'
	VALOR_IR = SALARIO_BRUTO*0
	
elif 900 < SALARIO_BRUTO <= 1500:
	IR = '5%'
	VALOR_IR = SALARIO_BRUTO*0.05

elif 1500 < SALARIO_BRUTO <= 2500:
	IR = '10%'
	VALOR_IR = SALARIO_BRUTO*0.10

else: 
	IR = '20%'
	VALOR_IR = SALARIO_BRUTO*0.20
TOTAL_DESCONTOS = VALOR_IR + SIND
SALARIO_LIQUIDO = SALARIO_BRUTO - TOTAL_DESCONTOS

print(f'\tSalário bruto: R${SALARIO_BRUTO:.2f}')
print(f'\tIR ({IR}): R${VALOR_IR:.2f}')
print(f'\tSindicato (3%): R${SIND:.2f}')
print(f'\tFGTS (11%): R${FGTS:.2f}')
print(f'\tTotal de descontos: R${TOTAL_DESCONTOS:.2f}')
print(f'\tSalário líquido: R${SALARIO_LIQUIDO:.2f}')
