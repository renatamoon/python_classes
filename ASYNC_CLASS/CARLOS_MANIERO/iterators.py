from iterators_generators import lancar_dados

# importando a função

"""
for dado in lancar_dados(10):
    print("ROLANDO DADO - RESULTADO: ", dado) """


print("=-"*20)

# se quisermos apenas lançar apenas 2 dados:

dados = lancar_dados(2)
print("ROLANDO DADO - RESULTADO: ", dados) # ROLANDO DADO - RESULTADO:  [3, 4]


# ------ retornando iterator dos dados que eu acabei de lançar

iterator = iter(dados)
print("ITERATOR: ", iterator) # ITERATOR:  <list_iterator object at 0x7f5a2b044790>

print("ITERATOR OUTPUT", dados.__iter__()) # <list_iterator object at 0x7fc1b6b892e0>

print("NEXT ITERATOR: ", next(iterator))
print("NEXT ITERATOR: ", next(iterator))
print("NEXT ITERATOR: ", next(iterator))