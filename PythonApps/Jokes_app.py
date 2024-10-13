# @MerlijnvdG

import requests
import time

warning = True

def ikwileengrapje(stringsoortgrap):
    url = f"https://v2.jokeapi.dev/joke/{stringsoortgrap}"
    oehgrappig = requests.get(url)
    print()

    if oehgrappig.status_code == 200:
        data = oehgrappig.json()
        type = data["type"]
        if type == "twopart":
            print(data["setup"])
            time.sleep(3)
            print("")
            print(data["delivery"])
        elif type == "single":
            print(data["joke"])
        womp = False
        while not womp:
            again = input("\nWil je nog een grap? (ja/nee) ")
            if again.lower() == "ja":
                womp = True
                ikwileengrapje(stringsoortgrap)
            elif again.lower() == "nee":
                womp = True
                print("Bedankt voor het gebruiken van deze app!")
                startmenu()
            else:
                print("Vul alleen ja of nee in.")
                womp = False
    else:
        print("Kon helaas geen grap genereren. Probeer later opnieuw.")
        ikwileengrapje(stringsoortgrap)


def startmenu():
    stringsoortgrap = ""
    global warning
    print("\n=-=-=-=-=-=Jokes=-=-=-=-=-=")
    print("Wat voor soort grapje wil je?")
    print("1: Programming grap")
    print("2: Dark humor grap")
    print("3: Woordspelling grap")
    print("4: Spooky grap")
    print("5: Kerst grap")
    print("6: Alles")
    print("0: Afsluiten")

    soortgrap = input("Maak een keuze: ")
    try:
        soortgrap = int(soortgrap)
    except ValueError:
        print("Verkeerde invoer. Probeer opnieuw.")
        startmenu()
    soortgrap = int(soortgrap)
    if soortgrap == 1:
        stringsoortgrap = "Programming"
    elif soortgrap == 2:
        if warning:
            warningtext = ""
            while warningtext != "ja" and warningtext != "nee":
                warningtext = input("LET OP: deze grapjes kunnen gevoelige inhoud bevatten. Weet je zeker dat je door wilt gaan (ja/nee): ")
                if warningtext.lower() == "ja":
                    warning = False
                elif warningtext.lower() == "nee":
                    warning = True
                    startmenu()
                else:
                    print("Vul alleen ja of nee in.")
        stringsoortgrap = "Dark"
    elif soortgrap == 3:
        stringsoortgrap = "Pun"
    elif soortgrap == 4:
        stringsoortgrap = "Spooky"
    elif soortgrap == 5:
        stringsoortgrap = "Christmas"
    elif soortgrap == 6:
        stringsoortgrap = "Any"
    elif soortgrap == 0:
        print("Bedankt voor het gebruiken van deze app!")
        exit()
    else:
        print("Vul een waarde tussen 0 en 6 in.")
        startmenu()
    ikwileengrapje(stringsoortgrap)
startmenu()
