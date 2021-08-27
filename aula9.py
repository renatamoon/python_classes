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

# frase = "NOVO PROJETO DE PYTHON SOMENTE HOJE"
#print(frase[3:9]) - #mostra do caractere 3 até a 8
# print(frase[2:13:2])
# print(frase.count("O")) #NO TERMINAL MOSTRA QUE TEM O "O" APARECE 7 VEZES
# print(len(frase)) #sai que tem 35 caracteres
# print(frase.replace("PYTHON", "ANDROID"))
# #UMA STRING É IMUTÁVEL

#FUNÇÕES DE VERIFICAÇÃO


# frase = "NOVO PROJETO DE PYTHON SOMENTE HOJE"
# print("CURSO" in frase) #terminal mostra FALSE - porque não existe curso na frase
# print(frase.lower().find("projeto")) #no terminal mostra 5 - porque começa no caractere numero 5
# print(frase.split()) #no terminal sai: ['NOVO', 'PROJETO, 'DE' ...]

# dividir = frase.split()
# print(dividir[1]) #saiu o segundo item da lista que é o PROJETO pois o numero 1 é o segundo item da lista
# print(dividir[1] [3]) #saiu o terceiro caractere "J" (no caso o 4 porque os caracteres começam pelo 0


#-----------DESAFIOS

#22 - CRIE UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSAO E MOSTRE:
#-O NOME COM TODAS AS LETRAS MAIUSCULAS
#-O NOME COM TODAS AS MINUSCULAS
#-QUANTAS LETRAS AO TODO (SEM CONSIDERAR ESPAÇOS)
#QUANTAS LETRAS TEM O PRIMEIRO NOME

#23 - FAÇA UM PROGRAMA QUE LEIA UM NUMERO DE 0 A 9999 E MOSTRE CADA UM DOS DIGITOS SEPARADOS
#EX: DIGITE UM NUMERO: 1834
#UNIDADE: 4
#DEZENA: 3
#CENTENA: 8
#MILHAR: 1

#24 - CRIE UM PROGRAMA QUE LEIA O NOEM DE UMA CIDADE E DIGA SE ELA COMEÇA OU NAO COM NOME "SANTO"

#25 - CRIE UM PROGRAMA QUE LEIA O NOME DE UMA PESSOA E DIGA SE ELA TEM "SILVA" NO NOME

#26 - FAÇA UM PROGRAMA QUE LEIA UMA FRASE PELO TECLADO E MOSTRE:
#-QUANTAS VEZES APARECE A LETRA A
#-EM QUE POSIÇÃO ELA APARECE A PRIMEIRA VEZ
#-EM QUE POSIÇÃO ELA APARECE A ULTIMA VEZ

#27 - FAÇA UM PROGRAMA QUE LEIA O NOEM COMPLETO DE UMA PESSOA, MOSTRANDO EM SEGUIDA O PRIMEIRO E O ULTIMO NOME
#SEPARADAMENTE.
#EX: ANA MARIA DE SOUZA
#PRIMEIRO: ANA
#ULTIMO: SOUZA

















