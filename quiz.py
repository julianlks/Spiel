#----
#Quiz
#-----

from use_import import _f_num_frage, _f_correct

richtig = "Glückwunsch, Du hast die Frage korrekt beantwortet.\n"
falsch = "Die Antwort war nicht korrekt, versuche es nocheinmal.\n"
antwort_ja = ("Ja","ja","JA")
antwort_nein = ("Nein", "nein", "NEIN")

#-------
#Frage 1
#-------

frage_1 = "Frage 1: \nWie lautet das Ergebnis vom 2 mal 2? Deine Eingabe muss der Zahl entsprechen.\n"
lösung_1 = 4
_f_num_frage(frage_1, lösung_1)

#-------
#Frage 2
#-------

frage_2 = "Frage 2: \nWieviele Bundesländer hat Deutschland? Die Eingabe muss der Zahl entsprechen.\n"
lösung_2 = 16

_f_num_frage(frage_2, lösung_2)

#-------
#Frage 3
#-------

print("Die letzte Frage besteht aus zwei Teilen. Kommen wir zum ersten Teil!\n")

frage_31 = "Frage 3.1: \nWie viele der 16 Bundesländer sind Stadtstaaten? Die Eingabe muss der Zahl entsprechen.\n"
lösung_31 = 3

_f_num_frage(frage_31, lösung_31)

print("Sehr gut, die richtige Antwort lautet 3. Kommen wir zum zweiten Teil der Frage.\n")

frage_32 = input("Frage 3.2: \nNenne einen Stadtstaat. FÜr eine richtige Eingabe wird nur ein Stadtstaat benötigt.\n")
lösung_32 = ["hamburg", "berlin", "bremen"]

while _f_correct(frage_32) not in lösung_32:
    print(falsch)
    frage_32 = input("Frage 3.2: \nNenne einen Stadtstaat. Für die richtige Eingabe wird nur ein Stadtstaat benötigt.\n")