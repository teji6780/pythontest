import sys
import pandas


def transformer_pLieu(pLieu):
    # Transformation des caractères 2, 3 et 4
    def transformer_caractere(c):
        voyelles = "aeiouy"
        if c.isdigit():
            return 1 if int(c) % 2 != 0 else 2
        x = ord(c) - ord("a") + 1  # Position dans l'alphabet (1-indexé)
        if x > 5:
            return 1 if c not in voyelles else 2
        else:
            return x

    pLieu = pLieu.lower()
    n = len(pLieu) - 1
    result = []
    for i in [1, 2, 3]:
        if i >= 0:
            result.append(transformer_caractere(pLieu[i]))
    return result


def transformer_pQui(pQui):
    # Transformation des caractères n-2, n-1 et n
    def transformer_caractere(c):
        voyelles = "aeiouy"
        if c.isdigit():
            return 1 if int(c) % 2 != 0 else 2
        x = ord(c) - ord("a") + 1  # Position dans l'alphabet (1-indexé)
        if x > 5:
            return 1 if c not in voyelles else 2
        else:
            return x

    pQui = pQui.lower()
    n = len(pQui) - 1
    result = []
    for i in [n - 2, n - 1, n]:
        if i >= 0:
            result.append(transformer_caractere(pQui[i]))
    return result


def routine(a1, a2, a3, b1, b2, b3):
    # Routine libre : pour l'instant, concaténation des nombres
    return f"{a1}{a2}{a3}-{b1}{b2}{b3}"


def main():
    # Lecture des paramètres
    # pRand = int(input("Entrez le premier paramètre (pRand, entier) : "))
    if len(sys.argv) == 4:
        pRand = int(sys.argv[1])
        pLieu = sys.argv[2]
        pQui = sys.argv[3]
    else:
        pRand = int(input("Entrez le premier paramètre (pRand, entier) : "))
        pLieu = input("Entrez le deuxième paramètre (pLieu, chaîne) : ")
        pQui = input("Entrez le troisième paramètre (pQui, chaîne) : ")

    # Transformation de pLieu
    a1, a2, a3 = transformer_pLieu(pLieu)

    # Transformation de pQui
    b1, b2, b3 = transformer_pQui(pQui)

    # Passage à la routine et préparation du retour
    sRetour = routine(a1, a2, a3, b1, b2, b3)

    # Affichage de la sortie
    print("res:" + sRetour + str({a1 + b3}) + str({a2 + b2}) + str({a3 + b1}))
    # print(sRetour)


if __name__ == "__main__":
    main()
