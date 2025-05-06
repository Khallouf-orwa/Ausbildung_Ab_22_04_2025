import re
from datetime import datetime
def save_data(saved_person_dict,saved_person,type_dict):                # Eine Funktion, um die Eingaben in Dictionary zu speichern
    saved_person_dict[type_dict] = saved_person
    print("Ihre Eingabe wurde erfolgreich gespeichert\n")               # Eine Meldung, dass die Eingabe gespeichert ist
def choice_check(my_text):                                              # Eine Funktion, um die Benutzerwahl zu prüfen
    my_choice = input(my_text)                                          # Die Eingabe in Variable speichern
    if my_choice.isdecimal():                                           # Prüfen, ob die Eingabe eine Zahl ist
        my_choice = int(my_choice)                                      # Die eingabe zu Integer wechseln
        return my_choice                                                # Die Eingabe zurückgeben
    else:
        print("Ungültige Eingabe\n")                                    # Eine Fehlermeldung
        return None
def is_valide(my_input,pattern_position):                                                               # Eine Funktion, um Eingaben zu prüfen
    pattern = [r"^\s*[A-Za-zäöüÄÖÜß\s]{2,}\s*$",
               r"^\s*([A-Za-zäöüÄÖÜß\s]+)\s+(\d+[A-Za-z]?)\s*,\s*(\d{4})\s+([A-Za-zäöüÄÖÜß\s]+)\s*$",
               r"^0\d{1,4}\s\d{6,8}$",
               r"^(?!.*\.\.)(?!\.)(?!.*\.$)[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"]            # Regex Liste für erlaubte zeichen
    match_ = re.fullmatch(pattern[pattern_position],my_input)                                           # Die Eingabe mit dem regex vergleichen
    if match_:
        return True
    else:                                                                # Fehlermeldungen
        match pattern_position:
            case 0:
                print("Ungültige Eingabe, geben Sie bitte Vorname und Nachname mit einer Leerzeichen inzwischen ein\n")
            case 1:
                print("Ungültige Eingabe, geben Sie bitte eine Adresse in dem richtigen Form ein")
            case _:
                print("Ungültige Eingabe\n")
        return False
def is_valide_date(my_date):                                                    # Eine Funktion, um das Geburtsdatum zu prüfen
    try:
        my_birthday = datetime.strptime(my_date,"%d.%m.%Y")              # Die Eingabe mit Datumsform vergleichen
        if my_birthday and my_birthday < datetime.today():
            return True
        else:                                                                   # Fehlermeldungen
            print("Ungültige Eingabe, Geben Sie bitte das Datum in der Vergangenheit\n")
            return False
    except ValueError:
        print("Ungültige Eingabe, Geben Sie bitte das Datum in dem richtigen Form ein\nTT.MM.JJJJ\n")
        return False
def show_data(my_list,my_type = None,my_filter = None):                         # Eine Funktion, um gespeicherte Daten zu zeigen
    counter = 1                                                                 # Ein Datenzähler
    for my_person in my_list:                                                   # Die Personen Dictionary in der Liste durchführen
        if my_type and my_person.get("type") != my_type:                        #Überspringt Einträge, wenn sie nicht dem gewünschten Typ entsprechen.
            continue
        if my_filter:                                                           # wenn Filter eingegeben wird
            print(f"{counter}. {my_person.get(my_filter)}\n")                   #Daten nach Filtereingabe zeigen
        else:                                                                   # wenn kein Filter eingegeben wird
            print(f"{counter}. Name: {my_person.get('name')}\nAdresse: {my_person.get('address')}\n"
                  f"Geburtsdatum: {my_person.get('birthday')}\nTelefonnummer: {my_person.get('phone')}\n"
                  f"E-Mail: {my_person.get('email')}\n")                        # alle Daten werden gezeigt
        counter += 1
    if counter == 1:
        print("Keine Daten gefunden\n")
def change_data(my_data_dict,my_new_data,my_key):
    my_data_dict[my_key] = my_new_data
    print("Die Datei wurde erfolgreich geändert\n")

print("Mitarbeiter*innen und Besucher*innen Daten\n")    #Programm Name
persons_list = []                                        # Eine Datenliste, um Dictionary zu speichern
while True:                                              # Eine Menüliste zeigen
    user_input = choice_check("Drücken Sie bitte 1, um neue Mitarbeiterdatei oder Besucherdatei hinzufügen\n"
                              "Drücken Sie bitte 2, um die Personendaten zu zeigen\n"
                              "Drücken Sie bitte 3, um Daten zu ändern\n"
                              "Drücken Sie bitte 4, Programm zu schlissen\n")
    match user_input:
        case 1:                                                     # Erste Wahl (Eine neue Datei einfügen)
            person_dict = {}                                        # Dictionary entleeren
            while True:
                while True:                                         # Meine Funktion aufrufen
                    choice = choice_check("Mitarbeiter*inne drücken Sie bitte 1\nBesucher*innen drücken Sie bitte 2\n")
                    if choice == 1:                                 # wenn, die erste Wahl
                        person_dict["type"] ="Mitarbeiter*innen"    # Die Type in Dictionary als Mitarbeiter*innen setzen
                        break
                    elif choice == 2:                               # wenn, die zweite Wahl
                        person_dict["type"] = "Besucher*innen"      # Die Type in Dictionary als Besucher*innen setzen
                        break
                while True:                                         # Wiederholen bis die erste Eingabe erfüllt ist
                    name = input("Geben Sie bitte eine vollständige Name ein:\n").strip()
                    if is_valide(name,0):                     # Meine Funktion aufrufen, um die Eingabe zu prüfen
                        name = name.title()                                 # Der erste Buchstabe als groß setzen
                        save_data(person_dict, name, "name")       # Meine Funktion aufrufen, um die Eingabe in dictionary zu speichern
                        break
                while True:                                                 # Wiederholen bis die Eingabe erfüllt ist
                    address = input("Geben Sie bitte eine vollständige Adresse ein:\n"
                                    "Muster (musterstraße 03, 3333 musterort)\n").strip()
                    if is_valide(address,1):                                # Meine Funktion aufrufen, um die Eingabe zu prüfen
                        save_data(person_dict, address, "address")               # Meine Funktion aufrufen, um die Eingabe in dictionary zu speichern
                        break
                while True:
                    birthday = input("Geben Sie bitte eine vollständige Geburtsdatum ein:\nMuster TT.MM.JJJJ\n").strip()
                    if is_valide_date(birthday):                                   # Meine Funktion aufrufen, um die Eingabe zu prüfen
                        save_data(person_dict,birthday,"birthday")        # Meine Funktion aufrufen, um die Eingabe in dictionary zu speichern
                        break
                while True:
                    phone = input("Geben Sie bitte eine Telefonnummer ein:\nMuster 0123 123456\n").strip()
                    if is_valide(phone,2):                          # Meine Funktion aufrufen, um die Eingabe zu prüfen
                        save_data(person_dict,phone,"phone")             # Meine Funktion aufrufen, um die Eingabe in dictionary zu speichern
                        break
                while True:
                    email = input("Geben Sie bitte eine E-Mail Adresse ein:\nMuster: muster@gmail.com\n").strip()
                    if is_valide(email,3):                                 # Meine Funktion aufrufen, um die Eingabe zu prüfen
                        save_data(person_dict,email,"email")                    # Meine Funktion aufrufen, um die Eingabe in dictionary zu speichern
                        break
                persons_list.append(person_dict.copy())
                print("Eine Mitarbeiter*innen Daten wurden erfolgreich gespeichert\n")              # Eine Meldung, wenn alle Eingaben gespeichert sind
                user_input = choice_check("Drücken Sie bitte 1, um noch eine Mitarbeiterdaten wieder hinzufügen\n"
                                          "Drücken Sie bitte andere Taste, um Die Menüliste wieder zu zeigen\n")
                if user_input == 1:
                    continue
                else:
                    break
        case 2:
            while True:                     # Wiederholen bis die Eingabe erfüllt ist
                choice = choice_check("Mitarbeiter*innen drücken Sie bitte 1\n"         # Meine Funktion aufrufen, um die Eingabe zu prüfen und in Variable speichern
                                      "Besucher*innen drücken Sie bitte 2\n"
                                      "Filtern: Drücken Sie bitte 3\n")
                if choice == 1:
                    show_data(persons_list,"Mitarbeiter*innen")                 # Meine Funktion aufrufen, um die Daten zu zeigen
                    break
                elif choice == 2:
                    show_data(persons_list,"Besucher*innen")                    # Meine Funktion aufrufen, um die Daten zu zeigen
                    break
                elif choice == 3:                                               # Meine Funktion aufrufen, um die Eingabe zu prüfen und in Variable speichern
                    type_filter = choice_check("Mitarbeiter*innen : Drücken Sie bitte 1\nBesucher*innen : Drücken Sie bitte 2\n")
                    person_type = "Mitarbeiter*innen" if type_filter ==1 else "Besucher*innen"      # Personen type nach Benutzerwahl setzen
                    choice_filter = choice_check("Drücken Sie eine Nummer der folgenden Filter\n"
                                                 "1.Name\n2.Adresse\n3.Geburtsdatum\n"              # meine Funktion aufrufen, um Filterwahl in Variable zu speichern
                                                 "4.Telefonnummer\n5.E-Mail\n")
                    filters = {1:"name",2:"address",3:"birthday",4:"phone",5:"email"}               # Ein Dictionary mit Integer Schlüssel, die meine Schlüssel erhalten
                    user_filter = filters.get(choice_filter)
                    if user_filter:
                        show_data(persons_list,person_type,user_filter)                             # Meine Funktion aufrufen, um die Daten zu zeigen
                        break
                    else:
                        print("Ungültige Eingabe\n")
                        continue
        case 3:                                                     # Daten ändern
            while True:
                change_key = input("Geben Sie der Name der Person, die Sie ihre Daten ändern möchten\n").strip().title()
                if is_valide(change_key,0):                                                # Meine Funktion aufrufen, um die Eingabe zu prüfen
                    for person in persons_list:                                                         # Die Personen in der Liste Durchführen
                        if person["name"] == change_key:                                                # die Eingabe mit gespeicherten Daten vergleichen
                            print(f"Name: {person.get('name')}\nAdresse: {person.get('address')}\n"     # Die passende Datei zeigen
                                  f"Geburtsdatum: {person.get('birthday')}\nTelefonnummer: {person.get('phone')}\n"
                                  f"E-Mail: {person.get('email')}\n")
                            choice_change = choice_check("Drücken Sie eine Nummer der folgenden Daten\n"
                                                         "1.Name\n2.Adresse\n3.Geburtsdatum\n"          # Funktion aufrufen, um die Benutzerwahl zu prüfen und speichern
                                                         "4.Telefonnummer\n5.E-Mail\n")
                            match choice_change:
                                case 1:
                                    while True:
                                        new_name = input("Geben Sie bitte eine vollständige Name ein:\n").strip()
                                        if is_valide(new_name, 0):                      # Meine Funktion aufrufen, um die Eingabe zu prüfen
                                            name = new_name.title()                                  # Der erste Buchstabe als groß setzen
                                            change_data(person,new_name,"name")
                                            break
                                case 2:
                                    while True:
                                        new_address = input("Geben Sie bitte eine vollständige Adresse ein:\n"
                                                            "Muster (musterstraße 03, 3333 musterort)\n").strip()
                                        if is_valide(new_address, 1):                           # Meine Funktion aufrufen, um die Eingabe zu prüfen
                                            change_data(person,new_address,"address")
                                            break
                                case 3:
                                    while True:
                                        new_birthday = input("Geben Sie bitte eine vollständige Geburtsdatum ein:\n"
                                                             "Muster TT.MM.JJJJ\n").strip()
                                        if is_valide_date(new_birthday):                                     # Meine Funktion aufrufen, um die Eingabe zu prüfen
                                            change_data(person, new_birthday, "birthday")
                                            break
                                case 4:
                                    while True:
                                        new_phone = input("Geben Sie bitte eine Telefonnummer ein:\nMuster 0123 123456\n").strip()
                                        if is_valide(new_phone, 2):                            # Meine Funktion aufrufen, um die Eingabe zu prüfen
                                            change_data(person, new_phone, "phone")
                                            break
                                case 5:
                                    while True:
                                        new_email = input("Geben Sie bitte eine E-Mail Adresse ein:\nMuster: muster@gmail.com\n").strip()
                                        if is_valide(new_email, 3):                           # Meine Funktion aufrufen, um die Eingabe zu prüfen
                                            change_data(person, new_email, "email")
                                            break
                                case _:
                                    print("Ungültige Eingabe\n")
                                    continue
                break
        case 4:
            break
        case _:
            continue