#FILTER
from python_80 import produtos, pessoas, lista
#ela recebe uma função - retorna verdadeiro ou falso para a expressão
#que você informar
nova_lista = filter(lambda x: x > 5, lista)
#aqui estamos falando que filtrará dentro da função lambda
#cada valor x dentro da lista, se o x for maior que 5.
print(list(nova_lista)) #excute:[6, 7, 8, 9, 10]
print("=*"*10)
#se for fazer em list comprehension
nova_lista1 = [x for x in lista if x > 5]
print(list(nova_lista1)) #excute:[6, 7, 8, 9, 10]
print("=*"*10)
#usando dicionarios
#pegando no dicionario valores que sejam maiores que 10,00

nova_lista2 = filter(lambda p : p['preco'] > 50, produtos)

for produto in nova_lista2:
    print(produto)
#execute:
# {'nome': 'p2', 'preco': 55.5}
# {'nome': 'p10', 'preco': 83}
print("=*"*10)

def filtra(pessoa):
    if pessoa['idade'] >= 18:  #mostra apeans quem é maior de idade
        return True
    else:
        return False

nova_lista3 = filter(filtra, pessoas)

for produto in nova_lista3:
    print(produto)

