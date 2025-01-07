# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valor_casa = int(input('Valor da casa: '))
salario_c = int(input('Digite seu salário: '))
tempo_pg = int(input('Anos para quitar a casa: '))

meses = tempo_pg * 12
valor_mensal = valor_casa / meses

if valor_mensal < salario_c * 0.3:
    print('Aprovado')
else:
    print('negado')