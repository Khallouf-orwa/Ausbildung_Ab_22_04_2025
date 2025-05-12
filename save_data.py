import json
import tkinter as tk
from tkinter import messagebox
import valide
# eine Funktion, um eine Liste in json zu speichern
def save_list(my_list):
    with open("person.json", "w", encoding="utf-8") as person:
        json.dump(my_list, person, ensure_ascii=False, indent=4)
    return True
# Eine Funktion, um eine Person datei zu speichern
def save_person(my_list,my_choice,my_txt_dict,my_lbl_dict):
    try:
        with open("person.json", "r", encoding="utf-8") as person:
            my_list = json.load(person)
    except (FileNotFoundError, json.JSONDecodeError):
        my_list = []
    person_dict = {}
    if my_choice.get() == 1:
        person_dict["type"] = "Mitarbeiter*innen"
    else:
        person_dict["type"] = "Besucher*innen"
    first_name = my_txt_dict["first_name_txt"].get()
    if valide.is_valide(first_name,0,my_lbl_dict["first_name_lbl"]):
        first_name = first_name.title()                                     # Der erste Buchstabe als groß setzen
        person_dict["first_name"] = first_name
        family_name = my_txt_dict["family_name_txt"].get()
        if valide.is_valide(family_name,0,my_lbl_dict["family_name_lbl"]):
            family_name = family_name.title()                                   # Der erste Buchstabe als groß setzen
            person_dict["family_name"] = family_name
            address = my_txt_dict["address_txt"].get()
            if valide.is_valide(address,1,my_lbl_dict["address_lbl"]):
                person_dict["address"] = address
                birthday = my_txt_dict["birthday_txt"].get()
                if valide.is_valide_date(birthday,my_lbl_dict["birthday_lbl"]):
                    person_dict["birthday"] = birthday
                    phone = my_txt_dict["phone_txt"].get()
                    if valide.is_valide(phone,2,my_lbl_dict["phone_lbl"]):
                        person_dict["phone"] = phone
                        email = my_txt_dict["email_txt"].get()
                        if valide.is_valide(email,3,my_lbl_dict["email_lbl"]):
                            person_dict["email"] = email
                            my_list.append(person_dict.copy())
                            if save_list(my_list):
                                messagebox.showinfo("Erfolgreich Gespeichert",
                                                    "Eine Persondaten wurden erfolgreich gespeichert")
                                for i in my_txt_dict:
                                    my_txt_dict[i].delete(0, tk.END)
def change_data(my_menu_choice,my_input,my_new_data,my_label):
    my_label.config(text= "")
    my_keys = {"Vornamen": "first_name",
               "Nachnamen": "family_name",
               "Adressen": "address",
               "Geburtstagen": "birthday",
               "Telefonnummern": "phone",
               "E-Mail Adressen": "email"}
    selected = my_menu_choice.get()
    key = my_keys.get(selected)
    if key:
        try:
            with open("person.json", "r", encoding="utf-8") as person:
                my_data = json.load(person)
        except (FileNotFoundError, json.JSONDecodeError):
            my_label.config(text="Fehler beim Lesen der Datei.")
        found = False
        for person in my_data:
            if person.get("birthday") == my_input:
                found = True
                if key == "first_name":
                    if valide.is_valide(my_new_data,0,my_label):
                        person["first_name"] = my_new_data
                        break
                elif key == "family_name":
                    if valide.is_valide(my_new_data,0,my_label):
                        person["family_name"] = my_new_data
                        break
                elif key == "address":
                    if valide.is_valide(my_new_data,1,my_label):
                        person["address"] = my_new_data
                        break
                elif key == "birthday":
                    if valide.is_valide_date(my_new_data,my_label):
                        person["birthday"] = my_new_data
                        break
                elif key == "phone":
                    if valide.is_valide(my_new_data,2,my_label):
                        person["phone"] = my_new_data
                        break
                else:
                    if valide.is_valide(my_new_data,3,my_label):
                        person["email"] = my_new_data
                        break
        if not found:
            my_label.config(text="Ungültige Eingabe")
        else:
            with open("person.json", "w", encoding="utf-8") as person_file:
                json.dump(my_data, person_file, ensure_ascii=False, indent=4)
                messagebox.showinfo("Erfolgreich Gespeichert", "Eine Persondaten wurden erfolgreich geändert")
    else:
        my_label.config(text= "Ungültige Eingabe")