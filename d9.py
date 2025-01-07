# Faça um programa que leia o ano de nascimento de um jovem e informe, 
# de acordo com a sua idade, 
# se ele ainda vai se alistar ao serviço militar, 
# se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
import datetime
ano_nascimento = int(input('Ano de nascimento: '))

ano = datetime.datetime.now().year

if ano - ano_nascimento < 18:
    print('Você ainda vai se alistar ao serviço militar')
elif ano - ano_nascimento == 18:
    print('É a hora exata de se alistar')
else:
    print('já passou do tempo do alistamento')