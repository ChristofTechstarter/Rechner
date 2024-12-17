import Skripte.grundrechenarten
import Skripte.winkelfunktionen
import Skripte.temperaturrechner
import Skripte.streckenumrechnung
import Skripte.flächeninhaltrechner
import Skripte.zahlensysteme


while True:
    print("\nWillkommen bei Christof's Rechner")
    print("Bitte wählen Sie eine der folgenden Optionen aus:")
    print("(1) Grundrechenfunktionen")
    print("(2) Winkelfunktionen")
    print("(3) Temperaturrechner")
    print("(4) Streckenumrechner")
    print("(5) Flächeninhaltsrechner")
    print("(6) Zahlensysteme")
    print("(7) Programm beenden")
    try:

        auswahl = int(input("\nBitte wählen Sie Ihre Operation aus (1-7): "))
        # Grundrechenarten
        if auswahl == 1:
            Skripte.grundrechenarten.grundrechenarten()
        # Winkelfunktionen
        elif auswahl == 2:
            Skripte.winkelfunktionen.winkelfunktion()
        # Temperaturrechner
        elif auswahl == 3:
            Skripte.temperaturrechner.temperraturrechnung()
        # Streckenumrechner
        elif auswahl == 4:
            Skripte.streckenumrechnung.streckenumrechnung()
        # Flächeninhaltsrechner
        elif auswahl == 5:
            Skripte.flächeninhaltrechner.flächeninhalt()
        elif auswahl == 6:
            Skripte.zahlensysteme.zahlensystem()
        # Beenden des Programmes
        elif auswahl == 7:
            print(f"Der Rechner wird beendet.")
            break
        else:
            print(f"Ungültige Auswahl. Bitte wählen Sie eine Option zwischen 1 und 7.")

    except ValueError:
        print(f"Ungültige Eingabe. Bitte geben Sie eine Zahl ein.")
