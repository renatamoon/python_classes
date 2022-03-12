#DICTIONARY COMPREHENSION

# l1 = [1,2,3,4,5,6]
# l2 = [v*2 for v in l1]
# print(l2)
#execução: [2, 4, 6, 8, 10, 12] - ele pega cada valor da lista e multiplica
#por 2
#------------------
# lista = [
#     ("chave", "valor"),
#     ("chave2", "valor2"),
#
# ]
    #x é a chave #y é valor
# d1 = {x: y for x, y in lista}
# print(d1) #EXECUÇÃO:{'chave': 'valor', 'chave2': 'valor2'}
# d1 = dict(lista) #execução: {'chave': 'valor', 'chave2': 'valor2'}
#------------------
# lista = [
#     ("chave", 2),
#     ("chave2", "valor2"),
# ]
#
# d1 = {x: y*2 for x, y in lista}
# print(d1) #execução:{'chave': 4, 'chave2': 'valor2valor2'}
#------------------
# lista = [
#     ("chave", "valor"),
#     ("chave2", "valor2"),
# ]

# d1 = {x.upper(): y.upper() for x, y in lista} #colocando em maiusculo o valor
# print(d1) #execução: {'CHAVE': 'VALOR', 'CHAVE2': 'VALOR2'}
#
# d1 = {x: y for x, y in enumerate(range(5))}
# print(d1) #EXECUÇÃO: {0: 0, 1: 1, 2: 2, 3: 3, 4: 4} #mostra o valor de cada chave

d1 = {f'chave_{x}': x**2 for x in range(5)}
print(d1, type(d1))
#pedindo para que o valor da chave seja
#elevado a 2 sendo que a chave vai até range 5.
#{0: 0, 1: 1, 2: 2, 3: 3, 4: 4} e ele printa conforme a execução abaixo:
#EXECUÇÃO: {'chave_0': 0, 'chave_1': 1, 'chave_2': 4, 'chave_3': 9, 'chave_4': 16} <class 'dict'>






