#FOR IN - ESTRUTURAS DE REPETIÇÃO
#INTERANDO STRINGS COM O FOR
#FUNÇÃO RANGE(START=0, STOP, STEP=1)

# texto = "python"

# c = 0
# while c < len(texto):
#     print(texto[c]) #acessando o indice da string
#     c+= 1 #incrementando 1 ao contador
#-------------
# for n, letra in enumerate(texto):
#     print(n, letra) #isso faz a mesma coisa que a funçao 
    #colocada acima
#RESULTADO:
# 0 p
# 1 y
# 2 t
# 3 h
# 4 o
# 5 n
#----------- FOR / IN 
#então a funação RANGE tem como premissa de
#INICIAR A VARIÁVEL EM 1
#STOP - PARAR
#STEP = 1 em 1 (pular) eXEMPLO ABAIXO:

# for n in range(0, 10, 1):
#no cas que iniciar em 0, vá até o 10 e pule de 1 em 1
#     print(n) #então esse laço range funciona até
    #chegar ao 9, printar o numero quando chegar
    #até o 9

#CASO QUEIRA UM DECREMENTAÇÃO -1 (DECREMENTAR DE 1 EM 1)
# for n in range(20, 10, -1):
#     print(n)

#RESULTADO:
# 20
# 19
# 18
# 17
# 16
# 15
# 14
# 13
# 12
# 11 #SE QUISER QUE PARE, TEM QUE COLOCAR O NUMERO 9

# for n in range(0,100,8):
#     print(n)

# #NESSE LAÇO INICIA EM 0, VAI ATÉ O 99, E PULA DE 8 EM 8

# print("="*5)

# for n in range(100):
#     if n % 8 == 0:
#         print(n) #ele vai printar todos os numeros que são
        #divisiveis por 8

#LAÇO FOR IN with strings

texto = 'Python'
nova_string = ''

for letra in texto:
    if letra == 't':
        continue
        nova_string = nova_string + letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
    else:
        nova_string += letra
print(nova_string)




