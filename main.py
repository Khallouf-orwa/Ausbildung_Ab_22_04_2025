
import tkinter as tk                                                # tkinter und meine Module importieren
import my_layout
import save_data
import show_data

def main():
    persons_list = []
    main_window = tk.Tk()                                                   # Neue Fenster definieren
    main_window.geometry("900x700")                                         # Größe für Fenster setzen
    main_window.grid_columnconfigure(0,weight=1)                      # Mein Fenster mit grid Funktion anpassen
    main_window.title("Mitarbeiter*innen und Besucher*innen Daten")

    main_frame = tk.Frame(main_window)                                      # Frames für mein Programm
    add_new_person_frame = tk.Frame(main_window)
    show_frame = tk.Frame(main_window)
    edit_frame = tk.Frame(main_window)
    for frame in (main_frame,add_new_person_frame,show_frame,edit_frame):   # Die Frames mit grid Funktion Anpassen
        frame.grid(row=0,column=0,sticky="nsew")
    # Drei Buttons, um die Frames aufzurufen
    my_layout.add_button(main_frame, "Neue Person einfügen",
               lambda :my_layout.change_frame(add_new_person_frame), 0, 0, 10,15,"ew" )
    my_layout.add_button(main_frame, "Personen Daten zeigen",
               lambda :my_layout.change_frame(show_frame), 1, 0, 10, 15, "ew")
    my_layout.add_button(main_frame, "Person Daten ändern",
               lambda :my_layout.change_frame(edit_frame), 2, 0, 10, 15, "ew")
    # Persondaten einfügen Frame
    type_choice = tk.IntVar()                                       # Eine Variable für Radio Buttons definieren
    type_choice.set(1)                                              # Wert für die Variable setzen
    my_layout.my_radiobuttons(add_new_person_frame,type_choice)     # Meine Funktion in Module my_layout aufrufen, um Radiobuttons zu setzen
    txt_feld_dict ={}                                               # Dictionary, um die schlüssel von Label und Entry zu speichern
    error_lbl_dict ={}
    for i  in range(2,14,2):                                        # for Schleife, um Label und Entry hinzufügen
        if i == 2:
            text ="Vorname"
            txt_key ="first_name_txt"                               # texte und Schlüssel für jedes Label und Entry
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
            lbl_key = "email_lbl"                               # Meine Module aufrufen, um Label und Entry hinzufügen
        error_lbl = my_layout.add_label(add_new_person_frame,"", i-1,1,5,5,"w",10)
        my_layout.add_label(add_new_person_frame, text, i, 0, 5, 5, "w",18)
        txt_feld = my_layout.add_text_feld(add_new_person_frame,i,1,5,5,"w")
        txt_feld_dict[txt_key] = txt_feld                       # Die Schlüssel in Dictionary speichern
        error_lbl_dict[lbl_key] = error_lbl
    # Meine Module aufrufen, um Button und Radiobutton hinzufügen
    my_layout.add_button(add_new_person_frame,"Speichern",lambda :save_data.save_person(persons_list,type_choice,txt_feld_dict,error_lbl_dict),
                         13,0,20,30,"w")
    my_layout.add_button(add_new_person_frame, "Abbrechen",lambda :my_layout.change_frame(main_frame),
                            13, 1, 20, 30, "w")
    my_layout.my_radiobuttons(show_frame, type_choice)
    # Daten zeigen Frame
    show_list = my_layout.add_listbox(show_frame,2,1)               # Listbox einfügen, um daten zu zeigen
    my_layout.add_button(show_frame,"Alles zeigen",lambda :show_data.show_all(type_choice,show_list),
               1,0,10,10,"wn")            # Button einfügen
    my_layout.add_button(show_frame, "Hauptmenü",lambda :my_layout.change_frame(main_frame),
               3, 0, 10, 10, "wn")
    menu_choice_show = tk.StringVar()                                                 # String Variablen für Menüliste definieren
    menu_choice_edit = tk.StringVar()
    my_layout.add_menu_option(show_frame,menu_choice_show,                            # Eine Menüliste einfügen
                    lambda :show_data.show_filter(menu_choice_show,type_choice,show_list),1,2,
                    "Filter",["Vornamen","Nachnamen","Adressen","Geburtstagen","Telefonnummern","E-Mail Adressen"])
    for i in range(0,9,5):                                                            # Schleife, um Label und Entry einzufügen
        if i ==0:
            text_lbl ="Geburtsdatum"
            lbl_key = "edit_birthday_lbl"
            txt_key ="edit_birthday_txt"
        else:
            text_lbl = "Änderungen eingeben"
            lbl_key = "edit_input_lbl"
            txt_key = "edit_txt"
        my_layout.add_label(edit_frame, text_lbl,
              i, 0, 5, 5, "w", 16)
        edit_error_lbl = my_layout.add_label(edit_frame,"",i+1,0,5,5,"w",10)
        edit_feld_txt = my_layout.add_text_feld(edit_frame,
                              i+2, 0, 5, 5, "w")
        txt_feld_dict[txt_key] = edit_feld_txt                                          # Label und Entry Schlüssel in dict speichern
        error_lbl_dict[lbl_key] = edit_error_lbl
    # Datenändern Frame
    edit_show = my_layout.add_listbox(edit_frame, 3, 1)
    my_layout.add_button(edit_frame, "Suchen",
                         lambda: show_data.show_person(edit_show,
                         txt_feld_dict["edit_birthday_txt"].get()),
                        2, 1, 10, 10, "w")
    my_layout.add_button(edit_frame,"Ändern",lambda :save_data.change_data(menu_choice_edit.get(),
                                                       txt_feld_dict["edit_birthday_txt"].get(),
                                                       txt_feld_dict["edit_txt"].get(),
                                                       error_lbl_dict["edit_input_lbl"]),
                                    7,1,10,10,"w")
    my_layout.add_button(edit_frame, "Hauptmenü", lambda: my_layout.change_frame(main_frame),
               8, 0, 10, 10, "wn")
    my_layout.add_menu_option(edit_frame,menu_choice_edit,
                    lambda :show_data.show_person(edit_show,"birthday"),4,0,"Änderungswahl",
                    ["Vornamen","Nachnamen","Adressen","Geburtstagen","Telefonnummern","E-Mail Adressen"])

    my_layout.change_frame(main_frame)
    main_window.mainloop()
if __name__ == "__main__":
    main()