def celsius_to_fahrenheit(x):
    return (x * (9 / 5)) + 32


def fahrenheit_to_celsius(x):
    return (x - 32) * (5 / 9)


def temperraturrechnung():

    while True:
        print("\nTemperaturrechner")
        print("Bitte wählen Sie eine der folgenden Optionen aus:")
        print("(1) Grad Celsius in Grad Fahrenheit")
        print("(2) Grad Fahrenheit in Grad Celsius")
        print("(3) Zurück")
        try:
            auswahl = int(input("\nBitte wählen Sie Ihre Operation aus (1-3): "))
            if auswahl in [1, 2]:
                zahl1 = float(input("Geben Sie eine Zahl ein: "))
            if auswahl == 1:
                print(f"{zahl1}°C entsprechen {celsius_to_fahrenheit(zahl1)}°F")
            elif auswahl == 2:
                print(f"{zahl1}°F entsprechen {fahrenheit_to_celsius(zahl1)}°C")
            elif auswahl == 3:
                break
            else:
                print(
                    f"Ungültige Auswahl. Bitte wählen Sie eine Option zwischen 1 und 3."
                )
        except ValueError:
            print(f"Ungültige Eingabe. Bitte geben Sie eine Zahl ein.")
