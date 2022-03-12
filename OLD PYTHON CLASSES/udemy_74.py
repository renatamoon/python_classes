#zip - unindo iteráveis
#zip_longest - itertools
from  itertools import zip_longest, count

indice = count()
##codigo
cidades = ["sao paulo", "belo horizonte", "salvador", "monte belo", "outra"]
#codigo
estados = ["sp", "mg", "ba"]

#cidades_estados = zip(cidades, estados)
#print(next(cidades_estados)) #ve o primeiro valor de cidade e estados

# for valor in cidades_estados:
#     print(valor[0], valor[1]) #mostra o valor 0 e 1 dentro das duas listas
#convertendo em uma lista:
#print(list(cidades_estados)) #execute:[('sao paulo', 'sp'), ('belo horizonte', 'mg'), ('salvador', 'ba')]
#print(dict(cidades_estados))
cidades_estados = zip(
    indice,
    estados,
    cidades,
    )
#print(list(cidades_estados)) #execute:[('sp', 'sao paulo'), ('mg', 'belo horizonte'), ('ba', 'salvador'), (None, 'monte belo')]
#printa a maior lista
#convertendo em uma lista

# for valor in cidades_estados: #desempacotando uma tupla tripla
#     print(valor)
#execute:
# (0, 'sp', 'sao paulo')
# (1, 'mg', 'belo horizonte')
# (2, 'ba', 'salvador')

#desempacotar os valores:

for indice, estados, cidades in cidades_estados:
    print(indice, estados, cidades)
    #execute:
# 0 sp sao paulo
# 1 mg belo horizonte
# 2 ba salvador
