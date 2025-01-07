# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado, 
# a quantidade de dias pelos quais ele foi alugado e se o cliente faz parte do programa de fidelidade da loja. 
# Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por Km rodado para clientes não participantes do programa de fidelidade 
# e R$ 58 a diária mais R$0,05 por Km rodado para clientes participantes do programa de fidelidade.

km = float(input('Digite a quantidade de Km percorridos: '))
dias = int(input('Digite a quantidade de dias de aluguel: '))

fidelidade = input('Você faz parte do programa de fidelidade? (s/n): ')

if fidelidade == 's':
    valor = 58 * dias + 0.05 * km
else:
    valor = 60 * dias + 0.15 * km