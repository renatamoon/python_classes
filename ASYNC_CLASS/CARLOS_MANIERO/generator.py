import random

""" toda vez que temos um yield é chamado de generator. """

# função principal
def lancar_dados(n):
    for i in range(0, n):
        yield random.randint(1, 6) # gerador
        

# iteração dos dados gerados
for dado in lancar_dados(10):
    print("RETORNO DO DADO LANÇADO: ", dado)
    