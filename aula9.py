#CADEIA DE CARACTERES
#MANIPULAÇÃO DE STRINGS
#MANIPULAÇÃO DE CADEAIA DE TEXTOS
#fateamento de caracteres

# print("""Essa é só uma entre as dezenas de notícias falsas sobre
#  tratamentos para Covid-19 que circulam nas mídias sociais
#   do país — incluindo uma que defende a nebulização com 
#   hidroxicloroquina, a nova obsessão de Bolsonaro. Mais 
#   de um ano após o início da pandemia, as fake news
#    ainda proliferam""") #dando um aspas tripla conseguimos colocar todo uma cadeia de
#    #caracteres juntos

#len = comprimento - qual o cumprimento da frase

#len(frase)
#frase.count("o") - #contar quantas vezes aparece a letra "o"
#frase.count("o",0,13) - considerando a posição do 0-12 e fala quantas vezes aparece o "o" do 0 ao 12
#frase.find("deo") - mostra a posição em que o "deo" está na frase
#podemos ursar a funcionalidade "in" - "Curso" in frase (frase é a variável onde está alocada a frase inteira)

#TRANSFORMAÇÃO

#frase.replace("python", "android")

#.upper() - fica em maiusculo
#.lower() - mantem o que é minusculo e transforma o que é maiusculo em minusculo
#.capitalize() - joga todos os caracteres em minusculo e as primeiras letras em MAISCULO
#.title() - analisa os caracteres vazios e transforma as primeiras letras depois do espaço em maiusculo
#.strip() - caso tenha caracteres vazios no inicio ou no fim, ele corta esses caracteres
#.rstrip() - remove espaços no final da frase do caractere
#.lstrip() - remover os caracteres a esquerda e deixa os a direita

#DIVISAO - FUNCIONALIDADES

#.sṕlit() - onde tiver espaço ele cria uma divisão
# "-".join(frase) - onde tiver na frase um espaço ele vai incluir esse "-" para juntar a frase

#PARTE PRATICAS

frase = "NOVO PROJETO DE PYTHON SOMENTE HOJE"

print(frase[3:9]) #mostra do caractere 3 até a 8
print(frase[2:13:2])
print(frase.count("O")) #NO TERMINAL MOSTRA QUE TEM O "O" APARECE 7 VEZES
print(len(frase)) #sai que tem 35 caracteres
print(frase.replace("PYTHON", "ANDROID"))

#UMA STRING É IMUTÁVEL

#FUNÇÕES DE VERIFICAÇÃO


frase = "NOVO PROJETO DE PYTHON SOMENTE HOJE"
print("CURSO" in frase) #terminal mostra FALSE - porque não existe curso na frase
print(frase.lower().find("projeto")) #no terminal mostra 5 - porque começa no caractere numero 5
print(frase.split()) #no terminal sai: ['NOVO', 'PROJETO, 'DE' ...]

dividir = frase.split()
print(dividir[1]) #saiu o segundo item da lista que é o PROJETO pois o numero 1 é o segundo item da lista
print(dividir[1] [3]) #saiu o terceiro caractere "J" (no caso o 4 porque os caracteres começam pelo 0


#-----------DESAFIOS

#22 - CRIE UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSAO E MOSTRE:
#-O NOME COM TODAS AS LETRAS MAIUSCULAS
#-O NOME COM TODAS AS MINUSCULAS
#-QUANTAS LETRAS AO TODO (SEM CONSIDERAR ESPAÇOS)

nome = input(str("digite seu nome inteiro: ")) #n projects/aula9.py"
# DIGITE SEU NOME COMPLETO: renata cardoso monteiro
# O PRIMEIRO NOME INSERIDO É O:  RENATA CARDOSO MONTEIR

print(nome.upper())
print(nome.lower())
print(nome.__len__())

#QUANTAS LETRAS TEM O PRIMEIRO NOME

primeiro_nome = input(str("digite seu primeiro nome: "))
print(primeiro_nome.__len__())


#23 - FAÇA UM PROGRAMA QUE LEIA UM NUMERO DE 0 A 9999 E MOSTRE CADA UM DOS DIGITOS SEPARADOS
#EX: DIGITE UM NUMERO: 1834
#UNIDADE: 4
#DEZENA: 3
#CENTENA: 8
#MILHAR: 1

numero = int(input("INFORME UM NUMERO: "))
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar =  numero // 1000 % 10

print("Analisando o número {}".format(numero))
print("UNIDADE: {}".format(unidade))
print("DEZENA: {}".format(dezena))
print("CENTENA: {}".format(centena))
print("MILHAR: {}".format(milhar))

#24 - CRIE UM PROGRAMA QUE LEIA O NOME DE UMA CIDADE E DIGA SE ELA COMEÇA OU NAO COM NOME "SANTO"

name = str(input("DIGITE O NOME DE UMA CIDADE: "))
cont = name.count("santo")
print("Quantas vezes aparece o nome SANTO: ", cont)


#25 - CRIE UM PROGRAMA QUE LEIA O NOME DE UMA PESSOA E DIGA SE ELA TEM "SILVA" NO NOME

nome_completo = str(input("DIGITE SEU NOME COMPLETO (em minúsculo)): "))
cont = nome_completo.count("silva")
print("Quantas vezes aparece o nome SILVA: ", cont)

#26 - FAÇA UM PROGRAMA QUE LEIA UMA FRASE PELO TECLADO E MOSTRE:
#-QUANTAS VEZES APARECE A LETRA A
#-EM QUE POSIÇÃO ELA APARECE A PRIMEIRA VEZ
#-EM QUE POSIÇÃO ELA APARECE A ULTIMA VEZ

phrase = str(input("DIGITE UMA FRASE: ")).lower()
a = phrase.count("a")

print("Quantas vezes aparece a LETRA A: ", a)
print("A letra A aparece quantas vezes? Resposta: " ,phrase.find("a"))
print("Em que posição a letra A aparece pela ultima vez? Resposta: " ,phrase.rfind("a")) 

#27 - FAÇA UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA, MOSTRANDO EM SEGUIDA O PRIMEIRO E O ULTIMO NOME
#SEPARADAMENTE.
#EX: ANA MARIA DE SOUZA
#PRIMEIRO: ANA
#ULTIMO: SOUZA

name_and_surname = str(input("DIGITE SEU NOME COMPLETO: ")).strip()
name = name_and_surname.split()

print("Olá!")
print("Seu primeiro nome é: {}".format(name[0]))
print("Seu ultimo nome é: {}".format(name[len(name)-1]))





















