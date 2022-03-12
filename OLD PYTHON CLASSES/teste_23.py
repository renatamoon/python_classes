from itertools import groupby, tee

alunos = [

    {'nome': 'luiz', 'nota': 'A'},
    {'nome': 'leticia', 'nota': 'B'},
    {'nome': 'fabricio', 'nota': 'A'},
    {'nome': 'rose', 'nota': 'C'},
    {'nome': 'mary', 'nota': 'D'},
    {'nome': 'joana', 'nota': 'A'},
    {'nome': 'joana', 'nota': 'A'},
    {'nome': 'joana', 'nota': 'A'},
    {'nome': 'joana', 'nota': 'A'},
    {'nome': 'joao', 'nota': 'B'},
    {'nome': 'eduardo', 'nota': 'A'},
    {'nome': 'andre', 'nota': 'C'},
    {'nome': 'anderson', 'nota': 'B'},
    {'nome': 'anderson', 'nota': 'B'},
    {'nome': 'anderson', 'nota': 'B'},
    {'nome': 'anderson', 'nota': 'B'},
]

# for agrupamento, valores_agrupados in alunos_agrupados:
#     va1, va2 = tee(valores_agrupados) #va1 e va2 - sao copias depois que os iteradores se esgotaram
#     print(f'Agrupamento: {agrupamento}') #retorna uma tupla com os valor
#     for aluno in va1:
#         print(f'\t{aluno}')
#     quantidade = len(list(va2))
#     print(f'\t{quantidade} alunos tiraram a nota {agrupamento}')
#     print()

#ordenando a lista primeiro:

ordenando = lambda item: item['nota']
alunos.sort(key=ordenando)
alunos_agrupados = groupby(alunos, ordenando)
    #nota       #valor grupby dentro dos alunos
for agrupamento, valores_agrupados in alunos_agrupados:
    va1, va2 = tee(valores_agrupados) #ele esta fazendo uma copia dos valores
    print(f'agrupamento: {agrupamento}')
    for aluno in va1:
        print(f'\t{aluno}')
    quantidade = len(list(va2))
    #print(quantidade) #quantidade de alunos dentro do agrupamento de novas b
    print(f'\t{quantidade} alunos que tiraram nota {agrupamento}')
    print()