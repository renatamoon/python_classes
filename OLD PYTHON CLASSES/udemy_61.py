#TUPLAS

#adicionando elementos dentro das tuplas

# t1 = 1,2,3,"a", "renata monteiro"
# print(t1)
#
# for valor in t1:
#     print(valor) #imprimir cada valor separado de cada elemento da tupla
# #fatiar a tupla:
# print(t1[2:]) #fatiando do elemento 2 até o ultimo, eu nao preciso mostrar qual é o ultimo
#
# t1 = 1,2,"luiz",4,5
# t2 = 6,7,8,9,10
# t3 = t1 + t2
# print(t3) #concateno as 2 tuplas - (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
#
# n1, n2, n3, *var, n10 = t3 #o var *var está desempacotando as outras variaveis
# print(n10) #o n10 equivale ao ultimo elemento da tupla

#----caso queira modificar o valor de uma tupla

t1 = (1,2,3,4,5)
#t1[1] = 3 #eu estou querendo modificar o valor de uma tupla, no caso o index 1 para 3
#mas nao da pra fazer isso.

#no caso temos que fazer o seguinte: TRANFORMAR TUPLA EM LISTA:

t1 = list(t1)
t1[1] = 3000
print(t1)#execução: [1, 3000, 3, 4, 5]



