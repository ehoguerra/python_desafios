# Refaça o exercício 6 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo que será formado a partir dos segmentos informados pelo usuário:

# EQUILÁTERO: todos os lados iguais

# ISÓSCELES: dois lados iguais, um diferente

# ESCALENO: todos os lados diferentes

r1 = float(input('Tamanho da reta 1: '))
r2 = float(input('Tamanho da reta 2: '))
r3 = float(input('Tamanho da reta 3: '))

def triangulo():
    if r1 <= r2 + r3 and r2 <= r1 + r3 and r3 <= r1 + r2:
        return True
    else:
        print('Nao podem formar um triangulo')
while triangulo() == True:
    if r1 == r2 == r3:
        print('Equilatero')
        break
    elif r1 == r2 or r2 == r3 or r1 == r3:
        print('Isosceles')
        break
    else:
        print('Escaleno')
        break