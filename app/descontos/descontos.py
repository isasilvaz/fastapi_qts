def calcular_desconto(valor, cliente_vip):

    if valor <= 0:
        return 0
    else:
        if cliente_vip:
            return valor * 0.8
        else:
            return valor * 0.9