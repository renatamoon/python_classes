#MAIS SOBRE GERADORES
#consumir os valores deles.
#listas, tuples, strings - iterável
nome = 'luiz otavio'
iterador = iter(nome)
gerador = (letra for letra in nome)

print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))
print("OLA O FOR")

for letra in gerador:
    print(letra)

# try:
#     print(next(iterador)) #entrega a primeira letra
#     print(next(iterador)) #entrega a segunda letra
#     print(next(iterador)) #assim por diante
#     print(next(iterador))
# except:
#     pass #peço para ele nao executar mais nada
# #esgotamos o iterador. Não conseguimos mais printar o iterador
# print("cade os valores")
# for valor in iterador: #aqui depois de ter printado o next antes, ele usa
#     #os valores restantes da string nome que nao foram usados pelo next
#     print(valor) #ele printa cada letra do nome - ele printa Otavio

# for letra in nome:
#     print(letra)
#
# print("x" * 20)
#
# for letra in nome:
#     print(letra)
#o for usa o __next__ até o iterador esgotar

