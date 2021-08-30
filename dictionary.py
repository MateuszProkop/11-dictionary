definitions = {}

while(True):
    print()
    print("Menu")
    print("1. Dodaj definicję")
    print("2. Wyszukaj definicję")
    print("3. Usuń definicję")
    print("4. Pokaż słownik")
    print("5. Zakończ")
    print()

    choice = input("Wybierz działanie: ")

    if (choice == "1"):
        key = input("Podaj słowo do zdefiniowania: ")
        definition = input("Podaj definicję: ")
        definitions[key] = definition
        print("Definicja została pomyślnie dodana!")
    
    if (choice == "2"):
        print("Wybrałeś 2")
    
    if (choice == "3"):
        print("Wybrałeś 3")

    if (choice == "4"):
        print("Wyświetl słownik")

    if (choice == "5"):
        print("See you soon")
        break

    else:
        print("Podałeś niewłaściwą liczbę")