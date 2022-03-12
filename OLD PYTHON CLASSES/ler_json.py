import json

with open('abc.json', 'r') as file:
    d1_json = file.read()
    d1_json = json.loads(d1_json) #quero que volte a ser um dicionario

for k, v in d1_json.items():
    print(k)
    for k1, v1 in v.items():
        print(k1, v1)
#execução
# Pessoa 1
# nome luiz
# idade 25
# Pessoa 2
# nome Rose
# idade 30

