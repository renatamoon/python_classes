#MODULOS PADRAO DO PYTHON # AULA 89
#criando, lendo, escrevendo arquivos
        #abrir um arquivo para escrita
"""file = open('abc.txt', 'w+') #w = escrita
file.write('Linha 1 \n') #executa a quebra de linha
file.write('Linha 2 \n')
file.write('Linha 3 \n')
file.write('Linha 4 \n')
file.write('Linha 5 \n')

print("x*"*10)

file.seek(0, 0) #posicao e a relatividade (no caso, e aposição absoluta
print('lendo linhas: ')
print(file.read())
print("x*"*10)

file.seek(0, 0)
print(file.readline(), end='') #lendo linha por linha - lendo a linha 1
print(file.readline(), end='')
print("x*"*10)

file.seek(0,0)
for linha in file.readlines():
    print(linha, end='')

print("x*"*10)

file.seek(0,0)
for linha in file:
    print(linha, end='')
file.close() #precisa fechar o arquivo

#também podemos usar da seguinte forma, usando o tru/finally
try:
    file = open('abc.txt', 'w+')
    file.write('linha')
    file.seek(0,0)
    print(file.read())
finally:
    file.close() #fechando arquivo """

#esse gerenciador de contexto, gerencia e também fecha o arquivo, não
#precisa colocar uma linha para fechar o arquivo
'''with open('abc.txt', 'w+') as file:
    file.write('Linha 1 \n')
    file.write('Linha 2 \n')
    file.write('Linha 3 \n')

    file.seek(0)
    print(file.read())
#apenas ler o arquivo'''

"""print("=*"*5)
with open('abc.txt', 'a+') as file:
    file.write("Outra Linha \n")
    file.seek(0)
    print(file.read()) # acada execução, ele cria mais uma linha"""

import json

d1 = {
    'Pessoa 1' :{
        'nome' : 'luiz',
        'idade' : 25,
    },
    'Pessoa 2': {
        'nome': 'Rose',
        'idade': 30,
    },
}

'''d1_json = json.dumps(d1)
print(d1_json)
#execute: {"Pessoa 1": {"nome": "luiz", "idade": 25}, "Pessoa 2": {"nome": "Rose", "idade": 30}}
'''
d1_json = json.dumps(d1, indent=True)

with open ('abc.json', 'w+') as file: #quero que ele abra um arquivo,  e se já existir quero que ele apague e jogue
    #infos lá dentro
    file.write(d1_json)


