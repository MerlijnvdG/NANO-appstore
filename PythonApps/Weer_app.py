# @MerlijnvdG

import requests

print("=-=-=-=-=-=Weer App=-=-=-=-=-=")
def watishetweer(stad):
    # API key is gratis tot 1000 uses per dag, dan geeft hij de error dus daarom verberg ik de API niet
    url = f"http://api.openweathermap.org/data/2.5/weather?q={stad}&appid=8a8184912b3b9490db29ab97e19e1307&units=metric&lang=nl"

    spannendhoor = requests.get(url)

    if spannendhoor.status_code == 200:
        data = spannendhoor.json()
        main = data['main']
        weer = data['weather'][0]

        temperatuur = main['temp']
        gevoelstemperatuur = main['feels_like']
        luchtvochtigheid = main['humidity']
        beschrijving = weer['description']


        print(f"Het weer in {stad.capitalize()}:")
        print(f"Beschrijving: {beschrijving}")
        print(f"Temperatuur: {temperatuur}°C")
        print(f"Gevoelstemperatuur: {gevoelstemperatuur}°C")
        print(f"Luchtvochtigheid: {luchtvochtigheid}%")
    else:
        print("Kon geen weerinformatie ophalen. Controleer of de stad correct is ingevoerd.")


nogeenkeer = True
while nogeenkeer:
    stad = input("Voer de naam van de stad in waarvoor je het weer wilt opvragen: ").strip()
    watishetweer(stad)

    while True:
        nogeenkeer = input("Wil je nog een stad invullen? (ja/nee): ")
        if nogeenkeer.lower() == "ja":
            nogeenkeer = True
            break
        elif nogeenkeer.lower() == "nee":
            nogeenkeer = False
            print("Bedankt voor het gebruiken van de app!")
            break
        else:
            print("Ongeldige invoer. Voer 'ja' of 'nee' in.")


# Bron: Chatgpt-4
# Share: https://chatgpt.com/share/66febaf5-0e2c-8010-9db9-798dc2e423f2
# Doel: Te weten krijgen op welke manier ik een API request kan doen naar openweathermap met een stad, en welke link ik daarvoor moet gebruiken
# Bijdrage: Ik weet nu welke link ik moet gebruiken
# Prompt: hey, hoe kan ik in python een api request doen naar openweathermap?