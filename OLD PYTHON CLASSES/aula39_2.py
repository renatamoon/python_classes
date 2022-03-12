secreto = "perfume"
digitadas = []
chances = 3
while True:
    if chances <= 0:
        print("VOCÊ PERDEU")
        break

    letra = input("DIGITE UMA LETRA:")

    if len(letra) > 1:
        print("ISSO NÃO VALE, DIGITE APENAS UMA LETRA!")
        continue

    digitadas.append(letra)

    if letra in secreto:
        print("A LETRA {} EXISTE NA PALAVRA SECRETA!".format(letra))
    else:
        print("A LETRA {} NÃO FAZ PARTE DA PALAVRA SECRETA!".format(letra))
        digitadas.pop()

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'
    if secreto_temporario == secreto:
        print("VOCÊ GANHOU O JOGUINHO! ACERTOU A PALAVRA")
        break
    else:
        print("VOCÊ NÃO GANHOU, A PALAVRA SECRETA É {}".format(secreto_temporario))

    if letra not in secreto:
        chances -= 1
    print("VOCÊ AINDA TEM {} chances restantes".format(chances))
