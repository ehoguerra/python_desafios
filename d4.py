# Desenvolva um programa que pergunte a distância de uma viagem em Km. 
# Calcule o preço da passagem, cobrando R$ 0,50 por Km para viagens de até 200Km 
# e R$ 0,45 parta viagens mais longas.​

distancia = int(input('Distancia da viagem: '))

if distancia <= 200:
    preco = distancia * 0.5
    print(f'O valor é {preco}')
else:
    preco = distancia * 0.45
    print(f'O valor é {preco}')