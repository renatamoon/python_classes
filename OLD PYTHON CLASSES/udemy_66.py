#LISTS COMPREHESIONS
#sao usadas para duas coisas: otimização, performance, escrever menos linhas de codigo

l1 = [1,2,3,4,5,6,7,8,9]
ex1 = [variavel for variavel in l1] #jogar cada elemento desta 

# ex2 = [v*2 for v in l1]
# ex3 = [(v, v2) for v in l1 for v2 in range(3)]
#
# l2 = ['Luiz', 'mauro', 'maria']
# ex4 = [v.replace('a', '@a').upper() for v in l2]

# tupla = (
#     ('chave', 'valor'),
#     ('chave1', 'valor1'),
#     ('chave2', 'valor2'),
# )
# ex5 = [(y, x) for x, y in tupla] #invertendo os valores
# ex5 = dict(ex5) #transformando ex5 em dicionario
# print(ex5['valor2'])

#l3 = list(range(100))
# ex6 = [v for v in l3 if v % 3 == 0 if v % 8 == 0]
# print(ex6)

# l3 = list(range(100)) #fazendo uma lista divisivel de 0 a 100
# ex7 = [v if v % 3 == 0 and v % 8 == 0 else 'Não é divisivel' for v in l3]
# #if com duas condições
# print(ex7)

# l3 = list(range(100)) #fazendo uma lista divisivel de 0 a 100
# ex7 = [v if v % 3 == 0 and v % 8 == 0 else 0 for v in l3]
# #if com duas condições
# print(ex7)