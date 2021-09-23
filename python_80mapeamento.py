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

nomes = map(lambda p: p['idade'] * 1.20 , pessoas)

for pessoa in nomes:
    print(pessoa)







