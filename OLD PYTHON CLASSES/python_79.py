#GROUP BY - agrupando valores
from itertools import groupby, tee #faz copias do iterador

alunos = [
#LISTA QUE CONTEM VARIOS DICIONARIOS
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
#para usar a função groupby, temos que ordenar a lista primeiro
#usar a função sorted do dicionario
# alunos.sort(key=lambda item: item['nota'])
# for aluno in alunos:
#     print(aluno)
#execute:
# {'nome': 'luiz', 'nota': 'A'}
# {'nome': 'fabricio', 'nota': 'A'}
# {'nome': 'joana', 'nota': 'A'}
# {'nome': 'eduardo', 'nota': 'A'}
# {'nome': 'leticia', 'nota': 'B'}
# {'nome': 'joao', 'nota': 'B'}
# {'nome': 'anderson', 'nota': 'B'}
# {'nome': 'rose', 'nota': 'C'}
# {'nome': 'andre', 'nota': 'C'}
# {'nome': 'mary', 'nota': 'D'}

#agrupando todos que tenha nota A
print()
ordena = lambda item: item['nota'] #ordena por nota
alunos.sort(key=ordena) #ordenando aos valores - é necessário ordenar os valores
alunos_agrupados = groupby(alunos, ordena)
    #chave = nota           #
for agrupamento, valores_agrupados in alunos_agrupados:
    va1, va2 = tee(valores_agrupados) #va1 e va2 - sao copias depois que os iteradores se esgotaram
    print(f'Agrupamento: {agrupamento}') #retorna uma tupla com os valor
    for aluno in va1:
        print(f'\t{aluno}')
    quantidade = len(list(va2))
    print(f'\t{quantidade} alunos tiraram a nota {agrupamento}')
    print()

#execute:
# Agrupamento: A
# 	{'nome': 'luiz', 'nota': 'A'}
# 	{'nome': 'fabricio', 'nota': 'A'}
# 	{'nome': 'joana', 'nota': 'A'}
# 	{'nome': 'joana', 'nota': 'A'}
# 	{'nome': 'joana', 'nota': 'A'}
# 	{'nome': 'joana', 'nota': 'A'}
# 	{'nome': 'eduardo', 'nota': 'A'}
# 	7 alunos tiraram a nota A
#
# Agrupamento: B
# 	{'nome': 'leticia', 'nota': 'B'}
# 	{'nome': 'joao', 'nota': 'B'}
# 	{'nome': 'anderson', 'nota': 'B'}
# 	{'nome': 'anderson', 'nota': 'B'}
# 	{'nome': 'anderson', 'nota': 'B'}
# 	{'nome': 'anderson', 'nota': 'B'}
# 	6 alunos tiraram a nota B
#
# Agrupamento: C
# 	{'nome': 'rose', 'nota': 'C'}
# 	{'nome': 'andre', 'nota': 'C'}
# 	2 alunos tiraram a nota C
#
# Agrupamento: D
# 	{'nome': 'mary', 'nota': 'D'}
# 	1 alunos tiraram a nota D





