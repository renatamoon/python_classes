# AULA 001 - ITERATORS E GENERATORS

# imports
import random
from time import sleep


# função principal
def lancar_dados(n):
    dados = []
    
    for i in range(0, n):
        dados.append(random.randint(1, 6))
        
    return dados

# iterador para receber os numeros dos dados
for dado in lancar_dados(10):
    # sleep(1)
    print("ROLANDO DADO - RESULTADO ... ", dado)
