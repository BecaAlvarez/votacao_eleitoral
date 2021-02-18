def vota(a):
    from datetime import date
    atual = date.today().year
    idade = atual - a
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA'
    if 16 <= idade < 18 or idade >= 70:
        return f'Com {idade} anos: VOTO OPCIONAL'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'
