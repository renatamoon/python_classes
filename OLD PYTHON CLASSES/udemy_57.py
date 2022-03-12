#VARIÁVEL GLOBAL

# variavel = "valor"
#
# def funcao():
#     print(variavel) #printa o valor da variavel
#
# def funcao2(arg=None):
#     arg = arg.replace("v", "c")
#     return arg
#
# funcao()
# outra_variavel = funcao2(arg=variavel)
#
# print(outra_variavel) #printamos o valor da variavel real que identificamos na linha 3

#RETURN:
# valor
#calor

# variavel = "valor"
# def func():
#     variavel = 1234
#     print(variavel)
#
# func()

#   qualquer variavel que esta dentro de uma função não pode ser acessada e mudada dentro
#de outra função
#
# variavel = "valor"
#
# def func():
#     outra_variavel = "valor"
#     return outra_variavel
#
# def func2():
#     print(outra_variavel)
#
# func()
# func2() #neste caso, não pode ser acessado o valor que esta dentro de uma funcão

#pode ser usado assim:

variavel = "valor"

def func():
    outra_variavel = "LUIZ OTAVIO"
    return outra_variavel

def func2(arg):
    print(arg)

var = func()
func2(var)
#CONECTANDO DUAS FUNÇÕES