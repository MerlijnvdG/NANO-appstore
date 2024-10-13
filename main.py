# @MerlijnvdG

import os
import subprocess

huidigedir = os.getcwd()
gamesfolder = os.path.join(huidigedir, "PythonApps")
folderbestaat = os.path.exists(gamesfolder)

if not folderbestaat:
    os.makedirs(gamesfolder)
    print("De folder met python apps bestond nog niet en is nu aangemaakt. Deze is dus nog wel leeg dus kan je geen app starten. Vind de folder met mijn games en verdere uitleg op: 'https://github.com/MerlijnvdG/NANO-appstore'.")
    exit()

while True:
    dirlijst = os.listdir(gamesfolder)
    pythonlijst = []
    for file in dirlijst:
        if file.endswith(".py"):
            pythonlijst.append(file)


    if len(pythonlijst) == 0:
        print("Er zitten geen (python) apps in de folder PythonApps. Maak je eigen .py app of voeg er een toe uit mijn repository: 'https://github.com/MerlijnvdG/NANO-appstore'.")
        exit()

    print("\nSelecteer een app om uit te voeren (of voer '0' in om af te sluiten):")
    for aantal, app in enumerate(pythonlijst):
        selectieapp = app.replace("_", " ").replace(".py", "")
        print(f"{aantal + 1}. {selectieapp}")
    print("0. Afsluiten")

    try:
        keuze = int(input("Voer het nummer in van de app die je wilt starten: "))
        if keuze == 0:
            print("Programma afgesloten.")
            break
        elif 1 <= keuze <= len(pythonlijst):
            geselecteerde_app = pythonlijst[keuze - 1]
            naam_geselecteerde_app = geselecteerde_app.replace("_", " ").replace(".py", "")

            app_plek = os.path.join(gamesfolder, geselecteerde_app)
            print(f"Starten van {naam_geselecteerde_app}...\n")

            try:
                subprocess.run(['python', app_plek], cwd=gamesfolder)
                print(f"\n{naam_geselecteerde_app} is afgesloten.")
            except:
                print(f"Er is een fout opgetreden tijdens het uitvoeren van {naam_geselecteerde_app}.")

            print(f"\n{naam_geselecteerde_app} is afgesloten.")
        else:
            print("Ongeldige keuze, probeer opnieuw.")
    except ValueError:
        print("Ongeldige invoer, voer een nummer in.")


# BRON
# https://www.datacamp.com/tutorial/python-subprocess
# https://stackoverflow.com/questions/1685157/how-can-i-specify-working-directory-for-a-subprocess
# https://www.geeksforgeeks.org/enumerate-in-python/


