#CONDIÇÕES NINHADAS
#ESTRUTRAS COLOCANDO UMA DENTRO DA OUTRA
#COLOCAR ESTRUTURAS CONDICIONAIS DENTRO DE ESTRUTURAS CONDICIONAIS

#so pra dizer que:
#IF é a primeira condição,
#ELIF é outra condição se a primeira não foi atendida
#outros elifs são pra outras condições

#pode ter um IF, e muitos elifs, e nenhum else, mas sempre tem que ter IF

# print("-="*20)
# nome = str(input("DIGITE SEU NOME: ")).upper()

# if nome == "GUSTAVO":
#     print("VOCÊ TEM UM BONITO NOME")
# else:
#     print("LHE DESEJO UM BOM DIA {}".format(nome))

#OUTRO EXEMPLO PARA PRATICA

# print("-="*20)
# nome = str(input("DIGITE SEU NOME: ")).upper()
# print("-="*20)

# if nome == "RENATA":
#     print("ESSE É O NOME DA PROGRAMADORA QUE ESTA FAZENDO ESSE PROGRAMA!")
# elif nome == "PEDRO":
#     print("VOCÊ FARÁ ANIVERSÁRIO SEMANA QUE VEM")
# elif nome == "RAFAEL" or nome == "\33[30;45mRICARDO":
#     print("ESSE É O NOME DOS IRMÃOS DA PROGRAMADORA RENATA")
# elif nome == "VICTORIA" or nome == "ANIELLY":
#     print("ESSE É O NOME DE UMA AMIGA DA PROGRAMADORA")
# else:
#     print("SEU NOME É NORMAL \33[30;45m{}, TENHA UM BOM DIA!!!\33[m".format(nome))


#-----------DESAFIO 36
#Aprova um emprestimo bancario para compra de uma casa. Perguntar valor da casa, o salario do comprador e em
#quantos anos ele vai pagar
#calcule o valor da prestação mensal, sabendo que ela nao pode exceder 30% do salario ou então o valor
#do emprestimo será negado

# print("="*20)
# salario = float(input("DIGITE SEU SALARIO: ---R$ "))
# valor_casa = float(input("DIGITE O VALOR DA CASA QUE QUER COMPRAR: ---R$ "))
# anos = int(input("DIGITE EM QUANTOS ANOS QUER PAGAR: ---"))
# print("="*20)

# prestacao_mensal = valor_casa / (anos*12)
# salario_minimo = salario * (30/100)

# if prestacao_mensal > salario_minimo:
#     print("\33[41mINFELIZMENTE SEU EMPRESTIMO FOI NEGADO\33[m")
# else:
#     print("\33[34m SEU EMPRESTIMO FOI APROVADO\33[m. CONTATE UM DE NOSSOS AGENTES")

#-----------DESAFIO 37
#Lee um numero inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
#1 para BINARIO
#2 PARA OCTAL
#3 PARA HEXADECIMAL

# print("*"*20)
# num = int(input("DIGITE UM NUMERO QUALQUER: "))
# print("*"*20)
# if num == 1:
#     print("A BASE DE CONVERSÃO SERÁ BINARIO!")
# elif num == 2:
#     print("A BASE DE CONVERSÃO SERÁ OCTAL!")
# elif num == 3:
#     print("A BASE DE CONVERSÃO SERÁ HEXADECIMAL!")
# else:
#     print("O VALOR DIGITADO NÃO SERÁ CONVERTIDO!")

#-----------DESAFIO 38
#ler dois numeros inteiros e comparar mostrando na tela:
#O PRIMEIRO VALOR É MAIOR
#O SEGUNDO VALOR É MENOR
#NAO EXISTE VALOR MAIOR, OS DOIS SÃO IGUAIS

# num1 = int(input("DIGITE O PRIMEIRO NUMERO ----"))
# num2 = int(input("DIGITE O SEGUNDO NUMERO ----"))

# if num1 > num2:
#     print("O MAIOR NUMERO É" ,num1)
# elif num2 > num1:
#     print("O MAIOR NUMERO É" ,num2)
# elif num1 == num2:
#     print("OS DOIS VALORES SÃO IGUAIS")

#-----------DESAFIO 39
#LER O ANO DE NASCIMENTO DE UM JOVEM E INFORME DE ACORDO COM A SUA IDADE:
#SE ELE VAI SE ALISTAR PARA O SERVIÇO MILITAR
#SE É HORA DELE SE ALISTAR
#SE JÁ PASSOU DO TEMPO DE ALISTAMENTO
#MOSTRAR TAMBÉM O TEMPO QUE FALTA OU QUE JÁ PASSOU DO PRAZO

# ano_nascimento = int(input("O ANO DE NASCIMENTO DO JOVEM:---- "))

# vai_alistar = 2003 - ano_nascimento
# passou_alistamento = ano_nascimento - 2003

# if ano_nascimento < 2003:
#     print("VOCÊ VAI SE ALISTAR AO SERVIÇO MILITAR? FALTA {} ANO(s) PARA VOCÊ SE ALISTAR!".format(vai_alistar))
# elif ano_nascimento == 2003:
#     print("JÁ É HORA DE SE ALISTAR AO SERVIÇO MILITAR!!")
# elif ano_nascimento > 2003:
#     print("JÁ PASSOU DA HORA DE VOCÊ SE ALISTAR! JÁ PASSOU {} ANO(S) DA FASE DE ALISTAMENTO!".format(passou_alistamento))

#-----------DESAFIO 40
#LER DUAS NOTAS DE UM ALUNO E CALCULE SUA MEDIA MOSTRANDO A MENSAGEM NO
#FINAL DE ACORDO COM A MEDIA ATINGIDA
#-MEDIA ABAIXO DE 5.0 = REPROVADO
#-MEDIA ENTRE 5 A 6,9: RECUPERAÇÃO
#-MEDIA 7 OU SUPERIOR: APROVADO

# nota1 = float(input("DIGITE A PRIMEIRA NOTA: --- "))
# nota2 = float(input("DIGITE A SEGUNDA NOTA: --- "))

# media = (nota1 + nota2) / 2

# if media <= 5:
#     print("VOCÊ FOI REPROVADO")
# elif media > 5 and media <=5.9:
#     print("VOCÊ ESTÁ DE RECUPERAÇÃO")
# elif media >= 7:
#     print("VOCÊ FOI APROVADO")

#-----------DESAFIO 41
#CONFEDERAÇÃO NACIONAL DE NATAÇÃO PRECISA DE UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE UM ATLETA E MOSTRE
#A SUA CATEGORIA DE ACORDO COM A IDADE:
#-ATÉ 9 ANOS - MIRIM
#-ATÉ 14: INFANTIL
#-ATÉ 19 ANOS: JUNIOR
#-ATÉ 20 ANOS: SENIOR
#ACIMA: MASTER

# ano_nascimento = int(input("DIGITE O SEU ANO DE NASCIMENTO ----: "))
# ano_atual = 2021

# idade = ano_atual - ano_nascimento

# if idade <= 9:
#     print("VOCÊ É DA CATEGORIA MIRIM")
# elif idade > 10 and idade <= 14:
#     print("VOCÊ É DA CATEGORIA INFANTIL")
# elif idade > 14 and idade <= 19:
#     print("VOCÊ É DA CATEGORIA JUNIOR")
# elif idade > 19 and idade <= 20:
#     print("VOCÊ É DA CATEGORIA MASTER")
# else:
#     print("VOCÊ É CATEGORIA MASTER")

#-----------DESAFIO 42
#ACRESCENTAR:
#REFAZER O EXERCICIO 35 DOS TRIANGULOS
# EQUILATERO, TODOS OS LADOS IGUAIS
#ISOCELES - DOIS LADOS IGUAIS
#ESCALENO - TODOS OS LADOS DIFERENTES

# print("-="*20)
# print("ANALISADOR DE TRIANGULOS")
# print("-="*20)

# a = int(input("DIGITE A PRIMEIRA MEDIDA DA RETA ----"))
# b = int(input("DIGITE A SEGUNDA MEDIDA DA RETA ----"))
# c = int(input("DIGITE A TERCEIRA MEDIDA DA RETA ----"))

# if a == b == c:
#     print("ESSE TRIANGULO É EQUILÁTERO!")
# elif a == b != c or a != b == c or a == c != b: 
#     print("ESSE TRIANGULO É ISOSCELES!")
# elif a != b != c:
#     print("ESSE TRIANGULO É ESCALENO")

# print("-="*20)
# print("FIM!")
# print("-="*20)

#-----------DESAFIO 43
#DESENVOLVA UMA LOFICA QUE LEIA O PESO, ALTURA DE UMA PESSOA, E CALCULE SEU IMC, E MOSTRE SUE STATUS
#DE ACORDO COM:
#-ABAIXO DE 18.5 = ABAIXO DO PESO
#-ENTRE 18.5 E 25 = PESO IDEAL
#-25 ATE 30: SOBREPESO
#-30 A 40: OBESIDADE
#ACIMA DE 40: OBESIDADE MORBIDA

# peso = float(input("DIGITE O SEU PESO EM KGS: "))
# altura = float(input("DIGITE O SEU ALTURA (COM PONTO X.XX): "))

# imc = peso / (altura*2)

# if imc < 18.5:
#     print("VOCÊ ESTÁ ABAIXO DO PESO IDEAL")
# elif imc > 18.5 and imc < 25:
#     print("VOCÊ ESTÁ NO PESO IDEAL")
# elif imc > 25 and imc < 30:
#     print("VOCÊ ESTÁ NO SOBREPESO")
# elif imc > 40:
#     print("VOCÊ ESTÁ COM OBESIDADE MORBIDA")

#----------DESAFIO 44
#CALCULE O VALOR A SER PAGO POR UM PRODUTO, CONSIDERANDO O SEU PRAÇO NORMAL E CONDIÇÃO DE PAGAMENTO
#A VISTA DINHEIRO/CHEQUE: 10% DE DESCONTO
#A VISTA NO CARTÃO: 5% DE DESCONTO
#EN ATÉ 2X NO CARTAO: PREÇO NORMAL
#3X OU MAIS: 20% DE JUROS INCLUSOS

# valor_produto = float(input("QUAL O VALOR PAGO NO PRODUTO? R$ "))
# forma_pagamento = int(input("QUAL A FORMA DE PAGAMENTO?(1)A VISTA, (2)A VISTA CARTÃO, (3)2 VEZES OU (4)3 VEZES OU MAIS:----- "))

# a_vista = valor_produto - (valor_produto * (10/100))
# a_vista_cartao = valor_produto - (valor_produto * (5/100))
# tres_vezes = valor_produto + (valor_produto * (20/100))

# if forma_pagamento == 1:
#     print("O VALOR A SER PAGO SERÁ: R$ {} E COM DESCONTO DE 10%".format(a_vista))
# elif forma_pagamento == 2:
#     print("O VALOR A SER PAGO SERÁ: R$ {} E COM DESCONTO DE 5%".format(a_vista_cartao))
# elif forma_pagamento == 3:
#     print("O VALOR A SER PAGO SERÁ: R$ {} SEM DESCONTO")
# elif forma_pagamento == 4:
#     print("O VALOR A SER PAGO SERÁ: R$ {} E COM ACRESCIMO DE 20%".format(tres_vezes))

# print("-="*20)
# print("OBRIGADA POR COMPRAR CONOSCO NAS LOJAS DO BEM!")
# print("-="*20)

#--------DESAFIO 45: CRIE UM PROGRAMA QUE FAÇA O COMPUTADOR JOGAR JOKEMPÔ COM VOCÊ.

from random import randint
from time import sleep

itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)
print('''PARA JOGAR ESSE JOGO VOCÊ TEM AS SEGUINTES OPÇÕES:
-PEDRA [0]
-PAPEL [1]
-TESOURA [2]''')
print("QUAL VOCÊ VAI ESCOLHER? ---- ")
sleep(1)
jogador = int(input("VAI JOGAR O QUE? ---"))
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!! VAI!!")
print("***"*10)
print("O COMPUTADOR JOGOU {} ".format(itens[computador]))
print("O JOGADOR JOGOU {}".format(itens[jogador]))
print("***"*10)

if computador == 0: #COMPUTADOR JOGOU PEDRA
    if jogador == 0:
        print("FOI UM EMPATE")
    elif jogador == 1:
        print("\33[41m O COMPUTADOR GANHOU!!!\33[m")
    elif jogador == 2:
        print("\33[41m O COMPUTADOR GANHOU!!!\33[m!")
    else:
        print("JOGADA INVALIDA!")
elif computador == 1: #COMPUTADOR JOGOU PAPEL
    if jogador == 0:
        print("O JOGADOR GANHOU!")
    elif jogador == 1:
        print("FOI UM EMPATE!")
    elif jogador == 2:
        print("O JOGADOR GANHOU!")
    else:
        print("JOGADA INVALIDA!")
elif computador == 2: #COMPUTADOR JOGOU TESOURA
    if jogador == 0:
        print("O JOGADOR GANHOU!")
    elif jogador == 1:
        print("\33[41m O COMPUTADOR GANHOU!!!\33[m")
    elif jogador == 2:
        print("FOI UM EMPATE!")
    else:
        print("JOGADA INVALIDA!")
print("***"*10)
sleep(1)
print("OBRIGADA POR JOGAR!")
print("***"*10)