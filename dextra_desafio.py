    """
Dado um vetor de números inteiros não negativos representando tijolos maciços empilhados onde a largura de cada tijolo é 1. Escreva um algoritmo que calcule quanto de água ficaria armazenado entre os tijolos após uma chuva intensa.
Assuma que:
    • O vetor nunca estará vazio
    • Os valores do vetor sempre serão de 0 até 5, ou seja, 0, 1, 2, 3, 4 ou 5
Exemplo 1:
Input: [2, 1, 0, 3, 1, 2, 2, 3, 2]
Output: 7
Explicação: A pilha de tijolos (parte marrom marcada com "x") é representado pelo vetor de input. Nesse caso, 7 unidades de água da chuva (parte azul marcada com "a") foram armazenadas.
"""

def encontra_maiores(lista):
    parede_maior1 = 0
    index_inicial = 0
    parede_maior2 = 0
    index_final = 0
    lista_temp = lista.copy()
    for index, numero in enumerate(lista_temp):
        if numero > parede_maior1:
            parede_maior1 = numero
            index_inicial = index
    lista_temp.remove(parede_maior1)
    for index, numero in enumerate(lista_temp):
        if numero > parede_maior2:
            parede_maior2 = numero
            index_final = index
    dic = [
        {
            'primeiro_indice': index_inicial,
            "primeiro_maior": parede_maior1
         },
        {
            'segundo_indice': index_final + 1,
            "segundo_maior": parede_maior2
        }
    ]
    if dic[0]['primeiro_maior'] != dic[0]['primeiro_maior']:
        return
    else:
        return dic

def remove_entre_paredes(lista, dic):
    lista_temp = []
    for numero in lista[:dic[0]['primeiro_indice']]:
        lista_temp.append(numero)
    for numero in lista[dic[1]['segundo_indice'] + 1:]:
        lista_temp.append(numero)
    return lista_temp

def aumenta_numeros(lista, dic):
    numeros_preenchidos = 0
    for numero in lista[(dic[0]['primeiro_indice'] + 1):dic[1]['segundo_indice']]:
        while numero < dic[0]['primeiro_maior']:
            numero += 1
            numeros_preenchidos += 1
    return numeros_preenchidos

def main(lista):
    dic = encontra_maiores(lista)
    if dic:
        qtd = aumenta_numeros(lista, dic)
        if remove_entre_paredes(lista, dic):
            lista_nova = remove_entre_paredes(lista, dic)
        while lista_nova[0] == lista_nova[-1]:
                new_dic = encontra_maiores(lista_nova)
                qtd += aumenta_numeros(lista_nova, new_dic)
                if not remove_entre_paredes(lista_nova, new_dic):
                    break
                else:
                    lista_nova = remove_entre_paredes(lista_nova, new_dic)
        print(f'Input: {lista}')
        print(f'Output: {qtd}')
        print()
    else:
        print('Não existe "tijolos" da mesma altura.')

entrada1 = [2, 1, 0, 3, 1, 2, 2, 3, 2]
entrada2 = [5, 2, 0, 2, 5]
entrada3 = [4, 2, 4, 1, 0, 1]
entrada4 = [1, 2, 5, 1, 5, 2]

main(entrada1)
main(entrada2)
main(entrada3)
main(entrada4)
