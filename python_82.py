#FUNÇÃO REDUCE
from python_80 import produtos, pessoas, lista
from functools import reduce #funcao acumuladora

print(lista)

acumula = 0
for item in lista:
    acumula += item
print(acumula) #soma todos os valores da lista

print("=*"*10)
soma_lista = reduce(lambda acumulador, item: item + acumulador,
                    lista, 0) #valor inicial é 0
#a ada volta do laço executa item + acumulador e guarda o valor no acumulador
print(soma_lista)

print("=*"*10)
soma_precos = reduce(lambda acumulador, p:p['preco'] + acumulador,
                     produtos, 0)
#acumulando os preços dentro do Acumulador, e no final teremos
#um valor reduzido com a soma de todos os preços.
print(soma_precos)

print("=*"*10)
soma_precos = reduce(lambda acumulador, p:p['preco'] + acumulador,
                     produtos, 0)
print(soma_precos/len(produtos)) #media de preços por produtos

print("=*"*10)
soma_idades = reduce(lambda acumulador, p: acumulador + p['idade'],
                     pessoas, 0)
print(soma_idades/len(pessoas)) #media de idades das pessoas do grupo

