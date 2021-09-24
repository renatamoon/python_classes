#objetos mutaveis - listas e dicionarios
#imutaveis = string, tuplas, numeros, True, False, None

def lista_de_clientes(clientes_iteravel, lista=None): #atributo imutavel
    #manda duas listas, e se uma lista já estiver feita, elas sao unidas
        if lista is None:
            lista = [] #se a lista tiver o valor None todas as listas serão independentes
        lista.extend(clientes_iteravel)
        return lista

lista_clientes_1 = ['fabricio'] #lista independente
clientes1 = lista_de_clientes(['joao', 'maria', 'eduardo'])
clientes2 = lista_de_clientes(['marcos', 'jonas', 'zico'])
clientes3 = lista_de_clientes(['bruna', 'maria', 'josé'])

print(clientes1)
print(clientes2)
print(clientes3)

#execute caso o atributo da função for list=[]:
# ['joao', 'maria', 'eduardo', 'marcos', 'jonas', 'zico']
# ['joao', 'maria', 'eduardo', 'marcos', 'jonas', 'zico']

#execute caso o atributo da funcao for lista=None:
# ['joao', 'maria', 'eduardo']
# ['marcos', 'jonas', 'zico']
# ['bruna', 'maria', 'josé']

