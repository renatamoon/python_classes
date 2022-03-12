#listas em PYTHON
#fatiamento
#append, insert, pop, del, clear, extend, +
#min, max
#range
#-----------
# booleanos = True
# Inteiros = 10
# flutuantes = -10.10
# strings = texto

#lista pode conter varios valores dentro de colchetes

# texto = 'valor'
# lista = [1, 2, 3, 4] #coo se fosse um variável
#mas podemos colocar qualquer coisa dentro dela
#[1, 2, 3, 'luiz otavio', True]

#indices  0   1    2    3    4
#   lista = ['a','b', 'c', 'd', 'e']
#        -5  -4   -3   -2   -1
#para acessar os valores dentro desta lista, devemos acessar atraves
#de indices
# string = "ABCDE"

# print(string[1]) # o indice 1 é a letra B

# lista = ['a','b', 'c', 'd', 'e', 10,5]
# print(lista[::2]) #começo, fim, e o pulo que no caso
#                     #é 2
# #['a', 'c', 'e', 5]

# print(lista[::-1])#ele vai inverter a lista de tras pra frente
# #[5, 10, 'e', 'd', 'c', 'b', 'a']

# lista_1 = [1,2,3]
# lista_2 = [4,5,6]
# #lista_1.extend(lista_2) #a lista_1 irá adicionar os valores
# #da lista 1 nela. ODE

# lista_2.append('b') #adicionando um valor no final da lista
# print(lista_2)
# lista_2.insert(0, "banana") #ADICIONANDO o valor de banana ao indice 0
# #RESULTADO - ['banana', 4, 5, 6, 'b']
# lista_2.pop()
# print(lista_2)

#----- ITERAR ELEMENTOS DE UMA LISTA

# l2 = [0,1,2,3,4,5,6,7,8,9]
# #print(l2) #RESULTADO: [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# for c in l2:
#     # print(c)
#     soma = soma + c #soma de todos os valores da lista
#     print(f'{soma} + {c} = {soma}')

#joguinho que irá descobrir qual a letra na palavra secreta
#na verdade tipo um jogo da forca
secreto = "perfume"
digitadas = []
chances = 3
while True:
    if chances <= 0: #aqui estou imputando o while True das chances
        #antes do laço que checará as palavras digitadas
        print("VOCÊ PERDEU")
        break
    letra = input("DIGITE UMA LETRA:")

    if len(letra) > 1:
        print("ISSO NÃO VALE, DIGITE APENAS UMA LETRA!")
        continue

    digitadas.append(letra)

    if letra in secreto:
        print("A LETRA {} EXISTE NA PALAVRA SECRETA!".format(letra))
    else:
        print("A LETRA {} NÃO FAZ PARTE DA PALAVRA SECRETA!".format(letra))
        digitadas.pop() #aqui vai adicionar às letras digitas que não fazem
        #parte das letras corretas

    secreto_temporario = '' #é uma string vazia que vai receber os imputs
    #do usuário
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta # += ESTÁ CONCATENANDO, ele está
            #adicionando os valores que foram adicionados na string
        else:
            secreto_temporario += '*' #ocultando ela em asterisco caso
    if secreto_temporario == secreto:
        print("VOCÊ GANHOU O JOGUINHO! ACERTOU A PALAVRA")
        break
    else:
        print("VOCÊ NÃO GANHOU, A PALAVRA SECRETA É {}".format(secreto_temporario))

    if letra not in secreto: #so quer que isso aconteça caso o cara errar
        chances -= 1 #chances = chances -1
    print("VOCÊ AINDA TEM {} chances restantes".format(chances))
    print("*-"*5)
#RES# ULTADO DO JOGUINHO:
# DIGITE UMA LETRA:e
# A LETRA e EXISTE NA PALAVRA SECRETA!
# *e****e
# DIGITE UMA LETRA:r
# A LETRA r EXISTE NA PALAVRA SECRETA!
# *er***e
# DIGITE UMA LETRA:p
# A LETRA p EXISTE NA PALAVRA SECRETA!
# per***e
#então a cada letra ele vai adicionando ao jogo
