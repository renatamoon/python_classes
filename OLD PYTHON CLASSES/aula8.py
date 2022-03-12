#AULA 8 DE PYTHON - IMPORTAÇÃO DE MODULOS
#IMPORTAÇÃO DE BIBLIOTECAS

import math

num = int(input("Digite um numero: "))
sqrt = math.sqrt(num)

print("A resposta da raiz do numero {} é igual a {}".format(num, math.ceil(sqrt)))

#usando o "".format(num, math.ceil(sqrt)"" esse math.ceil é usado para arredondar as casas.
#mas também pode ser usado a seguinte formatação dentro das chaves que você quer arredondar: {:.2f} - tanto faz qual a formatação

#USANDO A IMPORTAÇÃO DA BIBLIOTECA DE MATEMATICA DA RAIZ QUADRADA

from math import floor, sqrt  #aqui importou a biblioteca de arredondamento p baixo + raiz quadrada

num = int(input("Digite um numero: "))
raiz = sqrt(num) #nesse caso nao precisa usar a função math.sqrt - somente usar sqrt que ele já sabe que você importou 
# #esse modulo
print("A resposta da raiz do numero {} é igual a {}".format(num, floor(raiz))) #floor arredonda para baixo

#acessando o python.org - acessando a parte de documentação você consegue encontrar quais bibliotecas disponiveis para usar

#acessando a biblioteca random - voocê consegue achar numeros aleatorios

import random #essa classe random gera um numero aleatorio entre 0 e 1 - no caso um numero float
num = random.randint(1, 20) #nesse caso colocando esse RANDINT - gera um numero INTEIRO entre 1 e 20
print(num)

#-------------------DESAFIOS

#16 - crie um programa que leia um numero real qualquer no teclado e mostre a sua porção inteira.
#ex: digite um numero 6.127 - a parte inteira é 6

num = float(input("DIGITE UM NUMERO REAL (DO TIPO FLOAT): "))
conversao = int(num)

print(conversao)


#17 - faça um programa que leia o comprimento do cateto oposto e do cateto 
# adjacente de um triangulo retangulo
#calcule e mostre o comprimento da hipotenusa

#18 - faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, 
# cosseno e tangente desse angulo

comp_cateto_oposto = int(input("DIGITE O CUMPRIMENTO DO CATETO OPOSTO: "))
comp_cateto_adjacente = int(input("DIGITE O CUMPRIMENTO DO CATETO ADJACENTE: "))

hipotenusa = comp_cateto_oposto + comp_cateto_adjacente
cosceno = comp_cateto_adjacente / hipotenusa
seno = comp_cateto_oposto / hipotenusa
tangente = seno / cosceno

print("O COMPRIMENTO DA HIPOTENUSA É: " ,hipotenusa)
print("O valor do cosceno é {:.2f}, e o valor do seno é {:.2f}, e o valor da tangente é {:.1f}".format (cosceno, seno, tangente))

#19 - um professor quer sortear um dos seus alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escrevendo
#o nome escolhido

import random

lista_alunos = ["renato", "rafael", "ricardo", "lucas"]
num = ""


while num != "rafael":
   num = random.choice(lista_alunos)
print(num)

#--------------OUTRA FORMA DE FAZER

import random

alunos  =["RENATO", "RAFAEL", "RICARDO", "LUCAS"]
escolhido = random.choice(alunos)

print("O ALUNO ESCOLHIDO FOI: {}".format(escolhido))
#escolhe uma opção dentro de uma fonte


#20 - o mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos
#faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random
from random import shuffle

alunos  =["RENATO", "RAFAEL", "RICARDO", "LUCAS"]
random.shuffle(alunos)

print("A ORDEM DE APRESENTAÇÃO SERÁ: {}".format(alunos))


