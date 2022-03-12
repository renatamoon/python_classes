#DECORADORES
#funcoes decoradoras

'''def fala_oi():
    print('Oi')
variavel = fala_oi #dizendo que a funcao fala_oi é igual a variavel
variavel() #e executando a variavel é a mesma coisa que executar a funcao

print(type(variavel)) #<class 'function'>'''

'''def master(funcao): #criei uma funcao master para que ela execute tbem o conteudo da funcao slave
    def slave(*args, **kwargs):
        print('agora estou decorada.')
        funcao(*args, **kwargs)
    #slave() #chamando a funcao slave para que ela possa ser executada
    return slave

@master #funcao esta decorada - decorador
def fala_oi():
    print('oi')

# variavel = master(fala_oi) #agora a funcao é uma funcao esperando para ser executada
# variavel()
#print(type(variavel)) #<class 'function'>

@master
def outra_funcao(msg):
    print(msg)

outra_funcao('ola, eu sou luiz')'''

#-------OUTRO EXEMPLO
from time import time
from time import sleep

def velocidade(funcao):
    def interna(*args, **kwargs):
        start_time = time()
        resultado = funcao(*args, **kwargs)
        end_time = time()
        tempo = (end_time - start_time) * 1000 #quer em milisegundos
        print(f'a função {funcao.__name__} levou {tempo: .2f}ms para executar')
        return resultado
    return interna

@velocidade
def demora():
    for numero in range(1000):
        print(numero, end='')
        #sleep(1)
demora()
#EXECUTE:
# 0
# 1
# 2
# 3
# 4
# a função demora levou 5047.149419784546s mpara executar





