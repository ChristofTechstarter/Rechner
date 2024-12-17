import Skripte.grundrechenarten


import math


def sinus(x):
    return math.sin(math.radians(x))


def cos(x):
    return math.cos(math.radians(x))


def tan(x):
    return math.tan(math.radians(x))


def celsius_to_fahrenheit(x):
    return (x * (9 / 5)) + 32


def fahrenheit_to_celsius(x):
    return (x - 32) * (5 / 9)


def calculator():
    print("\nWillkommen bei Christof's Rechner")
    print("Bitte wählen Sie eine der folgenden Optionen aus:")
    print("(1) Grundrechenfunktionen")
    print("(2) Winkelfunktionen")
    print("(3) Temperaturrechner")
    print("(4) Programm beenden")


def winkelfunktionen():
    print("\nWinkelfunktionen")
    print("Bitte wählen Sie eine der folgenden Optionen aus:")
    print("(1) Sinusfunktion")
    print("(2) Kosinusfunktion")
    print("(3) Tangensfunktion")
    print("(4) Zurück")


def temperaturrechner():
    print("\nTemperaturrechner")
    print("Bitte wählen Sie eine der folgenden Optionen aus:")
    print("(1) Grad Celsius in Grad Fahrenheit")
    print("(2) Grad Fahrenheit in Grad Celsius")
    print("(3) Zurück")


while True:
    calculator()
    try:

        auswahl = int(input("\nBitte wählen Sie Ihre Operation aus (1-4): "))
        # Grundrechenarten
        if auswahl == 1:
            Skripte.grundrechenarten.grundrechenarten()
        # Winkelfunktionen
        elif auswahl == 2:
            while True:
                winkelfunktionen()
                try:
                    auswahl = int(
                        input("\nBitte wählen Sie Ihre Operation aus (1-4): ")
                    )
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
        # Temperaturrechner
        elif auswahl == 3:
            while True:
                temperaturrechner()
                try:
                    auswahl = int(
                        input("\nBitte wählen Sie Ihre Operation aus (1-3): ")
                    )
                    if auswahl in [1, 2]:
                        zahl1 = float(input("Geben Sie eine Zahl ein: "))
                        if auswahl == 1:
                            print(
                                f"{zahl1}°C entsprechen {celsius_to_fahrenheit(zahl1)}°F"
                            )
                        elif auswahl == 2:
                            print(
                                f"{zahl1}°F entsprechen {fahrenheit_to_celsius(zahl1)}°C"
                            )
                    elif auswahl == 3:
                        break
                    else:
                        print(
                            f"Ungültige Auswahl. Bitte wählen Sie eine Option zwischen 1 und 3."
                        )
                except ValueError:
                    print(f"Ungültige Eingabe. Bitte geben Sie eine Zahl ein.")
        elif auswahl == 4:
            print(f"Der Rechner wird beendet. Auf Wiedersehen!")
            break
        else:
            print(f"Ungültige Auswahl. Bitte wählen Sie eine Option zwischen 1 und 4.")

    except ValueError:
        print(f"Ungültige Eingabe. Bitte geben Sie eine Zahl ein.")
