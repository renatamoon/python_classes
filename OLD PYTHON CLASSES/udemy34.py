'''while em Python - aula 7
Utilizado para realizar ações enquanto
uma condição for verdadeira
'''

while True:
    print()
    num = input("DIGITE UM NUMERO: ")
    num2 = input("DIGITE OUTRO NUMERO: ")
    operador = input("DIGITE O OPERADOR: + - * /: ")
    sair = input("DESEJA SAIR? [s]im ou [n]ão?")

    if sair == "s":
        break

    if not num.isnumeric() or not num2.isnumeric():
        print("VOCÊ PRECISA DIGITAR UM NUMERO")
        continue #ISSO FAZ COM QUE A FUNÇÃO CONTINUE
    #CASO o usuario continuar digitando valores que 
    #não são numericos, então ele continuará rodando esta função

    num = int(num) #transformando os numeros em inteiros
    num2 = int(num2)

    if operador == "+":
        print(num + num2)
    elif operador == '-':
        print(num - num2)
    elif operador == '*':
        print(num * num2)
    elif operador == '/':
        print(num / num2)
    else:
        print("operador não será lido")

