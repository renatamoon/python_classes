#tratando exceções
# try:
#     a = {}
    #print(a[1]) #o try tentará gerar algum codigo dentro do primeiro
    #try, caso dê algum erro dentro desse try, ele vai para a parte de
# except NameError as erro: #except e executará o que estiver dentro
#     print("ERRO DO DESENVOLVEDOR", erro) #NameErro está definindo qual o tipo de erro
# except (IndexError, KeyError) as erro: #primeiro trata o erro de Index, e depois de dicionario
#     print("ERRO DE INDICE")
# except Exception as erro:
#     print("ocorreu um erro inesperado.")
# else:
#     print("Seu codigo foi executado com sucesso")
#     print(a)
# finally: #se ocorreu ou nao um erro sempre será executada
#     print("FINALMENTE")
#
# print('Bora continuar ...')
#execução:
# ERRO DO DESENVOLVEDOR name 'a' is not defined
# Bora continuar ...

#-----------------
try:
    a = 0
    try:
        a = 1/0
    except:
        print("ERRO")
except NameError as erro:
    print("ERRO DO DESENVOLVEDOR", erro)
except (IndexError, KeyError) as erro:
    print("erro de indice ou de chave")
except Exception as erro:
    print("ocorreu um erro inesperado")
else:
    pass
finally:
    a = ""

print(a)