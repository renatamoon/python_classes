#WHILE/ELSE
#CONTADORES
#ACUMULADORES

'''há um contador, vai garantir que o nosso laço while terá
um fim'''

contador = 1 #pode iniciar em que numero quiser
#contanto que seja menor que o "while contador < 100:"
acumulador = 1

while contador <= 10:
    print(contador, acumulador)

    if contador > 5: #no caso, qdo o contador
        #chegou a 4, ele deu um break
        break

    acumulador = acumulador + contador
    contador += 1 #acumulado de forma linear
    #quando é iniciado em 0 ou aumenta de acordo
    #com o inicio do contador
else: 
    print("CHEGUEI NO ELSE") #ele vale quando a expressão de cima for
    #falsa. quANDO O CONTADOR PASSOU A SER MAIOR QUE 10
    #while contador <= 10: ai vem a vez do else.
print("ISSO SERÁ EXECUTADO NA TELA")

#RESULTADO:
#1 1
# 2 2
# 3 4
# 4 7
# 5 11
# 6 16
# 7 22
# 8 29
# 9 37
# 10 46
# #incrementar a cada laço
#pode ser qualquer tipo de conta dentro do laço