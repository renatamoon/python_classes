#combinations, permutations e product - itertools
#combinacao - ordem nao importa
#permutação - ordem importa
#ambos nao repetem valores unicos
#produto - ordem importa e repete valores unicos

from itertools import combinations, permutations, product

lista_pessoas = ["luiz", "andre", "eduardo", "leticia", "fabricio", "rose"]
#queira saber todas as combinações possivels dessa lista

#----------- COMBINATIONS - mostra todas as combinações possiveis sem ordem, menos valores repetidos
# for grupo in combinations(lista_pessoas, 2): #combinando de 2 em 2
#     print(grupo) #execute - a ordem nao importa
# ('luiz', 'andre')
# ('luiz', 'eduardo')
# ('luiz', 'leticia')
# ('luiz', 'fabricio') etc

#---------PERMUTATIONS - todas as combinações possiveis na ordem, menos valores repetidos

# for grupo in permutations(lista_pessoas, 2): #lista onde a ordem importa
#     print(grupo) #execute
    #('luiz', 'andre')
# ('luiz', 'eduardo')
# ('luiz', 'leticia')
# ('luiz', 'fabricio')

#----- PRODUCT - mostra todas as possibilidades inclusive todas as repetições de valores
for grupo in product(lista_pessoas, repeat=2): #precisamos mostra quntas vezes irá repetir
    print(grupo)

#combinações em grupos de 3 onde a ordem nao função




