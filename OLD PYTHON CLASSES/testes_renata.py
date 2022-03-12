'''from math import ceil

def media_aluno():
    nota_1 = 0
    for n in range(3):
        nota = float(input("INFORME A NOTA: "))
        nota_1 += nota
        media = nota_1 / 3
    if media >= 7:
        print("VOCÊ FOI APROVADO! SUA MEDIA É: ", ceil(media))
    else:
        print("VOCÊ NÃO FOI APROVADO, TENTE NOVAMENTE")
print(media_aluno())'''

#usando o loop while
notas = []
count = 1

while True:
    nota = float(input("DIGITE A NOTA" + str(count) +": "))
    notas.append(nota)
    count += 1


media = sum(notas) / len(notas)

if media >= 7:
    print("VOCÊ FOI APROVADO")
else:
    print("O ALUN0 FOI REPROVADO")

print("A media foi", media)


