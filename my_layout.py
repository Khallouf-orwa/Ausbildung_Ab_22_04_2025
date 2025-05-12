import tkinter as tk
from tkinter.ttk import Label, Entry
from tkinter import messagebox, Scrollbar, Listbox
# Eine Funktion, um Button hinzufügen
def add_button(my_frame,my_text,my_command,my_row,my_column,my_pady,my_padx,my_sticky):
    my_button = tk.Button(my_frame,text= my_text,command=lambda :my_command(),
                          font=("Arial Black", 16), relief="raised",bd=5)
    my_button.grid(row=my_row,column=my_column,pady=my_pady,padx=my_padx,sticky=my_sticky)
    return my_button
# Eine Funktion, um Radiobutton hinzufügen
def add_radiobutton(my_frame,my_text,my_choice,my_value,my_row ,my_column):
    my_rbtn = tk.Radiobutton(my_frame, text=my_text,
                             font=("Arial Black", 16), variable=my_choice, value=my_value)
    my_rbtn.grid(row=my_row,column=my_column,pady=10,padx=10)
    return my_rbtn
# Eine Funktion, um Label hinzufügen
def add_label(my_frame,my_text,my_row, my_column,my_pady,my_padx,my_sticky,my_font_size):
    my_lable = Label(my_frame,text=my_text,font=("Arial Black",my_font_size))
    my_lable.grid(row=my_row,column=my_column,pady=my_pady,padx=my_padx,sticky=my_sticky)
    return my_lable
# Eine Funktion, um Entry hinzufügen
def add_text_feld(my_frame,my_row,my_column,my_pady,my_padx,my_sticky):
    my_text_feld = Entry(my_frame,width = 65,font=("Arial",12))
    my_text_feld.grid(row=my_row,column=my_column,pady=my_pady,padx=my_padx,sticky=my_sticky)
    return my_text_feld
# Eine Funktion, um Listbox mit Scrollbar hinzufügen
def add_listbox(my_frame,my_row,my_column):
    show_scrollbar = tk.Scrollbar(my_frame)
    show_scrollbar.grid(row=my_row, column=my_column, sticky="nsw")
    my_listbox = Listbox(my_frame, width=50, height=10, yscrollcommand=show_scrollbar.set)
    my_listbox.grid(row=my_row, column=my_column-1, padx=30)
    show_scrollbar.config(command=my_listbox.yview)
    return my_listbox
# Eine Funktion, um Menüliste hinzufügen
def add_menu_option(my_frame,my_choice,my_command,my_row,my_column,my_text,my_options):
    my_choice.set(my_text)
    filter_menu = tk.OptionMenu(my_frame, my_choice, *my_options,command=lambda _:my_command())
    filter_menu.config(font=('Arial Black', 14))
    filter_menu.grid(row=my_row, column=my_column, padx=10, pady=10, sticky="n")
# Eine Funktion, um meine Radiobuttons hinzufügen
def my_radiobuttons(my_frame,my_choice):
    first_radbutton = add_radiobutton(my_frame, "Mitarbeiter*innen",
                                    my_choice, 1, 0, 0)
    second_radbutton = add_radiobutton(my_frame, "Besucher*innen",
                                   my_choice, 2, 0, 1)
    return first_radbutton,second_radbutton
# Eine Funktion, um Frame zu wechseln
def change_frame(my_frame):
    my_frame.tkraise()