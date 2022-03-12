from python_80 import produtos, pessoas, lista
#importando os dados de um outro arquiv para trabalhar com codigo mais limpo
#precisamos mapear os dados
#fazendo uma list comprehension

# print(lista)
# nova_lista = map(lambda x: x * 2, lista) #dentro do lambda recebemos
    #uma função como argumento onde neste caso estamos multiplicando cada
    #item da lista (que colocamos como x) para que seja *2
#print(list(nova_lista))
        #execucao: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# for produto in produtos:
#     print(produto)
# #caso queira adicionar 5% em cada item dos produtos
# print("x"*20)

#precos = map(lambda p: p['preco'], produtos) #retornando o valor da chave preço dentro
#do dicionario de "produtos"

# for preco in precos:
#     print(preco) #retorna apenas o preço dentro da chave

# def aumenta_preco(p):
#     p['preco'] = round(p['preco'] * 1.05, 2) #arredondou duas casas
#     return p
#
# novos_produtos = map(aumenta_preco, produtos)
#
# for produto in novos_produtos:
#     print(produto)

#------criar uma lista somente com os nomes das pessoas
#usando a função map
#aumentando a idade das pessoas em 20%

def aumenta_idade(p):                           #2 = duas casas decimais
    p['nova_idade'] = round(p['idade'] * 1.20, 2)
    return p

nomes = map(aumenta_idade , pessoas)

for pessoa in nomes:
    print(pessoa)

#EXECUTE:
# {'nome': 'Luiz', 'idade': 32, 'nova_idade': 38.4}
# {'nome': 'max', 'idade': 40, 'nova_idade': 48.0}
# {'nome': 'norma', 'idade': 22, 'nova_idade': 26.4}
# {'nome': 'felipe', 'idade': 10, 'nova_idade': 12.0}
# {'nome': 'eduardo', 'idade': 12, 'nova_idade': 14.399999999999999}
# {'nome': 'pricila', 'idade': 40, 'nova_idade': 48.0}
# {'nome': 'ana', 'idade': 41, 'nova_idade': 49.199999999999996}
# {'nome': 'joao', 'idade': 5, 'nova_idade': 6.0}
# {'nome': 'linda', 'idade': 30, 'nova_idade': 36.0}
# {'nome': 'amara', 'idade': 22, 'nova_idade': 26.4}
#








