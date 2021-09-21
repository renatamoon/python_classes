#FOR/ELSE
#
# variavel = ['Renata Monteiro', 'João Cardoso', 'Eliane Felix']
#
# comeca_com_j = False
# for valor in variavel:
#     if valor.lower().startswith('j'): #essa função checa se o valor começa com X
#         #e também faz a palavra se transformar para minusculo
#         comeca_com_j = True
#
# if comeca_com_j:
#     print("EXISTE UMA PALAVRA QUE COMEÇA COM J")
# else:
#     print("NÃO EXISTE UMA PALAVRA QUE COMEÇA COM J")
#NÃO COMEÇA COM M
# COMEÇA COM M Maria Cardoso
# NÃO COMEÇA COM M

#FUNÇÃO ENUMERAR
# lista = [
#     [0, 'Luiz'],
#     [1, 'João'],
#     [2, 'Maria'],
# ]
# for indice, nome in lista:
#     print(indice, nome)
#DESEMPACOTANDO AS LISTAS - ELE FAZ O QUE A FUNÇÃO ENUMERATE FAZ.
#O RESULTADO FICARIA O SEGUINTE:
# 0 Luiz
# 1 João
# 2 Maria

#FAZENDO A FUNÇÃO ENUMERATE:

# lita = ['luiz', 'joao', 'maria']
#
# for indice, nome in enumerate(lista):
#     print(indice, nome)

# #no caso o resultado seria o seguinte:
# 0 [0, 'Luiz']
# 1 [1, 'João']
# 2 [2, 'Maria']

#DESEMPACOTAMENTO DE LISTAS EM PYTHON

lista = ['luiz', 'joao', 'maria', 1,2,3,4,5,6,7]

n1, n2, n3, *outra_lista, ultimo_item = lista

print(n1, n2, n3) #nesse caso eu estou dizendo que a a var n1 é o primeiro
#item da lista, o n2 é segundo item da lista, assim pór diante
#ao que se refere ao *outra_lista, se refere ao restante da lista e que não
#foram adicionados a nenhuma variável
print(ultimo_item) #como eu adicionei um ultimo item dentro do jogo de variáveis,
#então é tido como ultimo item da variável