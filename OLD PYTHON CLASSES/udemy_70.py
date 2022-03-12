#GERADORES, ITERADORES, ITERÁVEIS EM PYTHON

# lista = [0,1,2,3,4,5]
# lista = iter(lista)
#
# print(next(lista))
# print(next(lista))
# print(next(lista))
# print(next(lista))
# print(hasattr(lista, '__next__')) #ele fala que esse numero é iteravel

#import sys
#lista = list(range(1000))
#print(sys.getsizeof(lista)) #pega quanto que a lista está pegando de memoria
#execução: 136

#----------
import sys
# import time
#
# def gera():
#     # r = [] #cria um array em branco
#     for n in range(10): #faz uma laço de cada numero do range de 0 a 99
#         yield n #coloca os valores a cada interação do laço e colocando so valores
#         #n no array (lista) criada em branco "r"
#         time.sleep(0.1) #pedindo para que espere 0,1 segundo
#     #return r #retorna o valor
#     #os iteradores tem um metodo next
# g = gera()
# print(g)
#
# print(hasattr(g, '__iter__'))
# print(hasattr(g, '__next__'))
#execução: True; True

import sys
import time

# def gerador():
#     variavel = "valor 1"
#     yield variavel
#     variavel = "valor 2"
#     yield variavel
#     variavel = "valor 3"
#     yield variavel
#
# g = gerador()

#print(next(g)) #a cada vez que damos a função next, vamos para o proximo
#valor da variavel
#print(next(g))
#quando acabar os valores e tentar chamar novamente a funçã NEXT,
#ele vai dar erro. a MELHOR MANEIRA DE USAR A FUNÇÃO NEXT é usando
#o FOR
# for v in g:
#     print(v)
#execução:
# valor 1
# valor 2
# valor 3

#-------------
import sys
import time

# lista = list(range(200))
#
# print(sys.getsizeof(lista)) #execução:1656 bites

#usando list comprehension

lista = [x for x in range(10000)]
lista2 = (x for x in range(10000))

print(sys.getsizeof(lista)) #execução:1656 bites
print(sys.getsizeof(lista2))

#execução: 8856 / 112