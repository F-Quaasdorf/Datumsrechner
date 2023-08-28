from Greg2JulCal import GregorianToJulianCalendar
from Jul2GregCal import JulianToGregorianCalendar


class Main:

    # Start of the program.
    print("\n~~~~~ KALENDERRECHNER ~~~~~\n")
    print("Zur Umwandlung von Datumsangaben aus dem gregorianischen Kalender in den julianischen und umgekehrt.")
    print("Befehle:")
    print("\tgreg\tGregorianischer Kalender -> julianischer Kalender")
    print("\tjul\tJulianischer Kalender -> gregorianischer Kalender")
    print("\tEND\tBeenden des Programms\t")
    
    # The program loops until terminated by the user by entering 'END'.
    while True:
        try:
            choice = input("Wählen Sie den Modus der Umwandlung:\n> ")
            
            # The user can enter three commands, two for the conversion process, and 'END' to terminate the program.
            if choice.lower() == "greg":
                GregorianToJulianCalendar()
            elif choice.lower() == "jul":
                JulianToGregorianCalendar()
            elif choice.upper() == "END":
                print("Programm wird beendet")
                break
            
            # user info in case the user has entered a command other than 'greg', 'jul' or 'END'.
            else:
                print("\n\t| Ungültige Eingabe. Wählen Sie zwischen:\n\t|")
                print("\t| greg\tWandelt ein gregorianisches Datum in ein julianisches um.")
                print("\t| jul\tWandelt ein julianisches Datum in ein gregorianisches um.")
                print("\t| END\tBeendet das Programm.")
        
        except AttributeError as attr_err:
            print("\t| Eingabe konnte nicht verarbeitet werden.\n\t| ERROR:", attr_err)
