import Skripte.grundrechenarten
import Skripte.winkelfunktionen
import Skripte.temperaturrechner


while True:
    print("\nWillkommen bei Christof's Rechner")
    print("Bitte wählen Sie eine der folgenden Optionen aus:")
    print("(1) Grundrechenfunktionen")
    print("(2) Winkelfunktionen")
    print("(3) Temperaturrechner")
    print("(4) Programm beenden")
    try:

        auswahl = int(input("\nBitte wählen Sie Ihre Operation aus (1-4): "))
        # Grundrechenarten
        if auswahl == 1:
            Skripte.grundrechenarten.grundrechenarten()
        # Winkelfunktionen
        elif auswahl == 2:
            Skripte.winkelfunktionen.winkelfunktion()
        # Temperaturrechner
        elif auswahl == 3:
            Skripte.temperaturrechner.temperraturrechnung()
        elif auswahl == 4:
            print(f"Der Rechner wird beendet. Auf Wiedersehen!")
            break
        else:
            print(f"Ungültige Auswahl. Bitte wählen Sie eine Option zwischen 1 und 4.")

    except ValueError:
        print(f"Ungültige Eingabe. Bitte geben Sie eine Zahl ein.")
