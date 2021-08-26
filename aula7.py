#AULA 7 - OPERADORES ARITIMETICOS

# algumas dicas para divisão e multiplicação

# ** usado para multiplicação
# // divisão inteira
# / divisão normal, divisão ReadableBuffer

#consegue-se também fazer multiplicaçãod
#de strings

nome = input("Qual é o seu nome? ")
print("Prazer em te conhecer {:>20}!" .format(nome))
#o >20 alinha o espaçamento a direito com 20 caracteres

#quer ler dois numeros 

n1 = int(input("Um valor: "))
n2 = int(input("Outro valor: "))

print("A soma vale {}" .format(n1+n2))

#Você pode também criar uma variável pra soma
s = n1 + n2

#outra forma de fazer

n1 = int(input("Um valor: "))
n2 = int(input("Outro valor: "))

s = n1 + n2
m = n1 + n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print("A soma é {}, \n o produto é {} e a \n divisão é {:.3f}" .format(s, m, d), end=' ')
print("A divisão inteira {} e potência {}" .format(di, e ))

#formatando um valor para deixar com apenas 2 casas ou mais
#somente colocar dentro da formatação {:.3f} - no caso
#isso significa 3 casas formatadas dentro do campo
#que você escolher formatar. No caso formataremos
#os campos da divisão.
#para quebrar uma linha, somente colocar um \n que quebra
# a linha do codigo que sairá no terminal

#---------------DESAFIOS dessa aula

#faça um programa que leia um numero inteiro e mostre
# n tela seu sucessor e antecessor

num1 = int(input("DIGITE UM NUMERO: "))
suc = num1 + 1
antec = num1 - 1
print("O sucessor do numero digitado é {} e o antecessor é {}".format(suc,antec))

#crie um algoritimo que leia um numero e mostre o seu dobro
# o triplo e a raiz quadrada.

import math

num = float(input("DIGITE QUALQUER NUMERO: "))
dobro = num*2
triplo = num*3
raiz = float(math.sqrt(num))

print("O resultado das operações: DOBRO tem resultado {}, TRIPLO tem resultado {} e RAIZ tem resultado {}".format(dobro,triplo,raiz))

#DESENVOLVA UM PROGRAMA QUE LEIAS AS DUAS NOTAS DE UM
#ALUNO , CALCULE E MOSTRE SUA MÉDIA

nota1 = float(input("DIGITE A SUA PRIMEIRA NOTA: "))
nota2 = float(input("DIGITE A SUA SEGUNDA NOTA: "))

media = ((nota1 + nota2)/2)
print("A SUA MÉDIA ATUAL É: " , media)

#ESCREVA UM PROGRAMA QUE LEIA UM VALOR EM METRO
#E O CONVERTA EM CENTRIMETROS E MILIMETROS

valor_metro = float(input("DIGITE UM VALOR: " ))
cent = valor_metro * 100
milim = valor_metro * 1000

print("O VALOR CONVERTIDO DE METRO PARA CENTIMETRO É {} E PARA MILIMETRO É {}".format(cent, milim))

#CRIE UM PROGRAMA  QUE LEIA QUANTO DINHEIRO UMA PESSOA
#TEM NA CARTEIRA E MOSTRE QUANTOS DOLARES ELA PODE COMPRAR
#CONSIDERE: USD 1,00 = USD 3,27

valor = float(input("DIGITE QUANTO DESEJA CONVERTER PARA DÓLAR: R$ "))
dolar = float(3.27)
conv_dolar = valor * dolar

print(conv_dolar)

#FAÇA UM PROGRAMA QUE LEIA A LARGURA E A ALTURA
#DE UMA PAREDE EM METROS. CALCULE A SUA ÁREA E A QUANTIDADE
#DE TINTA NECESSÁRIA PARA PINTA-LA. SABENDO QUE CADA
#LITRO DE TINTA PINTA UMA ÁREA DE 2M2.

largura = float(input("DIGITE A LARGURA: "))
altura = float(input("DIGITE A ALTURA: "))

area = largura * altura
qnt_tinta = area / 2

print("Para a aérea informada de {} será necessário {} latas de tinta".format(area,qnt_tinta))


