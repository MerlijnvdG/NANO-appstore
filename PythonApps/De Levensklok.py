# @MerlijnvdG

import random
import time

print("Welkom bij de Levensklok!")
print("Ik zal je nu een paar vragen stellen,")
print("met die antwoorden ga ik berekenen wanneer jij doodgaat.")
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
while True:
    name = input("Mijn naam is: ")
    age = ""

    while type(age) is not type(1): #type(1) is eigenlijk type(int)
        ans = (input("Mijn leeftijd is: "))
        try:
            age = int(ans)
        except ValueError:
            print("Vul alleen een getal in.")
            continue

    jaar = ""
    while type(jaar) is not type(1):
        jaar = int(input("Ik zit nu in het jaar: "))
        try:
            jaar = int(jaar)
        except ValueError:
            print("Vul alleen een getal in.")
            continue

    wachttijd = int(random.randrange(1, 7))
    maxleeftijd = int(random.randrange(100, 120))
    leeftijddood = random.randrange(int(age) , maxleeftijd)
    jaardood = jaar + int(leeftijddood) - age
    maanden = ["januari", "februari", "maart", "april", "mei", "juni", "juli", "augustus", "september", "oktober", "november", "december"]
    maand = random.choice(maanden)
    dag = int(random.randrange(1, 28))
    jarenover = leeftijddood - age
    dood_manieren = ["verdrinken", "vallen van grote hoogte", "vergiftiging", "een verkeersongeval", "een hartaanval", "verstikking", "een overdosis drugs", "brandwonden", "een elektrische schok", "een mislukte parachutesprong", "oude leeftijd", "zelfmoord", "verpletterd worden door een zwaar object", "een natuurramp (bijv. aardbeving, tsunami)", "hypothermie", "uitdroging", "verhongeren", "giftige gasinademing", "medisch falen tijdens een operatie", "een kogelwond", "mishandeling", "opgegeten worden door wilde dieren", "een infectieziekte", "kanker", "een terroristische aanslag", "een beroerte", "vergiftigd voedsel", "nierfalen", "een botsing met een trein", "een vliegtuigcrash", "de ontsporing van een achtbaan", "een snorkel-ongeluk", "een val in een vulkaan", "verpletterd worden door een lawine", "bijtende dieren zoals slangen", "wegspoelen door een overstroming", "geraakt worden door bliksem", "gevangen zitten in een instortend gebouw", "overlijden aan hitte-uitputting", "een hitteberoerte", "verdrinken in drijfzand", "een ongeluk met een vuurwapen", "een explosie", "neergestoken worden", "een fataal auto-ongeluk", "radiationvergiftiging", "sneeuwstorm onderkoeling", "gebeten worden door giftige insecten", "de ontploffing van een gaslek", "overlijden door marteling", "uithongeren in een gevangeniscel", "verstikking door marshmallows", "overlijden na een episch Fortnite-gevecht", "proberen Superman te zijn vanaf een dak", "verpletterd worden door een vallende piano", "te hard lachen en niet meer kunnen ademen", "proberen een cactus te knuffelen", "te lang naar de zon staren", "een overdosis koffie na een all-nighter", "een ongeluk met een badkuip vol pudding", "verdrinken in een zwembad van bier", "verstikking door een gigantische kauwgombel", "verpletterd worden door een enorme stapel pizzadozen", "overlijden door een zenuwinzinking tijdens IKEA-meubelmontage", "uitglijden op een bananenschil", "proberen een selfie te maken met een agressieve geit"]
    manierdood = random.choice(dood_manieren)



    input("Eet je gezond: ")
    input("Aantal broers of zussen: ")
    input("Aantal keer sporten per week: ")
    print("Levensduur berekenen...")
    time.sleep(wachttijd)
    print("\n")
    print(f"Hallo " + str(name) + ".")
    print(f"Jij gaat dood als je " + str(leeftijddood) + " bent op " + str(dag) + " " + str(maand) + " " + str(jaardood),". Dat is over " + str(jarenover) + " jaar.")
    print(f"Jij overlijd door {manierdood}.")
    if jarenover <= 10:
        print("Ga maar alvast aftellen")

    while True:
        again = input("\nWil je de levensklok nog een keer gebruiken (ja/nee): ").lower()
        if again == "ja":
            print()
            break
        elif again == "nee":
            print("Bedankt voor het gebruiken van de levensklok!")
            exit()
        else:
            print("Vul alleen ja of nee in.")


