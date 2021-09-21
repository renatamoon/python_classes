#PROGRAMA PARA GERAR CPF E VALIDAR O CPF DEPOIS

from random import randint
numero = str(randint(100000000, 999999999))

novo_cpf = numero#retirando os 2 ultimos numeros do cpf
reverso = 10
total = 0

for index in range(19):#19 é o numero de vezes que o for tem que fazer a volta para
    #cacular todos os valores
    if index > 8:   #primeiro indice vai de 0 a 9
        index -= 9     #no caso são 9 primeiros digitos do cpf
    #to chamando a var de index pois o index equivale a cada
        #valor de cada caractere do cpf
    total += int(novo_cpf[index]) * reverso #acessando o cpf do novo index

    reverso -= 1  # decrementando cada valor do valor reverso
    if reverso < 2:
        reverso = 11
        digito = 11 - (total % 11)

        if digito > 9:
            digito = 0
        total = 0 #tem que zerar a var para que depois ele for fazer outra
        #volta ele precisa zerar a variável total
        novo_cpf += str(digito) #pois ele tá como inteiro, então precisamos
        #tranformá-lo em string
print(novo_cpf)