#1 - crie uma função que exibe a palavra saudação com os parametros - saudação e nome

# nome = str(input("DIGITE SEU NOME: "))
#
# def saudacao ():
#     return "Olá a todos", nome
# print(saudacao())

#2 - crie uma função que receba 3 numeros como parameteos, e exiba a soma entre eles

# def soma(num1, num2, num3):
#     return num1 + num2 + num3
#
# print(soma(2,3,4))

#3 crie uma função que receba 2 numeros.
#o primeiro valor é um valor, segundo é um percentual. Retorne (return) o primeiro numero somado
#ao aumento % do mesmo.

# def valor_percentual (num, percentual):
#     return num + (num * (percentual/100))
#
# print(valor_percentual(500,10))

#4 - fizz buzz - se o parametro da função for divisivel por 3, retorne fizz,
# se o parametro da função for divisivel por 5, retorne buzz. Se o parametro da funcao
#for divisel por 5 e 3, retorne FIZZ, BUZZ, caso contrario, retorno o numero enviado


def funcao_fizz_buzz(num):
    if num % 5 == 0 and num % 3 == 0:
        return "FIZZBUZZ"
    elif num % 3 == 0:
        return "FIZZ"
    elif num % 5 == 0:
        return "BUZZ"
    else:
        print(num)
print(funcao_fizz_buzz(15))