import re
import tkinter as tk
from tkinter.ttk import Label, Entry
from tkinter import messagebox, Scrollbar, Listbox
import json
from datetime import datetime

def is_valide(my_input,pattern_position,my_label):                      # Eine Funktion, um Eingaben zu prüfen
    pattern = [r"^\s*[A-Za-zäöüÄÖÜß\s]{1,}\s*$",
               r"^\s*([A-Za-zäöüÄÖÜß\s]+)\s+(\d+[A-Za-z]?)\s*,\s*(\d{4})\s+([A-Za-zäöüÄÖÜß\s]+)\s*$",
               r"^0\d{1,4}\s\d{6,8}$",                                  # Regex Liste für erlaubte zeichen
               r"^(?!.*\.\.)(?!\.)(?!.*\.$)[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"]
    match_ = re.fullmatch(pattern[pattern_position],my_input)           # Die Eingabe mit dem regex vergleichen
    if match_:
        return True
    else:                                                               # Fehlermeldungen
        match pattern_position:
            case 0:
                my_label.config(text="Ungültige Eingabe, geben Sie bitte für Vorname oder Nachname nur Buchstaben ein")
            case 1:
                my_label.config(text="Ungültige Eingabe, geben Sie bitte eine Adresse in dem richtigen Form ein musterstraße 03, 3333 musterort")
            case 2:
                my_label.config(text="Ungültige Eingabe, geben Sie bitte eine gültige Telefonnummer ein")
            case _:
                my_label.config(text="Ungültige Eingabe, geben Sie bitte eine gültige E-Mail Adresse ein")
        return False

def is_valide_date(my_date,my_label):                                           # Eine Funktion, um das Geburtsdatum zu prüfen
    try:
        my_birthday = datetime.strptime(my_date,"%d.%m.%Y")              # Die Eingabe mit Datumsform vergleichen
        if my_birthday and my_birthday < datetime.today():
            return True
        else:                                                                   # Fehlermeldungen
            my_label.config(text="Ungültige Eingabe, Geben Sie bitte das Datum in der Vergangenheit")
            return False
    except ValueError:
        my_label.config(text="Ungültige Eingabe, Geben Sie bitte das Datum in dem richtigen Form ein TT.MM.JJJJ")
        return False

def show_data(my_list,my_type = None,my_filter = None):                         # Eine Funktion, um gespeicherte Daten zu zeigen
    my_list.delete(0, tk.END)
    counter = 1                                                                 # Ein Datenzähler
    try:
        with open("person.json", "r", encoding="utf-8") as show_person:
            persons_data = json.load(show_person)
            for person in persons_data:
                if isinstance(person,dict):
                    if my_type and person.get("type") != my_type:               # Überspringt Einträge, wenn sie nicht dem gewünschten Typ entsprechen.
                        continue
                    if my_filter:                                               # wenn Filter eingegeben wird
                        value = person.get(my_filter, "Nicht vorhanden")
                        my_list.insert(tk.END, f"{counter}. {value}")
                    else:
                        my_list.insert(tk.END, f"{counter}.")
                        my_list.insert(tk.END, f"  Vorname: {person.get("first_name", "-")}")
                        my_list.insert(tk.END, f"  Nachname: {person.get("family_name", "-")}")
                        my_list.insert(tk.END, f"  Adresse: {person.get("address", "-")}")
                        my_list.insert(tk.END, f"  Geburtsdatum: {person.get("birthday", "-")}")
                        my_list.insert(tk.END, f"  Telefonnummer: {person.get("phone", "-")}")
                        my_list.insert(tk.END, f"  E-Mail: {person.get("email", "-")}")
                        my_list.insert(tk.END, "")
                    counter += 1
            if counter ==1:
                my_list.insert(tk.END, "Keine passenden Daten gefunden.")
    except FileNotFoundError:
        my_list.insert(tk.END,"Datei 'person.json' nicht gefunden.")
    except json.JSONDecodeError:
        my_list.insert(tk.END,"Fehler beim Lesen der JSON-Datei")

def save_list(my_list):
    with open("person.json", "w", encoding="utf-8") as person:
        json.dump(my_list, person, ensure_ascii=False, indent=4)
    return True

def change_data(my_data_dict,my_new_data,my_key):
    my_data_dict[my_key] = my_new_data
    print("Die Datei wurde erfolgreich geändert\n")

def add_button(my_frame,my_text,my_command,my_row,my_column,my_pady,my_padx,my_sticky):
    my_button = tk.Button(my_frame,text= my_text,command=my_command,
                          font=("Arial Black", 16), relief="raised",bd=5)
    my_button.grid(row=my_row,column=my_column,pady=my_pady,padx=my_padx,sticky=my_sticky)
    return my_button

def add_radiobutton(my_frame,my_text,my_choice,my_value,my_row ,my_column):
    my_rbtn = tk.Radiobutton(my_frame, text=my_text,
                             font=("Arial Black", 16), variable=my_choice, value=my_value)
    my_rbtn.grid(row=my_row,column=my_column,pady=10,padx=10)
    return my_rbtn

def add_label(my_frame,my_text,my_row, my_column,my_pady,my_padx,my_sticky,my_font_size):
    my_lable = Label(my_frame,text=my_text,font=("Arial Black",my_font_size))
    my_lable.grid(row=my_row,column=my_column,pady=my_pady,padx=my_padx,sticky=my_sticky)
    return my_lable

def add_text_feld(my_frame,my_row,my_column,my_pady,my_padx,my_sticky):
    my_text_feld = Entry(my_frame,width = 65,font=("Arial",12))
    my_text_feld.grid(row=my_row,column=my_column,pady=my_pady,padx=my_padx,sticky=my_sticky)
    return my_text_feld
def my_radiobuttons(my_frame,my_choice):
    first_radbutton = add_radiobutton(my_frame, "Mitarbeiter*innen",
                                    my_choice, 1, 0, 0)
    second_radbutton = add_radiobutton(my_frame, "Besucher*innen",
                                   my_choice, 2, 0, 1)
    return first_radbutton,second_radbutton

def change_frame(my_frame):
    my_frame.tkraise()

def my_program():
    persons_list = []
    main_window = tk.Tk()
    main_window.geometry("900x700")
    main_window.grid_columnconfigure(0,weight=1)
    main_window.title("Mitarbeiter*innen und Besucher*innen Daten")

    main_frame = tk.Frame(main_window)
    add_new_person_frame = tk.Frame(main_window)
    show_frame = tk.Frame(main_window)
    edit_frame = tk.Frame(main_window)
    for frame in (main_frame,add_new_person_frame,show_frame,edit_frame):
        frame.grid(row=0,column=0,sticky="nsew")

    add_button(main_frame, "Neue Person einfügen",
               lambda :change_frame(add_new_person_frame), 0, 0, 10,15,"ew" )
    add_button(main_frame, "Personen Daten zeigen",
               lambda :change_frame(show_frame), 1, 0, 10, 15, "ew")
    add_button(main_frame, "Person Daten ändern",
               lambda :change_frame(edit_frame), 2, 0, 10, 15, "ew")

    type_choice = tk.IntVar()
    type_choice.set(1)
    my_radiobuttons(add_new_person_frame,type_choice)
    txt_feld_dict ={}
    error_lbl_dict ={}
    for i  in range(2,14,2):
        if i == 2:
            text ="Vorname"
            txt_key ="first_name_txt"
            lbl_key = "first_name_lbl"
        elif i == 4:
            text = "Nachname"
            txt_key ="family_name_txt"
            lbl_key = "family_name_lbl"
        elif i == 6:
            text = "Adresse"
            txt_key = "address_txt"
            lbl_key = "address_lbl"
        elif i == 8:
            text = "Geburtsdatum"
            txt_key = "birthday_txt"
            lbl_key = "birthday_lbl"
        elif  i == 10:
            text = "Telefon"
            txt_key = "phone_txt"
            lbl_key = "phone_lbl"
        else:
            text = "E-Mail"
            txt_key = "email_txt"
            lbl_key = "email_lbl"
        error_lbl = add_label(add_new_person_frame,"", i-1,1,5,5,"w",10)
        add_label(add_new_person_frame, text, i, 0, 5, 5, "w",18)
        txt_feld = add_text_feld(add_new_person_frame,i,1,5,5,"w")
        txt_feld_dict[txt_key] = txt_feld
        error_lbl_dict[lbl_key] = error_lbl

    def save_person():
        person_dict = {}
        if type_choice.get() == 1:
            person_dict["type"] = "Mitarbeiter*innen"
        else:
            person_dict["type"] = "Besucher*innen"
        first_name = txt_feld_dict["first_name_txt"].get()
        if is_valide(first_name,0,error_lbl_dict["first_name_lbl"]):
            first_name = first_name.title()                                     # Der erste Buchstabe als groß setzen
            person_dict["first_name"] = first_name
            family_name = txt_feld_dict["family_name_txt"].get()
            if is_valide(family_name,0,error_lbl_dict["family_name_lbl"]):
                family_name = family_name.title()                                   # Der erste Buchstabe als groß setzen
                person_dict["family_name"] = family_name
                address = txt_feld_dict["address_txt"].get()
                if is_valide(address,1,error_lbl_dict["address_lbl"]):
                    person_dict["address"] = address
                    birthday = txt_feld_dict["birthday_txt"].get()
                    if is_valide_date(birthday,error_lbl_dict["birthday_lbl"]):
                        person_dict["birthday"] = birthday
                        phone = txt_feld_dict["phone_txt"].get()
                        if is_valide(phone,2,error_lbl_dict["phone_lbl"]):
                            person_dict["phone"] = phone
                            email = txt_feld_dict["email_txt"].get()
                            if is_valide(email,3,error_lbl_dict["email_lbl"]):
                                person_dict["email"] = email
                                persons_list.append(person_dict.copy())
                                if save_list(persons_list):
                                    messagebox.showinfo("Erfolgreich Gespeichert","Eine Persondaten wurden erfolgreich gespeichert")

    def click_and_switch():
        save_person()
        change_frame(main_frame)
    add_button(add_new_person_frame,"Speichern",click_and_switch,
                         13,0,20,30,"w")
    add_button(add_new_person_frame, "Abbrechen", main_frame,
                            13, 1, 20, 30, "w")
    my_radiobuttons(show_frame, type_choice)
    show_scrollbar = tk.Scrollbar(show_frame)
    show_scrollbar.grid(row=2, column=1, sticky="nsw")
    show_list = Listbox(show_frame, width=50, height=10, yscrollcommand=show_scrollbar.set)
    show_list.grid(row=2, column=0, padx=30)
    show_scrollbar.config(command=show_list.yview)
    def show_all():
        if type_choice.get() ==1:
            show_data(show_list,"Mitarbeiter*innen")
        else:
            show_data(show_list,"Besucher*innen")

    def show_filter(*args):
        my_filters ={"Vornamen": "first_name",
                     "Nachnamen": "family_name",
                     "Adressen": "address",
                     "Geburtstagen": "birthday",
                     "Telefonnummern": "phone",
                     "E-Mail Adressen": "email"}
        selected_filter = menu_choice.get()
        filter_key = my_filters.get(selected_filter)
        if filter_key:
            if type_choice.get() == 1:
                show_data(show_list,"Mitarbeiter*innen",filter_key)
            else:
                show_data(show_list,"Besucher*innen",filter_key)

    add_button(show_frame,"Alles zeigen",show_all,1,0,10,10,"wn")
    add_button(show_frame, "Hauptmenü", click_and_switch, 3, 0, 10, 10, "wn")
    menu_choice = tk.StringVar()
    menu_choice.set("Filtern")
    menu_choice.trace_add("write", show_filter)
    filters =["Vornamen","Nachnamen","Adressen","Geburtstagen","Telefonnummern","E-Mail Adressen"]
    filter_menu = tk.OptionMenu(show_frame, menu_choice, *filters)
    filter_menu.config(font=('Arial Black', 14))
    filter_menu.grid(row=1, column=2, padx=10, pady=10,sticky="n")

    change_frame(main_frame)
    main_window.mainloop()
def main():
    my_program()
    # print("Mitarbeiter*innen und Besucher*innen Daten\n")    #Programm Name
    # persons_list = []                                        # Eine Datenliste, um Dictionary zu speichern
    # while True:                                              # Eine Menüliste zeigen
    #     user_input = choice_check("Drücken Sie bitte 1, um neue Mitarbeiterdatei oder Besucherdatei hinzufügen\n"
    #                               "Drücken Sie bitte 2, um die Personendaten zu zeigen\n"
    #                               "Drücken Sie bitte 3, um Daten zu ändern\n"
    #                               "Drücken Sie bitte 4, Programm zu schlissen\n")
    #     match user_input:
    #         case 1:                                                     # Erste Wahl (Eine neue Datei einfügen)
    #             person_dict = {}                                        # Dictionary entleeren
    #             while True:
    #                 while True:                                         # Meine Funktion aufrufen
    #                     choice = choice_check("Mitarbeiter*inne drücken Sie bitte 1\nBesucher*innen drücken Sie bitte 2\n")
    #                     if choice == 1:                                 # wenn, die erste Wahl
    #                         person_dict["type"] ="Mitarbeiter*innen"    # Die Type in Dictionary als Mitarbeiter*innen setzen
    #                         break
    #                     elif choice == 2:                               # wenn, die zweite Wahl
    #                         person_dict["type"] = "Besucher*innen"      # Die Type in Dictionary als Besucher*innen setzen
    #                         break
    #                 while True:                                         # Wiederholen bis die erste Eingabe erfüllt ist
    #                     name = input("Geben Sie bitte eine vollständige Name ein:\n").strip()
    #                     if is_valide(name,0):                     # Meine Funktion aufrufen, um die Eingabe zu prüfen
    #                         name = name.title()                                 # Der erste Buchstabe als groß setzen
    #                         save_data(person_dict, name, "name")       # Meine Funktion aufrufen, um die Eingabe in dictionary zu speichern
    #                         break
    #                 while True:                                                 # Wiederholen bis die Eingabe erfüllt ist
    #                     address = input("Geben Sie bitte eine vollständige Adresse ein:\n"
    #                                     "Muster (musterstraße 03, 3333 musterort)\n").strip()
    #                     if is_valide(address,1):                                # Meine Funktion aufrufen, um die Eingabe zu prüfen
    #                         save_data(person_dict, address, "address")               # Meine Funktion aufrufen, um die Eingabe in dictionary zu speichern
    #                         break
    #                 while True:
    #                     birthday = input("Geben Sie bitte eine vollständige Geburtsdatum ein:\nMuster TT.MM.JJJJ\n").strip()
    #                     if is_valide_date(birthday):                                   # Meine Funktion aufrufen, um die Eingabe zu prüfen
    #                         save_data(person_dict,birthday,"birthday")        # Meine Funktion aufrufen, um die Eingabe in dictionary zu speichern
    #                         break
    #                 while True:
    #                     phone = input("Geben Sie bitte eine Telefonnummer ein:\nMuster 0123 123456\n").strip()
    #                     if is_valide(phone,2):                          # Meine Funktion aufrufen, um die Eingabe zu prüfen
    #                         save_data(person_dict,phone,"phone")             # Meine Funktion aufrufen, um die Eingabe in dictionary zu speichern
    #                         break
    #                 while True:
    #                     email = input("Geben Sie bitte eine E-Mail Adresse ein:\nMuster: muster@gmail.com\n").strip()
    #                     if is_valide(email,3):                                 # Meine Funktion aufrufen, um die Eingabe zu prüfen
    #                         save_data(person_dict,email,"email")                    # Meine Funktion aufrufen, um die Eingabe in dictionary zu speichern
    #                         break
    #                 persons_list.append(person_dict.copy())
    #                 print("Eine Mitarbeiter*innen Daten wurden erfolgreich gespeichert\n")              # Eine Meldung, wenn alle Eingaben gespeichert sind
    #                 user_input = choice_check("Drücken Sie bitte 1, um noch eine Mitarbeiterdaten wieder hinzufügen\n"
    #                                           "Drücken Sie bitte andere Taste, um Die Menüliste wieder zu zeigen\n")
    #                 if user_input == 1:
    #                     continue
    #                 else:
    #                     break
    #         case 2:
    #             while True:                     # Wiederholen bis die Eingabe erfüllt ist
    #                 choice = choice_check("Mitarbeiter*innen drücken Sie bitte 1\n"         # Meine Funktion aufrufen, um die Eingabe zu prüfen und in Variable speichern
    #                                       "Besucher*innen drücken Sie bitte 2\n"
    #                                       "Filtern: Drücken Sie bitte 3\n")
    #                 if choice == 1:
    #                     show_data(persons_list,"Mitarbeiter*innen")                 # Meine Funktion aufrufen, um die Daten zu zeigen
    #                     break
    #                 elif choice == 2:
    #                     show_data(persons_list,"Besucher*innen")                    # Meine Funktion aufrufen, um die Daten zu zeigen
    #                     break
    #                 elif choice == 3:                                               # Meine Funktion aufrufen, um die Eingabe zu prüfen und in Variable speichern
    #                     type_filter = choice_check("Mitarbeiter*innen : Drücken Sie bitte 1\nBesucher*innen : Drücken Sie bitte 2\n")
    #                     person_type = "Mitarbeiter*innen" if type_filter ==1 else "Besucher*innen"      # Personen type nach Benutzerwahl setzen
    #                     choice_filter = choice_check("Drücken Sie eine Nummer der folgenden Filter\n"
    #                                                  "1.Name\n2.Adresse\n3.Geburtsdatum\n"              # meine Funktion aufrufen, um Filterwahl in Variable zu speichern
    #                                                  "4.Telefonnummer\n5.E-Mail\n")
    #                     filters = {1:"name",2:"address",3:"birthday",4:"phone",5:"email"}               # Ein Dictionary mit Integer Schlüssel, die meine Schlüssel erhalten
    #                     user_filter = filters.get(choice_filter)
    #                     if user_filter:
    #                         show_data(persons_list,person_type,user_filter)                             # Meine Funktion aufrufen, um die Daten zu zeigen
    #                         break
    #                     else:
    #                         print("Ungültige Eingabe\n")
    #                         continue
    #         case 3:                                                     # Daten ändern
    #             while True:
    #                 change_key = input("Geben Sie der Name der Person, die Sie ihre Daten ändern möchten\n").strip().title()
    #                 if is_valide(change_key,0):                                                # Meine Funktion aufrufen, um die Eingabe zu prüfen
    #                     for person in persons_list:                                                         # Die Personen in der Liste Durchführen
    #                         if person["name"] == change_key:                                                # die Eingabe mit gespeicherten Daten vergleichen
    #                             print(f"Name: {person.get('name')}\nAdresse: {person.get('address')}\n"     # Die passende Datei zeigen
    #                                   f"Geburtsdatum: {person.get('birthday')}\nTelefonnummer: {person.get('phone')}\n"
    #                                   f"E-Mail: {person.get('email')}\n")
    #                             choice_change = choice_check("Drücken Sie eine Nummer der folgenden Daten\n"
    #                                                          "1.Name\n2.Adresse\n3.Geburtsdatum\n"          # Funktion aufrufen, um die Benutzerwahl zu prüfen und speichern
    #                                                          "4.Telefonnummer\n5.E-Mail\n")
    #                             match choice_change:
    #                                 case 1:
    #                                     while True:
    #                                         new_name = input("Geben Sie bitte eine vollständige Name ein:\n").strip()
    #                                         if is_valide(new_name, 0):                      # Meine Funktion aufrufen, um die Eingabe zu prüfen
    #                                             new_name = new_name.title()                                  # Der erste Buchstabe als groß setzen
    #                                             change_data(person,new_name,"name")
    #                                             break
    #                                 case 2:
    #                                     while True:
    #                                         new_address = input("Geben Sie bitte eine vollständige Adresse ein:\n"
    #                                                             "Muster (musterstraße 03, 3333 musterort)\n").strip()
    #                                         if is_valide(new_address, 1):                           # Meine Funktion aufrufen, um die Eingabe zu prüfen
    #                                             change_data(person,new_address,"address")
    #                                             break
    #                                 case 3:
    #                                     while True:
    #                                         new_birthday = input("Geben Sie bitte eine vollständige Geburtsdatum ein:\n"
    #                                                              "Muster TT.MM.JJJJ\n").strip()
    #                                         if is_valide_date(new_birthday):                                     # Meine Funktion aufrufen, um die Eingabe zu prüfen
    #                                             change_data(person, new_birthday, "birthday")
    #                                             break
    #                                 case 4:
    #                                     while True:
    #                                         new_phone = input("Geben Sie bitte eine Telefonnummer ein:\nMuster 0123 123456\n").strip()
    #                                         if is_valide(new_phone, 2):                            # Meine Funktion aufrufen, um die Eingabe zu prüfen
    #                                             change_data(person, new_phone, "phone")
    #                                             break
    #                                 case 5:
    #                                     while True:
    #                                         new_email = input("Geben Sie bitte eine E-Mail Adresse ein:\nMuster: muster@gmail.com\n").strip()
    #                                         if is_valide(new_email, 3):                           # Meine Funktion aufrufen, um die Eingabe zu prüfen
    #                                             change_data(person, new_email, "email")
    #                                             break
    #                                 case _:
    #                                     print("Ungültige Eingabe\n")
    #                                     continue
    #                 break
    #         case 4:
    #             break
    #         case _:
    #             continue
main()