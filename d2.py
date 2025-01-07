# Escreva um programa que leia a velocidade de um carro. 
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. 
# A multa vai custar R$7,00 por cada Km acima do limite e mais 10% caso a velocidade ultrapasse 120 km/h.

speed = float(input('Digite a velocidade do carro: '))

if 80 < speed < 120:
    add = speed - 80
    valor = 7 * add
    print(f'Voce foi multado em R${valor}')
elif speed > 120:
    add = speed - 80
    v2 = 7 * add
    valor = v2 + (v2 * 10/100)
    print(f'Voce foi multado em R${valor}')
else:
    print('Nao multado')






