# @MerlijnvdG

import random


def spsreal():
    while True:
        print("\n=-=-=-=-=-=Steen Papier Schaar=-=-=-=-=-=")
        keuze = input("Steen, papier of schaar (of 0 om te stoppen): ").capitalize()
        lijst = ["Steen", "Papier", "Schaar"]
        botkeuze = random.choice(lijst)
        if keuze == "0":
            print("Bedankt voor het spelen!")
            break
        vergelijken(keuze, botkeuze)

def vergelijken(keuze, botkeuze):
    if keuze == botkeuze:
        print(f"Jullie hebben gelijkspel! Het was {botkeuze}. Probeer opnieuw.")
    elif keuze == "Steen":
        if botkeuze == "Papier":
            print(f"Je hebt verloren! Het was {botkeuze}. Probeer opnieuw.")
        else:
            print(f"Je hebt gewonnen! Het was {botkeuze}. Speel nog een keer!")
    elif keuze == "Papier":
        if botkeuze == "Schaar":
            print(f"Je hebt verloren! Het was {botkeuze}. Probeer opnieuw.")
        else:
            print(f"Je hebt gewonnen! Het was {botkeuze}. Speel nog een keer!")
    elif keuze == "Schaar":
        if botkeuze == "Steen":
            print(f"Je hebt verloren! Het was {botkeuze}. Probeer opnieuw.")
        else:
            print(f"Je hebt gewonnen! Het was {botkeuze}. Speel nog een keer!")
    else:
        print("Ongeldige keuze. Kies opnieuw uit Steen, Papier, Schaar of 0.")


def spsrigged():
    while True:
        keuze = input("\nSteen, papier of schaar (of 0 om te stoppen): ").capitalize()
        botkeuze = ""
        if keuze == "Steen":
            botkeuze = "Papier"
        elif keuze == "Papier":
            botkeuze = "Schaar"
        elif keuze == "Schaar":
            botkeuze = "Steen"
        elif keuze == "0":
            print("Bedankt voor het spelen!")
            break
        vergelijken(keuze, botkeuze)


def start():
    while True:
        goed = input("Ben je goed in dit spel? (ja/nee): ").capitalize()
        if goed == "Ja":
            spsrigged()
            break
        elif goed == "Nee":
            spsreal()
            break
        else:
            print("Antwoord alleen met ja of nee.")


start()