def dezimal_to_bin(x):
    return bin(x)


def dezimal_to_hex(x):
    return hex(x)


def bin_to_dezimal(x):
    return int(x)


def bin_to_hex(x):

    return hex(x)


def hex_to_dezimal(x):
    return int(x)


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
                    print("Dezimal in Binär:")
                    print(f"{zahl1} entspricht: {dezimal_to_bin(zahl1).replace("0b", "")}")
                elif auswahl == 2:
                    print("Dezimal in Hex: ")
                    print(f"{zahl1} entspricht: {dezimal_to_hex(zahl1).replace("0x", "")}")
            elif auswahl in [3, 4]:

                zahl1 = int(input("Geben Sie eine Zahl ein: "), 2)

                if auswahl == 3:
                    print("Binär in Dezimal: ")
                    print(f"{bin(zahl1).replace("0b", "")} entspricht: {bin_to_dezimal(zahl1)}")
                elif auswahl == 4:
                    print("Binär in Hex: ")
                    print(f"{bin(zahl1).replace("0b", "")} entspricht: {bin_to_hex(zahl1).replace("0x", "")}")
            elif auswahl in [5, 6]:

                zahl1 = int(input("Geben Sie eine Zahl ein: "), 16)

                if auswahl == 5:
                    print("Hex in Dezimal: ")
                    print(f"{hex(zahl1).replace("0x", "")} entspricht: {hex_to_dezimal(zahl1)}")
                elif auswahl == 6:
                    print("Hex in Binär: ")
                    print(f"{hex(zahl1).replace("0x", "")} entspricht: {hex_to_bin(zahl1).replace("0b", "")}")
            elif auswahl == 7:
                break
            else:
                print(
                    f"Ungültige Auswahl. Bitte wählen Sie eine Option zwischen 1 und 7."
                )
        except ValueError:
            print(f"Ungültige Eingabe. Bitte geben Sie eine Zahl ein.")
