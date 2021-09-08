#AULA 10 DE PYTHON
#todo metodo tem um parenteses na frente como = .lower()
#estrutura sequencial - passo a passo
#ASSUNTO PRINCIPL - ESTRUTURA CONDICIONAL
# if e else

#1. PROGRAMA PARA MOSTRAR SE SEU CARRO É NOVO OU VELHO

tempo = int(input("DIGITE QUANTO TEMPO TEM SEU CARRO: "))

if tempo <= 3:
    print("SEU CARRO É NOVINHO")
else:
    print("SEU CARRO É VELHO")

#--------------------------------------------------------

#programa para identificar se o nome é ou nao aquele que a gente colocou na condicional IF

name = str(input("QUAL O SEU NOME: ")).upper()
if name == "RENATA":
    print("QUE NOME LINDO VOCÊ TEM, FOI UM PRAZER TE CONHECER RENATA!")
else:
    print("FOI UM PRAZER TE CONHECER {}".format(name))
print("TENHA UM BOM DIA, {}".format(name))

#--------------------------------------------------------
#programa para médias

grade1 = float(input("PLEASE TYPE YOUR FIRST GRADE: "))
grade2 = float(input("PLEASE TYPE YOUR SECOND GRADE: "))

grades_medium = (grade1 + grade2)/2

print("THE MEDIUM NUMBER OF YOUR TWO GRADES IS: {:.2} ".format(grades_medium))

if grades_medium >= 6:
    print("YOUR GRADE IS SATISFATORY")
else:
    print("YOUR GRADE IS NOT SATISFATORY AT ALL")

#--------------------------------------------------------DESAFIOS

#28. FAÇA UM PRAGRAMA QUE FAÇA O COMPUTADOR PENSAR INTEIRO ENTRE UM NUMERO DE 0 A 5
#FAÇA O USUARIO TENTAR ADIVINHAR QUAL O NUMERO ESCOLHIDO
#O PROGRAMA DEVERA ESCREVER NA TELA SE O USUARIO PERDEU OU NAO

import random 

number_x = random.randint(0, 5)
number = int(input("DIGITE UM NUMERO QUALQUER DE 0 A 5: "))

if number == number_x:
    print("VOCÊ ACERTOU O NUMERO :)")
else:
    print("VOCÊ NÃO ACERTOU O NUMERO. O NUMERO CORRETO É: {}".format(number_x))

#29. LER A VELOCIDADE DE UM CARRO. SE ULTRAPASSAR 80KM/H MOSTRAR UMA MENSAGEM DIZENDO QUE ELE FOI MULTADO
#A MULTA DEVE SER R$ 7,00 CADA KM ACIMA DO LIMITE

velocity = float(input("DIGITE A VELOCIDADE "))
fine = (velocity-80)*7

if velocity >= 80:
    print("VOCÊ RECEBEU UMA MULTA DE R${:.2f}".format(fine))
else:
    print("VOCÊ ESTÁ DENTRO DA VELOCIDADE, NÃO RECEBERÁ MULTA. BOA VIAGEM!")

#30. CRIE UM PROGRAMA QUE LEIA UM NUMERO INTEIRO E MOSTRE SE É PAR OU IMPAR

numero = int(input('DIGITE UM NUMERO INTEIRO: '))

if (numero%2) == 0:
    print("O NÚMERO É PAR")
else:
    print("O NUMERO É IMPAR")

#31. LER A VIAGEM EM KM , CALCULE O PREÇO DA PASSAGEM COBRANDO R$0,50 POR KM PARA VIAGENS DE ATÉ 200KM
#E 0,45 PARA VIAGENS MAIS LONGAS

km = float(input("DIGITE QUANTOS KM VOCÊ PERCORREU: "))
viagem_1 = km * 0.50
viagem_2 = km * 0.45

if km < 200:
    print("O VALOR DA VIAGEM SERÁ " , viagem_2)
else:
    print("O VALOR DA VIAGEM SERÁ " , viagem_1)

#32. FAÇA UM PROGRAMA QUE LEIA UM ANO QUALQUER E MOSTRE SE ELE OU NAO BISSEXTO

year = int(input("DIGITE UM ANO QUALQUER: ----"))

if year%4==0 and year%100!=0 or year%400==0:
    print("O ANO  É BISSEXTO!!")
else:
    print("O ANO NÃO É BISSEXTO!")

#33. LER 3 NUMEROS E MOSTRE QUAL É MAIOR E QUAL É O MENOR

num1 = int(input("DIGITE O PRIMEIRO NUMERO ----"))
num2 = int(input("DIGITE O SEGUNDO NUMERO ----"))
num3 = int(input("DIGITE O TERCEIRO NUMERO ----"))

lista = [num1, num2, num3]

print('O MAIOR NUMERO QUE VOCÊ DIGITOU FOI: {} '.format(max(lista)))
print('O MENOR NUMERO QUE VOCÊ DIGITOU FOI: {} '.format(min(lista)))

#34. LER O SALARIO DE UM FUNCIONARIO E CALCULE O VALOR DO SEU AUMENTO
#PARA SALARIOS SUPERIORES A 1250,00, CALCULE 10% DE AUMENTO. 
#PARA INFERIORES OU IGUAIS O AUMENTO É DE 15%

salario = float(input("DIGITE O SALARIO DO FUNCIONÁRIO ----R$ "))

calculo_superior = (salario * (10/100))+salario
calculo_inferior = (salario * (15/100))+salario

if salario > 1250.00:
    print("SEU SALARIO SERÁ AUMENTADO EM 10%", calculo_superior)
else:
    print("SEU SALARIO SERÁ AUMENTADO EM 15%", calculo_inferior)    

#35. ler o comprimento de 3 retas e diga ao usuário se elas podem ou nao formar um triangulo.

print("-="*20)
print("ANALISADOR DE TRIANGULOS")
print("-="*20)
a = float(input("DIGITE A PRIMEIRA MEDIDA DA RETA ----"))
b = float(input("DIGITE A SEGUNDA MEDIDA DA RETA ----"))
c = float(input("DIGITE A TERCEIRA MEDIDA DA RETA ----"))

calculo_1 = (b - c) < a < b + c
calculo_2 = (a - c) < b < a + c
calculo_3 = (a - c) < c < a + b

if (b - c) < a < b + c and (a - c) < b < a + c and (a - c) < c < a + b:
    print("OS VALORES ACIMA PODEM FORMAR UM TRANGULO :)")
else:
    print("OS VALORES DIGITADOS NÃO PODEM FORMAR UM TRIANGULO :(")

print("-="*20)
print("FIM!")
print("-="*20)
