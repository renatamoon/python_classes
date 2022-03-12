#Curso de Python 3 - Mundo 1: Fundamentos
#aula de TIPOS PRIMITIVOS

n1 = int(input("Digite um valor: "))
n2 = int(input("Digite outro valor: "))

s = n1 + n2

#ha duas formas de se fazer esse print
print("A soma entre" , n1,  "e", n2, "vale", s)

#mas pode ser usado o .format que formata como
#você quer deixar o seu codigo

print("A soma entre {} e {} vale {}" .format(n1, n2, s))

#-----------float, str e boleano
n = float(input("Digite um valor: "))
print(n)

n = bool(input("Digite um valor"))
print(n)

#nessa parte somente vai dizer que é verdadeiro pois
#se digitarmos um valor de qualquer natureza vai dizer que
# é verdadeiro

#agora vamos verificar a validade de um numero
#que dirá se é verdadeiro ou falso

n = input("Digite qualquer coisa: ")
print(n.isnumeric()) #se é possivel converter esse
#valor em numero ou nao ...

#OU

n = input("Digite qualquer coisa: ")
print(n.isalpha()) #nesse caso diz que
#se o que você digitou no input é ou não
#alfabetico no caso tem letras
#colocando um resultado numerico sai um valor Falso
#colocando um resultado alfabetico sai um valor True








