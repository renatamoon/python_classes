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
import time

def gera():
    r = [] #cria um array em branco
    for n in range(100): #faz uma laço de cada numero do range de 0 a 99
        r.append(n) #coloca os valores a cada interação do laço e colocando so valores
        #n no array (lista) criada em branco "r"
        time.sleep(0.1) #pedindo para que espere 0,1 segundo
    return r #retorna o valor

g = gera()

for v in g:
    print(v)


