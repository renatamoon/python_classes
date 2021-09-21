#OPERADOR TERNARIO EM PYTHON

logged_user = False #aqui eu já informei que o usuário não está logado,
#então a mensagem será a segundam, que o usuário precisa logar.
#desta forma, a primeira operação IF é falsa, já que colocamos nossa var como
#falsa.
#caso colocassemos o logged_user = True, ele já informaria como USUÁRIO LOGADO
if logged_user:
    message = 'USUÁRIO LOGADO'
else:
    message = 'USUÁRIO PRECISA LOGAR'
print(message)

#USANDO UM OPERADOR TERNARIO NESSE PROGRAMA:

message = 'usuário logado' if logged_user else 'Usuario precisa logar'
            #já fala antes do IF qual o valor que quer assumir se a var for
            #TRUE e depois do ELSE, se a condição for FALSE
print(message)

#TAMBÉM PODE-SE FAZER DA SEGUINTE MANEIRA
#EXEMPLO:
idade = input("qual a sua idade? ")

if not idade.isnumeric():
    print("VOCÊ PRECISA DIGITAR APENAS NUMEROS")
# if idade >= 18:
#     print("PODE ACESSAR")
# else:
#     print("NÃO PODE ACESSAR")
#fazendo essa operação de cima usando operadores ternários:
else:
    idade = int(idade)
    maior_idade = (idade >= 18)
    message = 'Pode acessar' if maior_idade else 'não pode acessar'

    print(message)
