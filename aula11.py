#TRABALHANDO COM SISTEMA DE CORES

# print("\33[1;31;43m Olá, Mundo!\33[m")
# print("\33[4;30;45m Olá Mundo novamente!\33[m")
# print("\33[7;30m Olá mundo de novo!\30[m")

# a = 3
# b = 5
# print("OS VALORES SÃO \33[32m{} e \33[31m{}".format(a, b))

#TESTE 1

nome = "RENATA"
cores = {"limpa":"\33[m", 
"azul":"\33[34m", 
"amarelo":"\33[33m", 
"pretoebranco":"\33[7;30m"}

# print("OLÁ, MUITO PRAZER EM TE CONHECER, {}{}{}!!!".format("\33[4;34m", nome, "\33[m"))

print("OLÁ, MUITO PRAZER EM TE CONHECER, {}{}{}!!!".format(cores["azul"], nome, cores["limpa"]))