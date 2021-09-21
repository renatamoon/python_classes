string = '012345678901234567890123456789012345678901234567890123456789'
'''separar de grupos de 0 a 9 com ponto'''
"""USANDO LIST COMPREEHENTION"""
n = 10
lista = [string[i:i+n] for i in range(0, len(string), n)]
retorno = ".".join(lista) #usando a função join para juntar a lista com ponto (.)
print(lista)
#fazendo uma list comprehension dentro de uma tupla com dois valores
#(i, i+n) - numero mais

"""lista = [string[i:i+n] for i in range(0, len(string), n)]
ele pega a string e faz o primeiro numero (i) até o último + n (que vale 10)
então esse valor vai fatiar de i até décimo numero.
---for i in range(0, len(string), n
aqui diz que numero no intervalo do index 0, total da string, pulando de n em n (10)

"""