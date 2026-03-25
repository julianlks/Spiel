#-------------
#Vorbereitung
#------------

from use_import import _f_win_spieler, _f_win_computer, _f_show_tt, _f_draw, _f_convert_spieler, \
    _f_convert_computer, _f_stop_game, _f_correct,  _f_num_ttt
import random


falsch = "Die Antwort war nicht korrekt, versuche es nocheinmal.\n"
belegt = "Dieses Feld ist schon belegt, wähle ein anderes.\n"
falsche_eingabe = "Dises Feld steht nicht zur Verfügung, wähle ein anderes.\n"
antwort_ja = ("Ja","ja","JA")
antwort_nein = ("Nein", "nein", "NEIN")

ttt = [
    ["(1)", "(2)", "(3)"],
    ["(4)", "(5)", "(6)"],
    ["(7)", "(8)", "(9)"]
]

win_spieler = False
win_computer = False
draw = False
stop_game = False
spieler_felder = []

#---------
#TicTacToe
#----------

while win_spieler == False and stop_game == False:

    eingabe_spieler = _f_correct(input("Entscheide dich zwischen x/o. Schreibe entweder x oder o."))
    lösung_eingabe = ["x","o"]

    while eingabe_spieler not in lösung_eingabe:
        print(falsch)
        eingabe_spieler = _f_correct(input("Entscheide dich zwischen x/o. Schreibe entweder x oder o."))

    if eingabe_spieler == "x":
        eingabe_computer = "o"
    else:
        eingabe_computer = "x"

    ttt_show = "\n1 | 2 | 3\n4 | 5 | 6\n7 | 8 | 9"

    print(f"Bestimme das Feld deines Steins, indem du eine Zahl zwischen 1-9 wählst. "
          "Die Aufteilung ist wie folgt:",
          ttt_show)

    #-------------------------------------------------------------------------------------------------------------------
    #Endlosschleife

    while win_computer == False and win_spieler == False and draw == False:

        #Spieler
        spieler_feld = _f_num_ttt()
        while spieler_feld not in range(1,10):
            print(falsche_eingabe)
            spieler_feld = _f_num_ttt()

        spieler_zeile, spieler_spalte= _f_convert_spieler(spieler_feld)

        while ttt[spieler_zeile][spieler_spalte] in ["x", "o"]:
            print(belegt)
            spieler_feld = _f_num_ttt()
            while spieler_feld not in range(1,10):
                print(falsche_eingabe)
                spieler_feld = _f_num_ttt()
            spieler_zeile, spieler_spalte = _f_convert_spieler(spieler_feld)
        spieler_felder.append(spieler_feld)

        ttt[spieler_zeile][spieler_spalte] = eingabe_spieler

        #Ergebnis prüfen
        win_spieler = _f_win_spieler(ttt, eingabe_spieler)
        if win_spieler == True:
            break
        draw = _f_draw(spieler_felder)
        if draw == True:
            break

        #---------------------------------------------------------------------------------------------------------------

        #Computer
        computer_feld = random.randint(1, 9)
        computer_zeile, computer_spalte = _f_convert_computer(computer_feld)

        while ttt[computer_zeile][computer_spalte] in ["x", "o"]:
            computer_feld = random.randint(1, 9)
            computer_zeile, computer_spalte = _f_convert_computer(computer_feld)

        ttt[computer_zeile][computer_spalte] = eingabe_computer
        _f_show_tt(ttt)

        #Ergebnis prüfen
        win_computer = _f_win_computer(ttt, eingabe_computer)
        if win_computer == True:
            break
        draw = _f_draw(spieler_felder)
        if draw == True:
            break

    #-------------------------------------------------------------------------------------------------------------------

    #Spielverlauf
    stop_game = _f_stop_game(draw, win_computer, win_spieler,ttt)






























