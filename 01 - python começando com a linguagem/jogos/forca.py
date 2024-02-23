
def jogar():

    print("*********************************")
    print("***Bem vindo no jogo de forca!***")
    print("*********************************")

    palavra_secreta = "banana"
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]

    enforcou = False
    acertou = False

    # enquanto True
    while not enforcou and not acertou:
        chute = input("Qual letra ")
        chute = chute.strip()

        index = 0

        for letra in palavra_secreta:
            if chute.upper() == letra.upper():
                
            index = index + 1

        print("Jogando...")

    print("Fim do jogo")


if __name__ == "__main__":
    jogar()
