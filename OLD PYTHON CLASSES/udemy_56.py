#FUNÇÕES (DEF) EM PYTHON - ARGS **KWARGS**

# def func(a1, a2, a3, a4, nome=None, a6=None):
#     print(a1, a2, a3, a4, nome, a6)
#     return nome, a4, a6 #posso fazer com que seja retornado apenas alguns dos valores colocados
    #o retorno dessa função é uma TUPLA, onde nao consigo modificar os valores
    #diferentemente da LISTA.
#func(1,2,3,4,nome="Luiz", a6="5") #caso eu tenha iniciado uma variável dentro do meu argumento
#que nao tenha valor numeral, tenho que dizer o que se refere a variavel usando um =
#como aqui: def func(a1, a2, a3, a4, nome=None, a6=None): todos os valores depois do None,
#tem que ter um valor onde indica o que esta mostrando na var
#
# var = func(1,2,3,4,nome="RENATA", a6="LUIZA")
# print(var[0], var[1]) #podemos acessar o indice tbem

# def func(*args):
#     print(args)
#
# lista = [1,2,3,4,5]
# n1, n2, *n = lista #aqui estamos empacotando a lista dizendo que op valor n1 = 1, n2 = 2, e
# #O RESTO DA LISTA VALOR *n
# print(n1, n2, *n)

#*** podemos também

# def func(*args):
#     print(args)
# lista = [1,2,3,4,5]
# print(*lista, sep="-") #desempacotando cada item da lista - EXECUÇÃO: 1 2 3 4 5
#utilizando esse SEP, eu tenho como atribuir qual o valor ou sinal do separador vai receber
#execução: 1-2-3-4-5

# def func(*args):
#     print(args) #args inteiros
#     print(args[0])#acessando o indice 0 (numero 1) da lista onde está a func (que é o valor da função
#     print(args[-1]) #ultimo item da lista
#     print(len(args))#mostrando o tamanho da lista que no caso é um tupla, não é modificavel
# func(1,2,3,4,5)

#FAZENDO CAST DE UMA LISTA
#
# def func(*args):
#     args = list(args) #transformando o valor de args (tupla) para uma lista
#     args[0] = 20 #transformando o indice 1 em 20
#     print(args) #printando args
# func(1,2,3,4,5)

# def func(*args):
#     for v in args: #para valor em args
#         print(v) # a cada volta do for vemos o valor printado
# lista = 1,2,3,4,5
# func(*lista) #definindo a função com valor da lista desempacotada

# def func(*args, **kwargs):
#     print(args) #pedindo para a função acessar o primeiro item da lista
# lista = [1,2,3,4,5]
# lista2 = [10,20,30,40,50]
# func(*lista,*lista2) #pedindo para desempacotar as listas + adicionar a outra lista desempacotada
#dentro da função
#*execução: ([1, 2, 3, 4, 5], '6')

#kwargs = key words with arguments

# def func(*args, **kwargs):
#     print(args) #pedindo para a função acessar o primeiro item da lista
#     print(kwargs) #ir[a executar apenas entre chaves: {'nome': 'renata', 'sobrenome': 'miranda'}
#     print(kwargs["nome"], kwargs["sobrenome"]) #retorna apenas: renata miranda
#
#     nome = kwargs.get("nome") #como o key argument foi dado dentro da função, ele retorna
#     #onde está colocado o nome ou qualquer outro argumento com valor.
#     print(nome) #retorna: renata
#
# lista = [1,2,3,4,5]
# lista2 = [10,20,30,40,50]
# func(*lista,*lista2, nome="renata", sobrenome="miranda")

#USANDO if EM KWARGS:
def func(*args, **kwargs):
    print(args)

    idade = kwargs.get("idade")

    if idade is not None: #se ele tiver valor printar a idade, se não, "nao existe"
        print(idade)
    else:
        print("não existe")

lista = [1,2,3,4,5]
lista2 = [10,20,30,40,50]
func(*lista, *lista2, nome="renata", sobrenome="monteiro", idade="20")

