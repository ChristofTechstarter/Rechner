def calc_area(width, height):
    return width * height


def flächeninhalt():
    while True:
        print("\nFlächeninhaltsrechner")
        print("Bitte wählen Sie eine der folgenden Optionen aus:")
        print("(1) Rechteck")
        print("(2) Zurück")
        try:
            auswahl = int(input("\nBitte wählen Sie Ihre Operation aus (1-6): "))

            if auswahl in [1]:

                zahl1 = float(input("Geben Sie die erste Zahl ein: "))
                zahl2 = float(input("Geben Sie die zweite Zahl ein: "))

                if auswahl == 1:
                    print(
                        f"Der Flächeninhalt eines Rechteckes beträgt: {calc_area(zahl1, zahl2)}"
                    )
            elif auswahl == 2:
                break
            else:
                print(
                    f"Ungültige Auswahl. Bitte wählen Sie eine Option zwischen 1 und 6."
                )

        except ValueError:
            print(f"Ungültige Eingabe. Bitte geben Sie eine Zahl ein.")
