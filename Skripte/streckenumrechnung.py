def km_to_miles(km):
    return km * float(0.621371)


def miles_to_km(m):
    return m / float(0.621371)


def streckenumrechnung():

    while True:

        print("\nStreckenumrechnung")
        print("Bitte wählen Sie eine der folgenden Optionen aus:")
        print("(1) Kilometer in Meilen umrechnen")
        print("(2) Meilen in Kilometer")
        print("(3) Zurück")
        try:
            auswahl = int(input("\nBitte wählen Sie Ihre Operation aus (1-3): "))
            if auswahl in [1, 2]:

                zahl1 = float(input("Geben Sie eine Zahl ein: "))

                if auswahl == 1:
                    print(f"{zahl1}km entsprechen {km_to_miles(zahl1)} Meilen!")
                elif auswahl == 2:
                    print(f"{zahl1} Meilen entsprechen {miles_to_km(zahl1)}km")
            elif auswahl == 3:
                break
            else:
                print(
                    f"Ungültige Auswahl. Bitte wählen Sie eine Option zwischen 1 und 3."
                )
        except ValueError:
            print(f"Ungültige Eingabe. Bitte geben Sie eine Zahl ein.")
