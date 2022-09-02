'''1. As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contrataram para desenvolver o programa que calculará os reajustes.
◦ Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
◦ salários até R$ 280,00 (incluindo): aumento de 20%
◦ salários entre R$ 280,00 e R$ 700,00: aumento de 15%
◦ salários entre R$ 700,00 e R$ 1500,00: aumento de 10%
◦ salários de R$ 1500,00 em diante: aumento de 5% Após o aumento ser realizado, informe na tela:
◦ o salário antes do reajuste;
◦ o percentual de aumento aplicado;
◦ o valor do aumento;
◦ o novo salário, após o aumento.'''

SALARIO = float(input("Digite o seu salário: "))
if SALARIO <= 280 :
	REAJUSTE = SALARIO*1.2
	PERCENTUAL = '20%'
elif 280 < SALARIO <= 700:
	REAJUSTE = SALARIO*1.15
	PERCENTUAL = '15%'
elif 700 < SALARIO < 1500:
	REAJUSTE = SALARIO*1.1
	PERCENTUAL = '10%'
else:
	REAJUSTE = SALARIO*1.05
	PERCENTUAL = '5%'
AUMENTO = REAJUSTE - SALARIO

print('\t-------------------------------------------------------')
print(f'\t\tSalário antes do reajuste: R${SALARIO:.2f}')
print('\t\tPercentual de aumento aplicado: ', PERCENTUAL)
print(f'\t\tValor do aumento: R${AUMENTO:.2f}')
print(f'\t\tNovo salário após os reajustes: R${REAJUSTE:.2f}')
print('\t-------------------------------------------------------')
