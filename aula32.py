#USO DE f'' E .FORMAT
# :s - texto (strings)
#:d - inteiros (int) - DIGITO
#:f - numeros de ponto flutuante (float)
# :.(NUMERO CASAS DECIUMAIS)f - quantidade de casas decimais (float)
# :(caractere) (> ou < ou ^) (quantidade) tipo s, d ou f
# > - esquerda
# < - direita
# ^ - centro

# num1 = 10
# num2 = 3
# divisao = num1 / num2
#print('{:.2f}'.format(divisao)) #AQUI FOI ESCOLHIDO DUAS CASAS
#APOS A VIRGULA e f é o numero de ponto flutuante
# print(f'{divisao:.2f}')

#--- caso queira formatar uma string
num = 1
num2 = 2
print(f'{num:0>10}') #aqui queremos que o seja preenchido 10 numeros
#a esquerda de acordo com as regras acima do numero - no caso sairá:
#0000000001 - esse valor vai ter 10 casas de acordo com a formatação f'{num:0>10}
print(f'{num2:0<10}') #se eu coloco 10 de formatação a direita, então
# o total de casas serão 10, se eu colocar total 20, serão 20.

#---também tem a possibilidade de eu transformar o numero como float

print(f'{num2:0>10.2f}') # transformando o numero em float .2f duas casas decimais
#0000002.00

#também podemos usar com letras

#usando o ljust

nome = "RENATA MONTEIRO"
nome = nome.ljust(20, "#")
print(nome)
#SAI O SEGUINTE RESULTADO : RENATA MONTEIRO##### - ele completa
#com  # (porque eu pedi que fizesse assim até chegar aos 20 caracteres

#usado lower, upper e o title
print(nome.lower())
print(nome.upper())
print(nome.title())
#resultados:
# renata monteiro##### - lower - tudo minusculo
# RENATA MONTEIRO##### - upper - maisculo
# Renata Monteiro##### - Capitize letter somente a primeira de cada palavra
