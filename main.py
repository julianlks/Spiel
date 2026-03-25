#################
#Main File Game
#################

from use_import import _f_num_frage_mod

#-------------
#1: Einleitung
#-------------

name = input("Es freut mich, dich in meinem Spiel begrüßen zu dürfen. Wie heißt du?")
print(f"Hallo {name}!")

print("""
Erklärung des Spiels: \nDieses Spiel besteht aus zwei Teilen, wobei der 1. Teil ein Quizz ist. Du gewinnst nur, 
falls du beide Teile überstehst. In dem Quizz hast du unednlich viele Versuche, gelangst aber nur zur nächsten Frage, 
sollte die  Eingabe korrekt sein. Wenn du alle drei Frage richtig beantwortet hast, dann gelangst du zum zweiten Teil!
""")

#---------
#2: Quizz
#---------

frage_quizz = "Um mit dem ersten Teil zu starten, schreibe 1."
lösung_quizz = 1

Quizz = "Quizz"
_f_num_frage_mod(frage_quizz, lösung_quizz, Quizz)

import quizz

#------------
#3: TicTacToe
#------------

print("""
Sehr gut, du hast das Quizz erfolgreich bestanden. Kommen wir nun zum zweiten Teil des Spiels, in welchem du eine Runde 
Tic-Tac-Toe gegen den Computer spielst. Du hast unendlich viele Versuche, gewinnst aber nur, solltest 
du im Tic-Tac-Toe gewinnen. Viel Glück!
""")

frage_ttt = "Um mit dem zweiten Teil zu starten, schreibe 2."
lösung_ttt = 2
TicTacToe = "Tic-Tac-Toe"

_f_num_frage_mod(frage_ttt,lösung_ttt, TicTacToe)

import tic_tac_toe

