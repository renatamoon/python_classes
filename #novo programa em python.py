#primeiros comandos em python

#passos simples no python

print("Olá, Mundo")
print(7+4)

# USANDO VARIÁVEIS

name = "Renata"
idade = 25
peso = 58.0
print(name, idade, peso)

nome = input("Qual é seu nome? ")
idade = input ("Quantos anos você tem?")
peso = input ("Qual é o seu peso?")

print(nome, idade,peso)


#------------------desafio 1
#script que leia o nome da pessoa e mostra uma mensagem de boas
#vindas de acordo com o valor digitado.

nome = input("Qual é o seu nome? ")
print("Boas vindas senhor(a)" ,nome)

#------------------desafio 2
#crie um script que leia o dia, o mes e o ano de nascimento
#de uma pessoa e mostre uma mensagem com a data formatada

dia = input("Qual o dia que você nasceu? ")
mes = input("Qual o mês que você nasceu? ")
ano = input("Qual o ano que você nasceu? ")

#print("O seu dia de nascimento formatado é " ,dia + " de" ,mes +" de" ,ano)

#------------------desafio 3
#crie um script que leia dois numeros e tente mostrar a
#a soma entre eles

num1 = input("Digite um numero ")
num2 = input("Digite outro numero ")
soma = int(num1) + int(num2)

print("A soma dos numeros é" ,soma)