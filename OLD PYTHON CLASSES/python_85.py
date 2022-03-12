#uso de try e except como condicional

def converte_numero(valor):
    try:
        valor = int(valor)
        return valor
    except ValueError:
        try:
            valor = float(valor)
            return valor
        except ValueError:
            pass

# while True:
#     numero = converte_numero(input("DIGITE UM NUMERO: "))
#     if numero is not None:
#         print(numero * 5)
#     else:
#         print("Isso nao é numero")
#EXECUTE
# DIGITE UM NUMERO: 1
# 5
# DIGITE UM NUMERO: 2
# 10
# DIGITE UM NUMERO: 2.5
# 12.5
# DIGITE UM NUMERO: a
# Isso nao é numero
# DIGITE UM NUMERO:

while True:
    numero = converte_numero(input("DIGITE UM NUMERO: "))

    if numero is None:
        print("isso não é um numero")
    else:
        print(numero * 2)