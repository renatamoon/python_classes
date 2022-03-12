#considerando duas listas de inteiros ou floats (lista A e B)
#some os valores nas listas retornando uma nova lista com valores somados:
#exemplo:

lista_a = [1,2,3,4,5,7,8]
lista_b = [1,2,3,4]
nova_lista = []
lista_soma = []

total1 = sum([int(x) for x in lista_a])
print(total1)
nova_lista.append(total1)
#
total2 = sum([int(y) for y in lista_b])
print(total2)
nova_lista.append(total2)
#transformando so valores em uma lista
print(nova_lista)

#A FORMA COMO O LUIZ OTAVIO FEZ:

lista_soma = [x + y for x, y in zip(lista_a, lista_b)]
print(lista_soma)
#execute: [2, 4, 6, 8] soma apenas os numeros que sao iguais, os outros
#numeros excedentes da lista não soma

#usando o ziplongest para incluir os valores a mais e somar também:

from itertools import zip_longest

lista_a = [10, 2, 3, 4, 5]
lista_b = [12, 2, 3, 6, 50, 60, 70]
lista_soma = [x + y for x, y in zip_longest(lista_a, lista_b, fillvalue=0)]
print(lista_soma)
#EXECUTE: [22, 4, 6, 10, 55, 60, 70]