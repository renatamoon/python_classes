#exercicio DE IDENTIFICAÇÃO DE PAR E IMPAR

# num = input("DIGITE UM NUMERO: ")
#
# if num.isdigit():
#     num = int(num)
#     if num % 2 == 0:
#         print("ESSE NUMERO É UM NUMERO PAR")
#     else:
#         print("ESSE NUMERO É UM NUMERO IMPAR")
# else:
#      print("ESSE NUMERO NÃO É UM NUMERO INTEIRO")

#EXERICIO PARA CHECAR O HORARIO E A SAUDAÇÃO APROPRIADA

# horario = input("DIGITE O HORARIO DAS 0 AS 23: ")
#
# if horario.isdigit():
#     horario = int(horario)
#     if horario <= 12:
#         print("BOM DIA, são {} HORAS".format(horario))
#     elif horario <= 17:
#         print("BOA TARDE, SÃO {} HORAS".format(horario))
#     else:
#         print("BOA NOITE, são {} HORAS".format(horario))
# else:
#     print("POR FAVOR DIGITE UM HORÁRIO ENTRE 0 E 23")

nome = input("DIGITE O SEU PRIMEIRO NOME: ").upper()
tamanho = len(nome)

if tamanho <= 4:
    print("SEU NOME É CURTO, {}".format(nome))
elif tamanho <= 6:
    print("SEU NOME É NORMAL, {}".format(nome))
else:
    print("SEU NOME É GRANDE, {}".format(nome))
