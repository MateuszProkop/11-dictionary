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
    
    elif (choice == "2"):
        key = input("Jakiej definicji szukasz? ")

        if key in definitions:
            print(definitions[key])
        else:
            print("Nie znaleziono takiej definicji ", key)
    
    elif (choice == "3"):
        key = input("Jaką definicję chcesz usunąć? ")

        if key in definitions:
            del definitions[key]
            print("Usunięto definicję - ", key)
        else:
            print("Nie znaleziono definicji o nazwie - ", key)

    elif (choice == "4"):
        for key in definitions:
            print(key)

    elif (choice == "5"):
        print("See you soon")
        break

    else:
        print("Podałeś niewłaściwą liczbę")