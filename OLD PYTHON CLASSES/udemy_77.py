"""count - itertools""" #gera um contador que é um iterador
#queira gerar contadores

from itertools import count

contador = count(start=5, step=2) #quero iniciar do 5, e pular de 0,1 em 0,1
#contador = count(start=9, step=-1) também pode colocar step -1

print(next(contador)) #1
print(next(contador)) #1
print(next(contador)) #1

for valor in contador:
    print(round(valor, 2)) #arredondando com 2 casas decimais

    if valor >= 8: #quebrando o laço no 50 pulando de acordo com o
        # count que coloquei = 5 (começar do 5)
        break

print("=*"*10)

