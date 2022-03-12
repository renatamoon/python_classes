#34. While - estrutura de repetição em Python

# x = 0
# #estou inicializando as variaveis
# while x < 10:
#     y = 0
#     while y < 5: #enquanto y for menor a 5, esse laço funciona, depois quando
#         #chegar a 4, ainda funciona. Mas quando o y for maior
#         #maior que 5, ele faz a estrutura debaixo
#         print(f'X vale {x} e Y vale {y}')
#         y += 1 #que é a mesma coisa que dizer y = y + 1
#     x += 1 #x = x + 1
# print("ACABOU!")
#no caso esse laço while termina quando o x for menor que 10.

#-FAZENDO UMA CALCULADORA USANDO O WHILE

while True:
    print()
    num = input("DIGITE O NUMERO: ")
    num2 = input("DIGITE OUTRO NUMERO: ")
    operador = input("DIGITE QUAL OPERADOR [+ - * /]: ")

    if operador == "+":
        print("O RESULTADO É: "num + num2))
    elif operador == "-":
        print("O RESULTADO É: {}".format(num - num2))
    elif operador == "*":
        print("O RESULTADO É: {}".format(num * num2))
    else operador == "/":
        print("O RESULTADO É: {}".format(num/num2))