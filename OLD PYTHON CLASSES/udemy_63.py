#SISTEMA DE PERGUNTAS E RESPOSTA USANDO TUDO O QUE FOI APRENDIDO E
#USANDO DICIONARIOS
print("TEXTO EXPLICATIVO: ")
perguntas = {
    'Pergunta 1': {
        'pergunta': 'quanto é 2 + 2? ',
        'respostas': {'a': '1','b': '4','c': '5',},
        'resposta_certa':'b',
    },
    'Pergunta 2': {
        'pergunta': 'quanto é 3*2? ',
        'respostas': {'a': '4','b': '10','c': '6',},
        'resposta_certa':'c',
    },
    'Pergunta 3': {
        'pergunta': 'quanto é 1 + 2? ',
        'respostas': {'a': '4','b': '3','c': '6',},
        'resposta_certa':'b',
    },
    'Pergunta 4': {
        'pergunta': 'quanto é 1 - 1? ',
        'respostas': {'a': '0','b': '10','c': '1.5',},
        'resposta_certa':'a',
    },
    'Pergunta 5': {
        'pergunta': 'quanto é 8/4? ',
        'respostas': {'a': '20','b': '1','c': '2',},
        'resposta_certa':'c',
    },
}
respostas_certas = 0
print("=-"*20) #acessando a chave de perguntas, e depois acessando a chave de respostas
for chave_pergunta, chave_resposta in perguntas.items():
    print(f'{chave_pergunta}: {chave_resposta["pergunta"]}')
    print()
    print('RESPOSTAS: ')
    for rk, rv in chave_resposta['respostas'].items(): #iterando dentro do dicionario de respostas
        print(f'[{rk}]:{rv}')
    resposta_usuario = input("SUA RESPOSTA: ")
    if resposta_usuario == chave_resposta['resposta_certa']:
        print("EEEH! VOCÊ ACERTOU")
        print()
        respostas_certas += 1
    else:
        print("VOCE ERROU :(")
        print()
print("=-"*20)

quantidade_perguntas = len(perguntas) #retorna quantas perguntas tem
porcentagem_acerto = respostas_certas / quantidade_perguntas * 100

print(f'Você acertou {respostas_certas} resposta(s).')
print(f'Sua porcentagem de acerto foi de {porcentagem_acerto}%')