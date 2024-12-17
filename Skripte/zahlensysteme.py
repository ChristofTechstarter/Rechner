def dezimal_to_bin(x):
    return bin(x)


def dezimal_to_hex(x):
    return hex(x)


def bin_to_dezimal(x):
    return int(x, 2)


def bin_to_hex(x):

    return hex(x)


def hex_to_dezimal(x):
    return int(x, 16)


def hex_to_bin(x):
    return bin(x)


def zahlensystem():

    while True:

        print("\nZahlensysteme")
        print("Bitte wählen Sie eine der folgenden Optionen aus:")
        print("(1) Dezimal in Binär")
        print("(2) Dezimal in Hex")
        print("(3) Binär in Dezimal")
        print("(4) Binär in Hex")
        print("(5) Hex in Dezimal")
        print("(6) Hex in Binär")
        print("(7) Zurück")
        try:
            auswahl = int(input("\nBitte wählen Sie Ihre Operation aus (1-7): "))
            if auswahl in [1, 2]:

                zahl1 = int(input("Geben Sie eine Zahl ein: "))

                if auswahl == 1:
                    print(f"{zahl1} entspricht: {dezimal_to_bin(zahl1)}")
                elif auswahl == 2:
                    print(f"{zahl1} entspricht: {dezimal_to_hex(zahl1)}")
            elif auswahl in [3, 4]:

                zahl1 = int(input("Geben Sie eine Zahl ein: "), 2)

                if auswahl == 3:
                    print(f"{bin(zahl1)} entspricht: {bin_to_dezimal(zahl1)}")
                elif auswahl == 4:
                    print(f"{bin(zahl1)} entspricht: {bin_to_hex(zahl1)}")
            elif auswahl in [5, 6]:

                zahl1 = int(input("Geben Sie eine Zahl ein: "), 16)

                if auswahl == 5:
                    print(f"{hex(zahl1)} entspricht: {hex_to_dezimal(zahl1)}")
                elif auswahl == 6:
                    print(f"{hex(zahl1)} entspricht: {hex_to_bin(zahl1)}")
            elif auswahl == 7:
                break
            else:
                print(
                    f"Ungültige Auswahl. Bitte wählen Sie eine Option zwischen 1 und 7."
                )
        except ValueError:
            print(f"Ungültige Eingabe. Bitte geben Sie eine Zahl ein.")
