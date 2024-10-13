# @MerlijnvdG

import random

maakbestand = open("galgjewoorden.txt", "a+")
maakbestand.close()

woorden = []

def leeswoorden():
    global woorden
    with open("galgjewoorden.txt", "r") as lezen:
        allewoorden = lezen.read().strip().split(",")
    woorden = []
    for woord in allewoorden:
        woord = woord.strip()
        if woord:
            woorden.append(woord)
    return woorden

score = 0
def puntofpunten():
    global score
    if score == 1:
        return "punt"
    else:
        return "punten"


def kies_moeilijkheidsgraad():
    while True:
        keuze = input("Kies een moeilijkheidsgraad (makkelijk, gemiddeld, moeilijk): ").lower()
        if keuze == "makkelijk":
            return 2
        elif keuze == "gemiddeld":
            return 1.4
        elif keuze == "moeilijk":
            return 1
        else:
            print("Vul een geldige moeilijkheidsgraad in.")


def galgje(moeilijkheid):
    global score
    dewoorden = leeswoorden()
    if len(dewoorden) == 0:
        print("Het bestand met woorden is leeg. Vul zelf woorden in of gebruik de woorden uit mijn github 'MerlijnvdG'")
        return
    randomwoord = random.choice(dewoorden).lower()
    geradenletters = []
    lengtewoord = len(randomwoord)
    aantalfouten = (lengtewoord * moeilijkheid)
    aantalfouten = round(aantalfouten)
    fouten = 0
    print(f"Je mag {aantalfouten} fouten maken.")

    while fouten < aantalfouten:
        voortgang = []
        for letter in randomwoord:
            if letter in geradenletters:
                voortgang.append(letter)
            else:
                voortgang.append("_")

        woordvoortgang = "".join(voortgang)
        print(f"Woord: {woordvoortgang}")

        gok = input("Raad een letter: ").lower()

        if len(gok) != 1 or not gok.isalpha():
            print("Vul alleen een letter in.\n")
            continue

        if gok in geradenletters:
            print(f"Je hebt '{gok}' al geraden. Vul een andere letter in.\n")
            continue

        geradenletters.append(gok)

        if gok in randomwoord:
            print(f"Goed geraden! '{gok}' zit in het woord!")

        else:
            print(f"Helaas! '{gok}' zit niet in het woord.")
            fouten = fouten + 1

            if aantalfouten - fouten != 0:
                print(f"Je kan nog {aantalfouten - fouten} keer raden.")

        woord_geraden = True

        for letter in randomwoord:
            if letter not in geradenletters:
                woord_geraden = False
                break
        print()
        if woord_geraden:
            print(f"Woord: {randomwoord}")
            print(f"Gefeliciteerd! Je hebt het woord '{randomwoord}' geraden!")
            if moeilijkheid == 2:
                score += 6
                print(f"\nJe hebt 6 punten gewonnen! Je hebt nu {score} {puntofpunten()}.\n")
            elif moeilijkheid == 1.4:
                score += 8
                print(f"\nJe hebt 8 punten gewonnen! Je hebt nu {score} {puntofpunten()}.\n")
            else:
                score += 10
                print(f"\nJe hebt 10 punten gewonnen! Je hebt nu {score} {puntofpunten()}.\n")
            opnieuw()

    else:
        print(f"Je hebt verloren! Het woord was: '{randomwoord}'.")
        if moeilijkheid == 2:
            score -= 3
            if score < 0:
                score = 0
            print(f"\nJe hebt 3 punten verloren. Je hebt nu {score} {puntofpunten()}.\n")
        elif moeilijkheid == 1.4:
            score -= 5
            if score < 0:
                score = 0
            print(f"\nJe hebt 5 punten verloren. Je hebt nu {score} {puntofpunten()}.\n")
        else:
            score -= 10
            if score < 0:
                score = 0
            print(f"\nJe hebt 10 punten verloren. Je hebt nu {score} {puntofpunten()}.\n")

        opnieuw()

def opnieuw():
    while True:
        nogkeer = input(f"Wil je nog een keer spelen (ja/nee): ").lower()
        if nogkeer == "ja":
            print()
            galgje(moeilijkheid)
        elif nogkeer == "nee":
            print("Bedankt voor het spelen!")
            exit()
        else:
            print("Vul alleen ja of nee in.")


print("=-=-=-=-=-=Galgje=-=-=-=-=-=")
moeilijkheid = kies_moeilijkheidsgraad()
galgje(moeilijkheid)


# BRONNEN
# https://www.w3schools.com/python/ref_string_isalpha.asp#:~:text=The%20isalpha()%20method%20returns,are%20alphabet%20letters%20(a%2Dz).

# Bron: Chatgpt-4
# Share: https://chatgpt.com/share/670bded7-3ca4-8010-939f-0c9caa316d0c
# Doel: Veel galgje woorden krijgen zonder zelf daar heel veel tijd in te moeten steken
# Bijdrage: Veel galgje woorden
# Prompt: hoi, geef me 300 nederlandse woorden. Doe een beetje variatie in onderwerpen want het is voor een galgje spel. Doe het in dit formaat: woord, woord, woord, woord (etc)

