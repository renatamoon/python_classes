#FUNÇÕES LAMBDA - PYTHON
#funcoes anonimas

# a = lambda x, y: x + y #destrinchando: colocando tudo numa variavel chamada A
#depois dizendo quais sao os parametros (no caso, x e y) e o ":" significa o calculo ou o que
#queremos que ela faça QUE NO CASO É x+y
#print(a(2,8)) #aqui fazemos como se fosse uma função, chamando o "a" da var
#e depois colocando entre parenteses os valores dos argumentos

lista = [
    ['p1', 13], #item 0 (p1) e item 1 (13)
    ['p2', 5],
    ['p3', 8],
    ['p4', 50],
    ['p5', 100],
]

# def funcao(item):
#     return item[1]
# lista.sort(key=funcao, reverse=True) #essa funcao retorna o valor ordenador:[['p2', 5], ['p3', 8], ['p1', 13], ['p4', 50], ['p5', 100]]
# print(lista)
#reverse=True MOSTRA O VALOR REVERSO DENTRO DA FUNCAO

#lista.sort(key=lambda item: item[1], reverse=True) #pega o item 1 que no caso é preço e faz
#do maior para o menor. Neste caso usando uma funcao lambda, nao é necessário fazer uma funcao
#para isso
#print(lista)

#---------ORDENAR LISTAS SEM AFETAR A LISTA ORIGINAL

print(sorted(lista, key=lambda i: i[1])) #i = item (no caso é o valor do produto (menor para o maior)
print(sorted(lista, key=lambda i: i[1], reverse=True)) #ordenando em ordem reversa
#execuções (isso porque nao mexe na lista original
# [['p2', 5], ['p3', 8], ['p1', 13], ['p4', 50], ['p5', 100]]
# [['p5', 100], ['p4', 50], ['p1', 13], ['p3', 8], ['p2', 5]]

#---ORDENANDO PELO NOME DO PRODUTO (EXEMPLO)

print(sorted(lista, key=lambda i: i[0], reverse=True)) #no caso pegando o indice 1 que é o 0
print(lista) #se der print na lista, ela aparece a lista original, isso porque nao muda a lista original




