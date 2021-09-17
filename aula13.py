#LAÇOS DE REPETIÇÃO - PARTE 1 - FOR

# for c in range(0,3):
#   passo
#   pula
# passo
# pula

# for c in range(0,6):
#     print("OLÁ MUNDO! ")
# print("FIM")

#*****OUTRA FORMA

# n = int(input("DIGITE UM NUMERO QUALQUER: "))
# for c in range(0, n+1): #coloquei o +1 para que ele chegasse ao numero digitado no N
# #se colocar apenas apenas o N, ele printa até o numero anterior, então se o N valer 5, ele printa até o 4
#     print(c)
# print("FIM")

#OUTRO PROGRAMA PARA VER UTILIDADES

# inicio = int(input("NUMERO DE INICIO: "))
# final = int(input("NUMERO DE FINAL: "))
# passo = int(input("QUANTOS PASSOS: "))

# for c in range(inicio, final+1, passo):
#     print(c)
# print("FIM")

# soma = 0 #tem que iniciar a variavel aqui para que possamos chama-la depois
# for c in range(0, 10):
#     n = int(input("DIGITE O VALOR: "))
#     soma += n #SOMA TODOS OS VALORES COLOCADOS NA VAR N 
# print("A SOMA DE TODOS OS VALORES FOI {}".format(soma))

# numero = int(input("DIGITE UM NUMERO: "))

# for c in range(numero+1):
#     print(c)
# print("FINAL DO PROGRAMA")

#outro

# inicio = int(input("DIGITE O NUMERO INICIAL: "))
# final = int(input("DIGITE O NUMERO FINAL: "))
# pulo = int(input("DIGITE DE QUANTOS EM QUANTOS QUER PULAR: "))

# for c in range(inicio, final+1, pulo):
#     print(c)
# print("*FINAL DO PROGRAMA*")

#USANDO A SOMA COM O CONTADOR

# soma = 0
# for c in range (0, 5):
#     num = int(input("DIGITE UM NUMERO: ---"))
#     soma += num
# print("A SOMA DE TODOS OS NUMEROS É: {}".format(soma))

#----------DESAFIO 46
# FAÇA UM PROGRAMA QUE MOSTRE A CONTAGEM REGRESSIVA PARA O ESTOURO
# DE FOGOS DE ARTIFICIO, DE 10 ATÉ 0, COM PAUSA DE 1 SEGUNDO ENTRE ELES

# from time import sleep

# for c in range(-10, 0):    
#     sleep(1)
#     print(abs(c))
# print("-="*20)
# print("FOGOS ESTÃO ESTOURANDO")
# print("-="*20)

#----------DESAFIO 47
#FAÇA UM PRPGRAMA QUE MOSTRE NA TELA TODOS OS NUMEROS PARES QUE ESTÃO NO INTERVALO ENTRE 1 E 50

# impar = 0

# for c in range(0, 50+1):
#     if c % 2 == 0:
#         print(c)
#     else:
#         impar == 0
# print("-="*20)
# print("FIM DO PROGRAMA")
# print("-="*20)

#----------DESAFIO 48
#FAÇA UM PROGRAMA QUE CALCULE A SOMA DE TODOS OS NUMEROS IMPARES QUE SÃO MULTIPLOS DE 3 E QUE SE ENCONTRAM
#NO INTERVALO DE 1 A 500

# par = 0
# impar = 0
# soma = 0

# for c in range(0, 500+1):
#     if c % 2 != 0:
#         impar == c
#         if c % 3 == 0:
#             soma += c
#         else:
#             par == 0
#     else:
#         par == 0
# print("A soma de todos os valores é {} ".format(soma))
# print("-="*20)
# print("FIM DO PROGRAMA")
# print("-="*20)

#----------DESAFIO 49
#REFAÇA O EXERCICIO (009) DE TABUADA DE UM NUMERO QUE O USUARIO ESCOLHER, SO QUE AGORA UTILIZANDO
#UM LAÇO FOR

# from time import sleep

# numero = int(input('DIGITE UM NUMERO QUE MOSTRAREMOS A TABUADA: '))
# tabuada = 0

# for c in range (0,11):
#     tabuada = numero * c
#     print("{} x {} = {}".format(numero, c, tabuada))
#     sleep(1)
# print("****FIM DA TABUADA****")

#----------DESAFIO 50
#LER 6 NUMEROS INTEIROS E MOSTRE APENAS A SOMA DAQUELES QUE FOREM PARES, SE O VALOR DIGITADO
#SE O VALOR FOR IMPAR, DESCONSIDERAR E NÃO MOSTRAR A SOMA.

# soma = 0
# n = 0
# impar = 0

# for c in range(0, 6+1):
#     n = int(input("DIGITE UM NUMERO: "))
#     if n % 2 == 0:
#         soma += n
#     else:
#         impar = 0
# print("A SOMA DE TODOS OS VALORES PARES É {}".format(soma))        

#----------DESAFIO 51
#DESENVOLVA UM PROGRAMA QUE LEIA O PRIMEIRO TERMO E A RAZÃO DE UMA PA. NO
#FINAL, MOSTRE OS 10 PRIMEIROS TERMOS DESSA PROGRESSÃO.

# num1 = int(input("DIGITE O PRIMEIRO TERMO DA PROGRESSÃO ARITIMETICA: "))
# razao = int(input("DIGITE O VALOR DA RAZÃO DA PROGRESSÃO ARITIMETICA: "))
# enesimo = num1 + (10-1) * razao

# for c in range(num1, enesimo+1, razao):
#     print("{}".format(c), end=" *")
# print("*FINAL DA PROGRESSÃO*")
        
#----------DESAFIO 52
#FAÇA UM PROGRAMA QUE LEIA UM NUMERO INTEIRO E DIGA SE ELE É OU NÃO UM NUMERO
#PRIMO

# num1 = int(input("DIGITE UM NUMERO PARA VERIFICAR SE O NUMERO É PRIMO: "))
# multiplos = 0

# for c in range(2,num1):
#     if num1 % c == 0:
#         print("MULTIPLO DE ",c )
#         multiplos += 1
# if multiplos == 0:
#     print("O NUMERO {} É UM NUMERO PRIMO!".format(num1))
# else:
#     print("O NÚMERO {} NÃO É UM NUMERO PRIMO".format(num1))

#----------DESAFIO 53
#CRIE UM PROGRAMA QUE LEIA UMA FRASE QUALQUER E DIGA SE ELA É UM
#PALINDROMO, DESCONSIDERANDO OS ESPAÇOS ENTRE ELAS.
#EXEMPLO: APOS A SOPA
#A SACADA DA CASA
#A TORRE DA DERROTA
#ANOTARAM A DATA DA MARATONA
# O PROGRAMA DEVE SER CAPAZ DE RETIRAR OS ESPAÇOS

#---USANDO ESTRUTURA SEM FOR:

# frase = input("DIGITE UMA FRASE: ").strip().upper().replace(' ','')
# if frase == frase[::-1]:
#     print("A FRASE DIGITADA É UM PALINDROMO!")
# else:
#     print('A FRASE DIGITADA NÃO É UM PALINDROMO!')

#----USANDO LAÇO DE REPETIÇÃO FOR

# frase = input("DIGITE UMA FRASE/ FRASE: ").strip().upper()#tirando espaços, fazendo a frase
# #ficar em maiusculo
# palavras = frase.split() #splitei ela pra gerar uma lista
# junto = "".join(palavras) #juntei a lista para eliminar os espaços
# inverso = ""
# for letra in range(len(junto) -1, -1, -1):
#     inverso += junto[letra] #esse for foi usado para juntar tudo
# if inverso == junto[::-1]: #se o inverso é igual ao tudo junto
#     print("A FRASE É UM PALINDROMO :)")
# else:
#     print("A FRASE NÃO É UM PALINDROMO :(")
# print("A FRASE INVERSA TODA JUNTA É :\33[34m{}\33[m, E A FRASE INVERSA É \33[34m{}\33[m".format(junto, inverso))

#----------DESAFIO 54
#LER O ANO DE NASCIMENTO DE 7 PESSOAS. NO FINAL, MOSTRE QUANTAS PESSOAS
#AINDA NAO ATINGIRAM A MAIORIDADE E QUANTAS JÁ SÃO MAIORES.

maior_18 = 0
menor = 0

for ano in range(0, 8):
    ano_nascimento = int(input("INFORME SEU ANO DE NASCIMENTO"))
    maioridade = 2021 - ano_nascimento
if maioridade > 18:
    maioridade == maior_18
elif maioridade < 18:
    maioridade == menor
else:
    print("DESCONSIDERAR")    

#----------DESAFIO 55
#FAÇA UM PROGRAMA QUE LEIA O PESO DE CINCO PESSOAS.
#NO FINAL MOSTRE QUAL FOI O MAIOR E O MENOR PESO LIDOS.

#----------DESAFIO 56
#DESENVOLVA UM PROGRAMA QUE LEIA O NOME, IDADEM SEXO DE 4 PESSOAS.NO FINAL
#DO PROGRAMA MOSTRE:
#-A MEDIA DE IDADE DO GRUPO;
#-QUAL O NOME DO HOMEM MAIS VELHO;
#-QUANTAS MULHERES TEM MENOS DE 20 ANOS


