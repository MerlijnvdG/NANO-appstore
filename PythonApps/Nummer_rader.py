# @MerlijnvdG

import random

maxgetal = 30
aantalraden = 10

def maakint(intkeuze):
    try:
        int(intkeuze)
        return True
    except ValueError:
        print("\nVul alleen een getal in.")
        return False

def randomgetal(maxgetal):
    randomgetal = random.randint(1, maxgetal)
    return randomgetal

aantalkeuzesgehad = 1


def settings():
    global maxgetal, aantalraden
    while True:
        if maxgetal == 30:
            settingsmaxgetal = "30 (standaard)"
        else:
            settingsmaxgetal = maxgetal

        if aantalraden == 10:
            settingsaantalraden = "10 (standaard)"
        else:
            settingsaantalraden = aantalraden

        print("\n=-=-=-=-=-=Instellingen=-=-=-=-=-=")
        print(f"1: Maximaal getal: {settingsmaxgetal}")
        print(f"2: Aantal keer raden: {settingsaantalraden}")
        print("0: Terug")

        keuze = input("Kies een getal waarvan je de waarde wilt vervangen: ")

        if maakint(keuze):
            keuze = int(keuze)
        else:
            continue

        if keuze == 1:
            maxkeuze = input("Vul een nieuw maximaal getal in: ")
            if maakint(maxkeuze):
                maxgetal = int(maxkeuze)
            else:
                continue
        elif keuze == 2:
            maxgetalkeuze = input("Vul een nieuw aantal keer raden in: ")
            if maakint(maxgetalkeuze):
                aantalraden = int(maxgetalkeuze)
            else:
                continue
        elif keuze == 0:
            break

def menu():
    while True:
        print("\n=-=-=-=-=-=Menu=-=-=-=-=-=")
        print("1: Spelen")
        print("2: Instellingen")
        print("0: Afsluiten")
        menukeuze = input("Maak een keuze: ")
        if maakint(menukeuze):
            menukeuze = int(menukeuze)
        else:
            menu()
        if menukeuze == 1:
            jouwrandomgetal = randomgetal(maxgetal)
            spel(maxgetal, aantalraden, jouwrandomgetal)
        elif menukeuze == 2:
            settings()
        elif menukeuze == 0:
            break
        else:
            print("\nVul een geldig getal in.")
            menu()



def opnieuw(speel_opnieuw):
    if speel_opnieuw.lower() == "ja":
        jouwrandomgetal = randomgetal(maxgetal)
        global aantalkeuzesgehad
        aantalkeuzesgehad = 1
        spel(maxgetal, aantalraden, jouwrandomgetal)
        return True
    else:
        print("Oke, bedankt voor het spelen!")
        return False

def spel(maxgetal, aantalraden, jouwrandomgetal):
    global aantalkeuzesgehad

    while True:
        print("\n=-=-=-=-=-=Nummer raden=-=-=-=-=-=")
        jouwkeuze = input(f"({aantalkeuzesgehad}/{aantalraden}) Kies een getal: ")
        if maakint(jouwkeuze):
            jouwkeuze = int(jouwkeuze)
        else:
            continue

        if jouwrandomgetal == jouwkeuze:
            print("Je hebt het getal geraden, gefeliciteerd!")
            speel_opnieuw = input("Wil je nog een keer spelen? (ja/nee)")
            if not opnieuw(speel_opnieuw):
                print("Bedankt voor het spelen!")
                break

        else:
            if aantalkeuzesgehad != aantalraden:
                print("Helaas, je keuze is niet correct. Probeer nog een keer.")

        aantalkeuzesgehad += 1

        if aantalkeuzesgehad > aantalraden:
            print(f"Helaas! Je hebt verloren. Het getal was {jouwrandomgetal}")
            speel_opnieuw = input("Wil je nog een keer spelen? (ja/nee)")
            if not opnieuw(speel_opnieuw):
                print("Bedankt voor het spelen!")
                break


menu()
