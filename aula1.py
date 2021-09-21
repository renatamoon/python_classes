#CONDICÕES
#WHILE PYTHON - AULA 7

# while True: #looping infinito
#     nome = input("QUAL O SEU NOME")
#     print("OLÁ, {}".format(nome))
#print("não será executada")

# x = 0   #para iniciar a var
# while x < 10:
#     if x == 3:
#         x = x +1
#         continue #sempre que tiver essa linha ele não executa o bloco de codigos
#         #caso o x for igual a 3
#
#     print(x)
#     x = x + 1
# print("ACABOU!")

#já a palavra break termina o loop, e ai acaba o codigo.

#---- outro exercicio
#
# x = 0
# y = 0

# x < 10:
        #     while y < 5:
#         print("X vale {} e Y vale".format(x, y))
#         y += 1
#     x += 1 #isso é basicamente igual ao x = x+1
# print("acabou")

#***CRIANDO UMA CALCULADORA

while True:
    print()
    num1 = input("DIGITE UM NUMERO: ")
    num2 = input("DIGITE OUTRO NUMERO: ")
    operador = input("DIGITE UM OPERADOR [+ - / *]: ")

    if not num1.isnumeric() or not num2.isnumeric(): #validação de numero para que
        #o usuário digite um numero e não um outro tipo de caracter
        print("você precisa digitar um numero")
        continue

    num1 = int(num1)
    num2 = int(num2)

    # + - / *
    if operador == "+":
        print("O RESULTADO É: ", num1 + num2)
    elif operador == "-":
        print("O RESULTADO É: ", num1 - num2)
    elif operador == "*":
        print("O RESULTADO É: ", num1 * num2)
    elif operador == "/":
        print("O RESULTADO É: ", num1 / num2)
    else:
        print("NÃO HÁ RETORNO PARA A OPERAÇÃO SOLICITADA")
