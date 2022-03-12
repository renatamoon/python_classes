#crie uma função que receba uma função 2 como parametro e retorne o valor da
#funcao2 executada

def ola_mundo():
    return "Ola Mundo!"

def mestre(funcao):
    return funcao()

executando = mestre(ola_mundo) #aqui eu pego a funcao mestre e passo os parametros da funcao
#ola_mundo para executar
print(executando)


#crie uma funcao1 que recebe funcao2 como parametro e retorne o valor da
#funcao2 executada. FDaça a funcao1 executar duas funcoes que receberam numeros
#diferentes de argumento

def funcao_master(funcao, *args, **kwargs): #tem uma funcao + 2 argumentos
    return funcao(*args, **kwargs) #aqui ele diz que retornar os valores da funcao, args
        #+ kwargs

def falar_oi(nome): #criando uma nova funcao que falar_oi e colocando o nome como arg
    return f'OI {nome}' #retorna o OI + nome

def saudacao(nome, saudacao): #mais uma funcao, colocando como arg e kwargs nome e saudacao
    return f'{saudacao} {nome}' #retorna saudação, e nome (que deveremos colocar depois)

executando = funcao_master(falar_oi, "Luiz") #executando a funcao falar_oi + nome
executando2 = funcao_master(saudacao, "luiz", saudacao="Bom dia")
#executando a funcao saudação + nome + colocando kwargs para saudação
print(executando)
print(executando2)