#CONJUNTOS - COLEÇÃO DE ELEMENTOS DENTRO DE UMA ESTRUTURA DE DADOS
#add, update, clear, discard
#union / une
#intersection & - todos os elementos presentes nos dois sets
#difference - elementos no set da esquerda
#symmetric_difference - elementos que estao nos dois sets, mas nao em ambos

# s1 = {1,2,3,4,5} #set ou conjunto que sao a mesma coisa
# print(s1) #nao tem par de chaves ou valores
# for v in s1:
#     print(v)
#podemos adicionar valores dentro do conjunto
# s1 = set()
# s1.add(1)
# s1.add(2)
# s1.add((1,2,3,'Luiz')) #pedindo para adicionar elementos dentro do set/conjunto
# s1.discard(2) #remover o elemento 2 - execute:{1, (1, 2, 3, 'Luiz')}
# s1.update('a') #adicionando um valor mas é iterável, manda uma lista ou outro set
# print(s1)

# l1 = {1,2,1,1,3,4,5,6,6,6,6,7,8,9}
# l1 = set(l1)#nao tem elementos duplicados - remove os elementos duplicados
# l1 = list(l1) #pedindo para retornar a ser uma lista
# print(l1[-1]) #acessando o ultimo elemento da lista

#USANDO O UNION - |

# set1 = {1,2,3,4,5,6,7}
# set2 = {1,2,3,4,5,6,8}
# set3 = set1 | set2 #usando o pipe
# print(set3) #EXECUTE: {1, 2, 3, 4, 5, 6}
# #USANDO O INTERSECÇÃO - "&"
# set4 = set1 & set2
# print(set4) #execute: {1, 2, 3, 4, 5} - mostra todos os elementos que estão presentes em ambos
# set5 = set2 - set1
# print(set5) #execute: {6} mostra apenas o elemento que nao está em ambos
# #USANDO DIFFERENCE ^
# set6 = set2 ^ set1
# print(set6) #{7, 8} - mostra apenas dos elementos diferentes dentro das duas listas

lista1 = ['luiz', 'joao', 'maria']
lista2 = ['joao', 'maria', 'luiz', 'luiz', 'luiz']

print(lista1 != lista2) #retorna True pois as listas em si são diferentes
lista1 = set(lista1) #transformando as listas acima em set
lista2 = set(lista2) #transformando as listas acima em set

print(lista1 == lista2) #retorna True, pois as listas tem elementos iguais

if set(lista1) == set(lista2):
    print("LISTA 1 É IGUAL A LISTA2")
else:
    print("LISTA1 É DIFERENTE DE LISTA2")
#RETORNA: LISTA 1 É IGUAL A LISTA2 MESMO CONTENDO VARIOS ELEMENTOS DUPLICADOS, POIS
#AO ANALISAR O CODIGO, ELE RETORNA E COMPARA APENAS OS VALORES IGUAIS
