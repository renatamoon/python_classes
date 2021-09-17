#INDICES
#ITERAÇÃO SOBRE STRINGS
#nesse caso iremos usar o laço while para passar por cada
#elemeto dentro da string
# 012345789 ........ 34 (contamos o zero na programação)
frase = "o rato roeu a roupa do rei de roma"
tamanho = len(frase)

contador = 0
nova_string = ""

while contador < tamanho:
    print(frase[contador], contador)
    contador += 1 #contará até ele ser menor que zero
    nova_string += frase[contador] #copiou os elementos desta string

#--RESULTADO
# o 0
#   1
# r 2
# a 3
# t 4
# o 5
#   6
# r 7
# o 8
# e 9
# u 10
#   11
# a 12
#   13
# r 14
# o 15
# u 16
# p 17
# a 18
#   19
# d 20
# o 21
#   22
# r 23
# e 24
# i 25
#   26
# d 27
# e 28
#   29
# r 30
# o 31
# m 32
# a 33

#---substituição de dados dentro de strings

frase = "o rato roeu a roupa do rei de roma"
tamanho = len(frase)

contador = 0
nova_string = ""

input_do_usuario = input("QUAL LETRA QUER TROCAR PARA MAISCULO?--")

while contador < tamanho:
    letra = frase[contador]
    if letra == input_do_usuario:
        nova_string += input_do_usuario.upper() #substitui a letra minuscula
        #pela maiuscula
    else:
        nova_string += letra
    contador += 1
print(nova_string)

# RESULTADO da função: o Rato Roeu a Roupa do Rei de Roma

#outros resultados: 
# QUAL LETRA QUER TROCAR PARA MAISCULO?--e
# o rato roEu a roupa do rEi dE roma