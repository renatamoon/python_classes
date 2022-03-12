#LISTA DE NUMEROS INTEIROS

lista_de_listas_de_inteiros = [
    [1,2,3,4,5,6,7,8,9,10],
    [9,1,8,9,9,7,2,1,6,8],
    [1,3,2,2,8,6,5,9,6,7],
    [3,8,2,8,6,7,7,3,1,9],
    [4,7,6,5,2,9,2,1,2,1],
    [5,3,1,8,5,7,1,8,8,7],
    [10,9,8,7,6,5,4,3,2,1],
]
#crie uma função que crie o primeiro duplicado, considerando o segundo numero como duplicação
#requisitos: aordem dos numeros duplicadosd é considerada a partir da segunda ocorrencia(o
# numero duplicado em si.
#exemplo: [1,2,3,>3<, 2,1]
#se nao conseguir encontrar numeros duplicados na lista, retorne -1

def encontra_primeiro_duplicado(parametro_listadeinteiros):
    numeros_checados = set()
    primeiro_duplicado = -1

    for numero in parametro_listadeinteiros:
        if numero in numeros_checados:
            primeiro_duplicado = numero
            break
        numeros_checados.add(numero) #a cada numero checado, vamos jogar dentor dentro do set
        #de numeros_checados. A var numero se trata de cada numero dentro da lista
    return primeiro_duplicado #retorna para a função o primeiro duplicado

for lista_de_inteiros in lista_de_listas_de_inteiros:
    print(lista_de_inteiros, encontra_primeiro_duplicado(lista_de_inteiros))
        #1. mostra a lista de inteiros
        #2. dentro da lista de inteiros, encontra dentro da lista de intieros, o primeiro duplicado
#EXECUÇÃO:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] -1 #nao tem numeros repetidos
# [9, 1, 8, 9, 9, 7, 2, 1, 6, 8] 9
# [1, 3, 2, 2, 8, 6, 5, 9, 6, 7] 2
# [3, 8, 2, 8, 6, 7, 7, 3, 1, 9] 8
# [4, 7, 6, 5, 2, 9, 2, 1, 2, 1] 2
# [5, 3, 1, 8, 5, 7, 1, 8, 8, 7] 5
# [10, 9, 8, 7, 6, 5, 4, 3, 2, 1] -1 #nao tem numeros repetidos

