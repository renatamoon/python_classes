
while True:
    print("=-"*20)
    # cpf = '16899535009' #esse numero de cpf foi gerado somente para
    #checar a validade de um cpf
    cpf = input("DIGITE UM NUMERO DE CPF PARA CHECAGEM: ")
    novo_cpf = cpf[:-2]#retirando os 2 ultimos numeros do cpf
    reverso = 10
    total = 0

    for index in range(19):#19 é o numero de vezes que o for tem que fazer a volta para
        #cacular todos os valores
        if index > 8:
            index -= 9
        #to chamando a var de index pois o index equivale a cada
            #valor de cada caractere do cpf
        total += int(novo_cpf[index]) * reverso #acessando o cpf do novo index

        reverso -= 1  # decrementando cada valor
        if reverso < 2:
            reverso = 11
            digito = 11 - (total % 11)

            if digito > 9:
                digito = 0
            total = 0 #tem que zerar a var para que depois ele for fazer outra
            #volta ele precisa zerar a variável total
            novo_cpf += str(digito) #pois ele tá como inteiro, então precisamos
            #tranformá-lo em string
    if cpf == novo_cpf:
        print("O CPF DIGITADO É VALIDO")
    else:
        print("O NOVO CPF É INVALIDO")


