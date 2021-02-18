from funcao import *

while True:
    r = 1
    try:
        ano = int(input("Em que ano você nasceu? "))
    except (ValueError, TypeError):
        print("VALOR INVÁLIDO!")
        break
    else:
        print(vota(ano))
    while r:
        resp = str(input("Desejas continuar?[S/N] "))
        if resp in 'Ss':
            break
        r = 0
    else:
        break

print('Programa Finalizado')