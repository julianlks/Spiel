import random
"""
from tic_tac_toe import spieler_zeile_list, spieler_spalte_list, computer_zeile_list, computer_spalte_list, \
    eingabe_spieler, eingabe_computer
"""

richtig = "Glückwunsch, Du hast die Frage korrekt beantwortet.\n"
falsch = "Die Antwort war leider nicht korrekt. Bitte versuche es nochmal.\n"
belegt = "Dieses Feld ist schon belegt, wähle ein anderes.\n"
falsche_eingabe = "Dises Feld steht nicht zur Verfügung, wähle ein anderes.\n"
antwort_nein = ("Nein", "nein", "NEIN")
antwort_ja = ("Ja", "ja", "JA")

def _f_show_ttt(spieler_zeile_list, spieler_spalte_list, eingabe_spieler, \
                computer_zeile_list, computer_spalte_list, eingabe_computer):

    ttt_copy = [
        ["(1)", "(2)", "(3)"],
        ["(4)", "(5)", "(6)"],
        ["(7)", "(8)", "(9)"]
    ]

    """
    Für alle i werden beide Listen elementweise durchlaufen. 
    """

    for i in range(len(spieler_zeile_list)):

        spieler_zeile = spieler_zeile_list[i]
        spieler_spate = spieler_spalte_list[i]
        ttt_copy[spieler_zeile][spieler_spate] = eingabe_spieler

    for i in range(len(computer_zeile_list)):

        computer_zeile = computer_zeile_list[i]
        computer_spate = computer_spalte_list[i]
        ttt_copy[computer_zeile][computer_spate] = eingabe_computer

    ttt_copy0 = ttt_copy[0]
    ttt_copy1 = ttt_copy[1]
    ttt_copy2 = ttt_copy[2]
    print(f"\nSpielfeld: \n{ttt_copy0}\n{ttt_copy1}\n{ttt_copy2}")



def _f_show_tt(ttt):
    ttt_0 = ttt[0]
    ttt_1 = ttt[1]
    ttt_2 = ttt[2]
    print(f"\nSpielfeld: \n{ttt_0}\n{ttt_1}\n{ttt_2}")

def _f_win_spieler(ttt, eingabe_spieler):

    """
    1: Iteriert über jedes element aus ttt. Da ttt selbst aus spieler_feldern besteht, sieht das erste Element wie folgt aus:

    ["","",""]
    """

    for row in ttt:
        if row == [eingabe_spieler, eingabe_spieler, eingabe_spieler]:
            return True

    """
    2: Iteriert über Zeile aus ttt, während auf eine Spalte konditioniert wird. 
    """

    for col in [0, 1, 2]:
        if ttt[0][col] == eingabe_spieler and ttt[1][col] == eingabe_spieler and ttt[2][col] == eingabe_spieler:
            return True

    """
    3: Prüft die Diagonale 
    """

    if ttt[0][0] == eingabe_spieler and ttt[1][1] == eingabe_spieler and ttt[2][2] == eingabe_spieler:
        return True

    if ttt[2][0] == eingabe_spieler and ttt[1][1] == eingabe_spieler and ttt[0][2] == eingabe_spieler:
        return True
    return False

def _f_win_computer(ttt, eingabe_computer):
    for row in ttt:
        if row == [eingabe_computer, eingabe_computer, eingabe_computer]:
            return True

    for col in [0, 1, 2]:
        if ttt[0][col] == eingabe_computer and ttt[1][col] == eingabe_computer and ttt[2][col] == eingabe_computer:
            return True

    if ttt[2][0] == eingabe_computer and ttt[1][1] == eingabe_computer and ttt[0][2] == eingabe_computer:
        return True

    if ttt[0][0] == eingabe_computer and ttt[1][1] == eingabe_computer and ttt[2][2] == eingabe_computer:
        return True
    return False

def _f_convert_computer(computer_feld):
    if computer_feld == 1:
        computer_zeile = 0
        computer_spalte = 0
    elif computer_feld == 2:
        computer_zeile = 0
        computer_spalte = 1
    elif computer_feld == 3:
        computer_zeile = 0
        computer_spalte = 2
    elif computer_feld == 4:
        computer_zeile = 1
        computer_spalte = 0
    elif computer_feld == 5:
        computer_zeile = 1
        computer_spalte = 1
    elif computer_feld == 6:
        computer_zeile = 1
        computer_spalte = 2
    elif computer_feld == 7:
        computer_zeile = 2
        computer_spalte = 0
    elif computer_feld == 8:
        computer_zeile = 2
        computer_spalte = 1
    elif computer_feld == 9:
        computer_zeile = 2
        computer_spalte = 2
    return computer_zeile, computer_spalte

def _f_convert_spieler(spieler_feld):
    if spieler_feld == 1:
        spieler_zeile = 0
        spieler_spalte = 0
    elif spieler_feld == 2:
        spieler_zeile = 0
        spieler_spalte = 1
    elif spieler_feld == 3:
        spieler_zeile = 0
        spieler_spalte = 2
    elif spieler_feld == 4:
        spieler_zeile = 1
        spieler_spalte = 0
    elif spieler_feld == 5:
        spieler_zeile = 1
        spieler_spalte = 1
    elif spieler_feld == 6:
        spieler_zeile = 1
        spieler_spalte = 2
    elif spieler_feld == 7:
        spieler_zeile = 2
        spieler_spalte = 0
    elif spieler_feld == 8:
        spieler_zeile = 2
        spieler_spalte = 1
    elif spieler_feld == 9:
        spieler_zeile = 2
        spieler_spalte = 2
    return spieler_zeile, spieler_spalte

def _f_draw(spieler_felder):
    if isinstance(spieler_felder, list) and len(spieler_felder) < 5:
        return False
    else:
        return True

def _f_stop_game(draw, win_computer, win_spieler,ttt):
    if draw == True and (win_spieler == False and win_computer == False):
        print(_f_show_tt(ttt),"\nSpielergebnis: Unentschieden.")
        stop = _f_correct(input("Wilst du nochmal spielen? Schreibe Ja oder Nein.\n"))
        while stop not in ["ja", "nein"]:
            print(f"Die Eingabe <{stop}> konnte nicht vearbeitet werden. Schreibe Ja oder Nein.\n")
            stop = _f_correct(input("Wilst du nochmal spielen? Schreibe Ja oder Nein.\n"))
        if stop in antwort_nein:
            print("Danke für deine Teilnahme, bis zum nächsten mal!")
            stop_game = True
        else:
            stop_game = False
    elif win_computer == True:
        print(_f_show_tt(ttt),"\nSpielergebnis: Der Computer hat gewonnen.")
        stop = _f_correct(input("Wilst du nochmal spielen? Schreibe Ja oder Nein\n"))
        while stop not in ["ja", "nein"]:
            print(f"Die Eingabe <{stop}> konnte nicht vearbeitet werden. Schreibe Ja oder Nein.\n")
            stop = _f_correct(input("Wilst du nochmal spielen? Schreibe Ja oder Nein.\n"))
        if stop in antwort_nein:
            print("Danke für deine Teilnahme, bis zum nächsten mal!")
            stop_game = True
        else:
            stop_game = False
    elif win_spieler == True:
        print(_f_show_tt(ttt),"\nSpielergenis: Glückwunsch, du hast das Spiel gewonnen!")
        stop_game = True
    return stop_game

def _f_num_frage(frage, lösung):

    while True:
        eingabe_frage = input(frage)

        try:
            int(eingabe_frage)
        except ValueError:
            print(f"Die Eingabe <{eingabe_frage}> konnte nicht verarbeitet werden. Schreibe eine Zahl.\n")
            continue

        if int(eingabe_frage) == lösung:
            print(richtig)
            break
        else:
            print(falsch)

def _f_num_frage_mod(frage, lösung, spiel):

    while True:
        eingabe_frage = input(frage)

        try:
            int(eingabe_frage)
        except ValueError:
            frage_type = type(frage)
            print(f"Die Eingabe <{eingabe_frage}> konnte nicht verareitet werden. Schreibe {lösung}.\n")
            continue

        if int(eingabe_frage) == lösung:
            print(f"\nSuper, dann beginnen wir mit dem {spiel}.\n")
            break
        else:
            print(falsch)

def _f_correct(frage):
    frage = frage.strip().lower()
    return frage

def _f_num_ttt():

    while True:
        spieler_feld = input("Bestimme ein Feld für deinen Stein.")

        try:
            spieler_feld = int(spieler_feld)
            break
        except ValueError:
            spieler_feld_type = type(spieler_feld)
            print(f"Der eingegebende Datentyp ist nicht korrekt: {spieler_feld_type}. Wähle eine Zahl.\n")
            continue

    return spieler_feld

def _f_comp_row(ttt, eingabe_spieler):
    
    """
    Prüft, ob der Spieler mit dem nächstem Zug in einer Zeile gewinnt.
    """

    for row in [0,1,2]:

        if ttt[row] == ["", eingabe_spieler, eingabe_spieler]:
            col = 0
            return row, col
        elif ttt[row] == [eingabe_spieler,"", eingabe_spieler]:
            col = 1
            return row, col
        elif ttt[row] == [eingabe_spieler, eingabe_spieler, ""]:
            col = 2
            return row, col
        else: 
            row, col = None, None
        
    computer_zeile = row
    computer_spalte = col
        
    return computer_zeile, computer_spalte
    
def _f_comp_col(ttt, eingabe_spieler):
    
    """
    Prüft, ob Spieler mit dem nächstem Zug in einer Spalte gewinnt.
    """

    for col in [0,1,2]:

        if ttt[0][col] == "" and ttt[1][col] == eingabe_spieler and ttt[2][col] == eingabe_spieler:
            row = 0
            return row, col
        elif ttt[0][col] == eingabe_spieler and ttt[1][col] == "" and ttt[2][col] == eingabe_spieler:
            row = 1
            return row, col
        if ttt[0][col] == eingabe_spieler and ttt[1][col] == eingabe_spieler and ttt[2][col] == "":
            row = 2
            return row, col
        else: 
            row, col = None, None
    
    computer_zeile = row
    computer_spalte = col
    
    return computer_zeile, computer_spalte

def _f_comp_dia(ttt, eingabe_spieler):
    
    """
    Prüft, ob Spieler mit nächsten Zug in Diagonale gewinnt. 
    """

    if ttt[0][0] == "" and ttt[1][1] == eingabe_spieler and ttt[2][2] == eingabe_spieler:
        row, col = 0,0
        return row, col
    elif ttt[0][0] == eingabe_spieler and ttt[1][1] == "" and ttt[2][2] == eingabe_spieler:
        row, col = 1, 1
        return row, col
    elif ttt[0][0] == eingabe_spieler and ttt[1][1] == eingabe_spieler and ttt[2][2] == "":
        row, col = 2,2
        return row, col

    elif ttt[2][0] == "" and ttt[1][1] == eingabe_spieler and ttt[0][2] == eingabe_spieler:
        row, col = 2,0
        return row, col
    elif ttt[2][0] == eingabe_spieler and ttt[1][1] == "" and ttt[0][2] == eingabe_spieler:
        row , col = 1,1
        return row, col
    elif ttt[2][0] == eingabe_spieler and ttt[1][1] == eingabe_spieler and ttt[0][2] == "":
        row, col = 0,2
        return row, col
    else: 
        row, col = None, None
        
    computer_zeile = row
    computer_spalte = col
    
    return computer_zeile, computer_spalte

def _f_comp_else(ttt, eingabe_spieler):

    computer_feld = random.randint(1, 9)
    computer_zeile, computer_spalte = _f_convert_computer(computer_feld)
    while ttt[computer_zeile][computer_spalte] == eingabe_spieler:
        computer_feld = random.randint(1, 9)
        computer_zeile, computer_spalte = _f_convert_computer(computer_feld)

    return computer_zeile, computer_spalte
    

    
    