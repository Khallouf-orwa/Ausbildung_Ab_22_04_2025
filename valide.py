import re
from datetime import datetime
def is_valide(my_input,pattern_position,my_label):                      # Eine Funktion, um Eingaben zu prüfen
    my_label.config(text="")
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
    my_label.config(text="")
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