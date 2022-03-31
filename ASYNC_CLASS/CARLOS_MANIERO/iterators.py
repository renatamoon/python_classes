from iterators_generators import lancar_dados

# importando a função
for dado in lancar_dados(10):
    print("ROLANDO DADO - RESULTADO: ", dado)


print("=-"*20)

# se quisermos apenas lançar apenas 2 dados:

dados = lancar_dados(2)
print("ROLANDO DADO - RESULTADO: ", dados) # ROLANDO DADO - RESULTADO:  [3, 4]

