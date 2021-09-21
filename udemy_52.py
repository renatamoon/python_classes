#FUNÇÕES - DEF EM PYTHON
#quando definimos uma função, temos que colocar o DEF de definir
#e colocar o que a função vai chamar. Para chamar a função, somente
#colocar o nome da função e abrir um parenteses
#-as funções são criadas para você não repetir os codigos

# def function(msg, nome):
#     print(msg, nome) #a função tá recebendo um parametro/argumento
# function("POSSO ESCREVER O QUE QUISER DENTRO DO CHAMAMENTO DA FUNÇÃO", "RENATA")
#PRIMEIRO TEM QUE COLOCAR O ARGUMENTO INICIAL, E DEPOIS SEGUNDO ARGUMENTO

#também da pra fazer da seguinte forma:

# def saudacao(msg="OLA", nome="mensagem"):
#     msg = nome.replace("a", "4")
#     nome = nome.replace("i", "1")
#     return "{} {}".format(msg, nome)
# saudacao()
# saudacao("oi", "luiz")
# saudacao("Hello", "maria")

#EXECUÇÃO: se chamar a função sem os valores, ele virá com os valores já pré-definidos na linha 14
# OLA mensagem
# oi luiz
# Hello maria

# def saudacao(msg="OLA", nome="mensagem"):
#     msg = nome.replace("a", "4")
#     nome = nome.replace("i", "1")
#     return "{} {}".format(msg, nome)
# var = saudacao()
# print(var)

#AULA 53

# def funcao(var): #E AQUI estamos definindo a função
#     print(var) #2. depois estamos imputando o valor para a variável onde está "VALOR QUE EU QUERO"
# funcao("VALOR QUE EU QUERO") #1. estamos chamando a funcao onde estamos colocando um valor para ela

#SE NAO COLOCARMOS O print(var) dentro da função, dá um erro, DESTA FORMA, TEMOS SEMPRE QUE printar dentro
#da função

# def funcao(var):
#     return var
#
# variavel = funcao("VALOR QUE EU QUERO")
#
# if variavel:
#     print(variavel)
# else:
#     print("nenhum valor")

# def divisao(n1, n2): #definindo a função e suas vars
#     return n1/n2 #retorno tem sempre que acontecer
# print(divisao(8,2)) #printar a função e aqui colocar os valores de cada var para fazer o calculo

# def soma(n1, n2):
#     if n2 == 0:
#      return #esse return somente será executado se o n2 for igual a 0
#
#     return n1 + n2
# soma = soma(8,5)
#
# if soma:
#     print(soma)
# else:
#     print("NÃO É VALIDO O CALCULO")

# def f(var):
#     print("isso vale a: ", var)
# def dumb():
#     return f
#
# var = dumb()
# print(id(var), id(f)) #checando o id desta função na memoria - ou seja os valores são iguais
#
# if var == f:
#     print("var é igual a f")
# else:
#     print("bla")

#TUPLA - LISTA QUE NAO PODE SER ALTERADA
#
# def dumb():
#     return("luiz", "otavio")
#
# var = dumb()
#
# print(var[1], type(var))
#

