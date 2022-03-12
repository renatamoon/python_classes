"""Faça um programa, com uma função que necessite de três argumentos, e que
forneça a soma desses três argumentos."""

# def soma_tres_argumentos(n1, n2, n3):
#     soma_argumentos = n1 + n2 + n3
#     return soma_argumentos
#
# print(soma_tres_argumentos(2,3,4))

"""Faça um programa, com uma função que necessite de um 
argumento. A função retorna o valor de caractere ‘P’, se seu
 argumento for positivo, e ‘N’, se seu argumento for
  zero ou negativo."""

# def retorna_valores(numero):
#     if numero > 0:
#         print("P")
#     elif numero == 0 or numero < 0:
#         print("N")
#
# print(retorna_valores(5))

"""Faça uma função que informe a quantidade de dígitos de 
um determinado número inteiro informado."""

# def quantidade_digitos(n):
#     digits = len(str(n))
#     return digits
# print(quantidade_digitos(20000))

"""Reverso do número. Faça uma função que retorne o reverso
 de um número inteiro informado. Por exemplo: 127 -> 721."""
#
# def reverso_numero(numero):
#     reverso = int(str(numero)[::-1])
#     return reverso
#
# print(reverso_numero(587522))

"""Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA
 e devolva uma string no formato D de mesPorExtenso de AAAA.
  Opcionalmente, valide a data e retorne NULL caso a data seja inválida."""

def retornar_data_DDMMAAAA(data_completa):
    data_completa = str(data_completa)
    for v in data_completa:
        print(v)

print(retornar_data_DDMMAAAA(26091994))

