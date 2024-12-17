import math


def sinus(x):
    return math.sin(math.radians(x))


def cos(x):
    return math.cos(math.radians(x))


def tan(x):
    return math.tan(math.radians(x))


def winkelfunktion():

    while True:

        print("\nWinkelfunktionen")
        print("Bitte wählen Sie eine der folgenden Optionen aus:")
        print("(1) Sinusfunktion")
        print("(2) Kosinusfunktion")
        print("(3) Tangensfunktion")
        print("(4) Zurück")
        try:
            auswahl = int(input("\nBitte wählen Sie Ihre Operation aus (1-4): "))
            if auswahl in [1, 2, 3]:

                zahl1 = float(input("Geben Sie eine Zahl ein: "))

                if auswahl == 1:
                    print(f"Das Ergebnis der Sinusfunktion ist: {sinus(zahl1)}")
                elif auswahl == 2:
                    print(f"Das Ergebnis der Kosinusfunktion ist: {cos(zahl1)}")
                elif auswahl == 3:
                    print(f"Das Ergebnis der Tangensfunktion ist: {tan(zahl1)}")
            elif auswahl == 4:
                break
            else:
                print(
                    f"Ungültige Auswahl. Bitte wählen Sie eine Option zwischen 1 und 4."
                )
        except ValueError:
            print(f"Ungültige Eingabe. Bitte geben Sie eine Zahl ein.")
