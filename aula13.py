#LAÇOS DE REPETIÇÃO - PARTE 1 - FOR

# for c in range(0,3):
#   passo
#   pula
# passo
# pula

# for c in range(0,6):
#     print("OLÁ MUNDO! ")
# print("FIM")

#*****OUTRA FORMA

# n = int(input("DIGITE UM NUMERO QUALQUER: "))
# for c in range(0, n+1): #coloquei o +1 para que ele chegasse ao numero digitado no N
# #se colocar apenas apenas o N, ele printa até o numero anterior, então se o N valer 5, ele printa até o 4
#     print(c)
# print("FIM")

#OUTRO PROGRAMA PARA VER UTILIDADES

# inicio = int(input("NUMERO DE INICIO: "))
# final = int(input("NUMERO DE FINAL: "))
# passo = int(input("QUANTOS PASSOS: "))

# for c in range(inicio, final+1, passo):
#     print(c)
# print("FIM")

soma = 0 #tem que iniciar a variavel aqui para que possamos chama-la depois
for c in range(0, 10):
    n = int(input("DIGITE O VALOR: "))
    soma += n #SOMA TODOS OS VALORES COLOCADOS NA VAR N 
print("A SOMA DE TODOS OS VALORES FOI {}".format(soma))

