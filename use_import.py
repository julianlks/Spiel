richtig = "Glückwunsch, Du hast die Frage korrekt beantwortet.\n"
falsch = "Die Antwort war leider nicht korrekt. Bitte versuche es nochmal.\n"
belegt = "Dieses Feld ist schon belegt, wähle ein anderes.\n"
falsche_eingabe = "Dises Feld steht nicht zur Verfügung, wähle ein anderes.\n"
antwort_nein = ("Nein", "nein", "NEIN")
antwort_ja = ("Ja", "ja", "JA")


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
        stop = _f_correct(input("Wilst du nochmal spielen? Schreibe Ja oder Nein."))
        while stop not in ["ja", "nein"]:
            print(falsche_eingabe)
            stop = _f_correct(input("Wilst du nochmal spielen? Schreibe Ja oder Nein."))
        if stop == antwort_nein:
            print("Danke für deine Teilnahme, uns bis zum nächsten mal!")
            stop_game = True
    elif win_computer == True:
        print(_f_show_tt(ttt),"\nSpielergebnis: Der Computer hat gewonnen.")
        stop = _f_correct(input("Wilst du nochmal spielen? Schreibe Ja oder Nein"))
        while stop not in ["ja", "nein"]:
            print(falsche_eingabe)
            stop = _f_correct(input("Wilst du nochmal spielen? Schreibe Ja oder Nein."))
        if stop == antwort_nein:
            print("Danke für deine Teilnahme, uns bis zum nächsten mal!")
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
            frage_type = type(frage)
            print(f"Der eingegebende Datentyp ist nicht korrekt: {frage_type}. Wähle eine Zahl.\n")
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
            print(f"Der eingegebende ist nicht korrekt: {frage_type}. Wähle eine Zahl.\n")
            continue

        if int(eingabe_frage) == lösung:
            print(f"Super, dann beginnen wir mit dem {spiel}.\n")
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





