#DICIONARIOS EM PYTHON
#tem INDICE & VALOR - estrutura de dados que recebe NOME e VALOR da chave

# dicionario = {'chave1': 'valor da chave'}
# dicionario['nova_chave'] = "valor da nova chave"
# #aqui estou adicionando um valor e uma chave ao dicionario
# print(dicionario) #execução: {'chave1': 'valor da chave', 'nova_chave': 'valor da nova chave'}
# print(dicionario['chave1']) #acessando um valor do dicionario
#
# print("=-"*20)
#
# dicionario = dict(chave1="valor da chave", chave2="valor da outra chave")
# print(dicionario)
#
# print("=-"*20)
#
# dicionario = {1:"valor", 2:"valor",3:"valor",4:"valor real da chave"}
# print(dicionario) #chaves precisam ser unicas, então cada uma precisa te
# #execução: {1: 'valor', 2: 'valor', 3: 'valor', 4: 'valor real da chave'}
# print(dicionario[3]) #acessando o indice 3 no dicionario - execução: valor
#
# print("=-"*20)
#
# dicionario = {
#     'str': 'valor',
#     123:"outro valor",
#     (1,2,3,4):"Tupla",
# }
#
# dicionario['nao existe'] = "agora existe"
# if "naoexiste" in dicionario:
#     print(dicionario['nao existe'])
#
# #ou podemos fazer o seguinte:
#
# if dicionario.get("nomedachave")) is not None:
#     print(dicionario.get("nomedachave"))
# print(123)

#=====
#
# dicionario = {
#     'chave1' : 'valor',
#     'chave2' :'outro valor',
#     'chave3' : 'Tupla',
# }
# dicionario['str'] = 'agora ela existe'
#
# if dicionario.get('str') is not None:
#     print(dicionario.get('str'))
# print(123)

#para vermos um valor dentro do dicionario - se existe ou nao - retorna um valor bool
# print('str' in dicionario) #no caso existe, então sai um valor TRUE
# print('str' in dicionario.keys()) #acessa da mesma forma de cima
# print("valor" in dicionario.values()) #acessando os valores do dicionario
#
# print(len(dicionario)) #tamanho do dicionario - mostra quantos pares existe

# dicionario = {
#     'chave1' : 'valor',
#     'chave2' :'outro valor',
#     'chave3' : 'Tupla',
# }

#for key, valor in dicionario.items():
    #print(key[0], key[1]) #irá mostrar apenas os valores dentro do dicionario
    #acessando a chave e o valor separadamente
    #print(key, valor)
# chave1 valor
# chave2 outro valor
# chave3 Tupla

clientes = {
    'cliente1': {
        'nome':'Luiz',
        'sobrenome':'Otavio',
    },
    'cliente2':{
        'nome':'joao',
        'sobrenome':'moreira',

    },
} #FAZENDO DICIONARIOS DENTRO DE DICIONARIOS - E ITERANDO VALORES
for clientes_k, clientes_v in clientes.items():
    print(f'Exibindo {clientes_k}')
    for dados_k, dados_v in clientes_v.items():
        print(f'\t{dados_k} = {dados_v}')
#EXECUTE:
# Exibindo cliente1
# 	nome = Luiz
# 	sobrenome = Otavio
# Exibindo cliente2
# 	nome = joao
# 	sobrenome = moreira