import json
import tkinter as tk
def show_data(my_list,my_type = None,my_filter = None):                         # Eine Funktion, um gespeicherte Daten zu zeigen
    my_list.delete(0, tk.END)
    counter = 1                                                                 # Ein Datenzähler
    try:
        with open("person.json", "r", encoding="utf-8") as persons:
            persons_data = json.load(persons)
            for person in persons_data:
                if isinstance(person,dict):
                    if my_type and person.get("type") != my_type:               # Überspringt Einträge, wenn sie nicht dem gewünschten Typ entsprechen.
                        continue
                    if my_filter:                                               # wenn Filter eingegeben wird
                        value = person.get(my_filter, "Nicht vorhanden")
                        my_list.insert(tk.END, f"{counter}. {value}")
                        counter += 1
                    else:
                        titels =["Vorname","Nachname","Adresse","Geburtsdatum","Telefonnummer","E-Mail"]
                        keys =["first_name","family_name","address","birthday","phone","email"]
                        my_list.insert(tk.END, f"{counter}.")
                        for i in range(len(titels)):
                            my_list.insert(tk.END, f"  {titels[i]}: {person.get(keys[i], "-")}")
                        my_list.insert(tk.END, "")
                        counter += 1
            if counter ==1:
                my_list.insert(tk.END, "Keine passenden Daten gefunden.")
    except FileNotFoundError:
        my_list.insert(tk.END,"Datei 'person.json' nicht gefunden.")
    except json.JSONDecodeError:
        my_list.insert(tk.END,"Fehler beim Lesen der JSON-Datei")
def show_all(my_choice,my_list):
    my_list.delete(0, tk.END)
    if my_choice.get() ==1:
        show_data(my_list,"Mitarbeiter*innen")
    else:
        show_data(my_list,"Besucher*innen")

def show_filter(my_menu_choice,my_choice,my_list):
    my_list.delete(0, tk.END)
    my_filters ={"Vornamen": "first_name",
                "Nachnamen": "family_name",
                "Adressen": "address",
                "Geburtstagen": "birthday",
                "Telefonnummern": "phone",
                "E-Mail Adressen": "email"}
    selected_filter = my_menu_choice.get()
    filter_key = my_filters.get(selected_filter)
    if filter_key:
        if my_choice.get() == 1:
            show_data(my_list,"Mitarbeiter*innen",filter_key)
        else:
            show_data(my_list,"Besucher*innen",filter_key)

def show_person(my_list,my_key):
    my_list.delete(0, tk.END)
    try:
        with open("person.json", "r", encoding="utf-8") as person:
            persons_data = json.load(person)
            for person_dict in persons_data:
                if isinstance(person_dict, dict) and person_dict["birthday"] == my_key:
                    titels = ["Vorname", "Nachname", "Adresse", "Geburtsdatum", "Telefonnummer", "E-Mail"]
                    keys = ["first_name", "family_name", "address", "birthday", "phone", "email"]
                    for i in range(len(titels)):
                        my_list.insert(tk.END, f"  {titels[i]}: {person_dict.get(keys[i], "-")}")
    except FileNotFoundError:
        my_list.insert(tk.END, "Datei 'person.json' nicht gefunden.")
    except json.JSONDecodeError:
        my_list.insert(tk.END, "Fehler beim Lesen der JSON-Datei")