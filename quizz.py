#-----
#Quizz
#------

from use_import import _f_num_frage, _f_correct

richtig = "Glückwunsch, Du hast die Frage korrekt beantwortet.\n"
falsch = "Die Antwort war nicht korrekt, versuche es nocheinmal.\n"
antwort_ja = ("Ja","ja","JA")
antwort_nein = ("Nein", "nein", "NEIN")

#-------
#Frage 1
#-------

frage_1 = "Frage 1: \nWie lautet das Ergebnis vom 2 mal 2? Antworte mit der Zahl."
lösung_1 = 4
_f_num_frage(frage_1, lösung_1)

#-------
#Frage 2
#-------

frage_2 = "Frage 2: \nWieviele Bundeslaender hat Deutschland? Antworte mit der Zahl."
lösung_2 = 16

_f_num_frage(frage_2, lösung_2)

#-------
#Frage 3
#-------

print("Die letzte Frage besteht aus zwei Teilen. Kommen wir zum ersten Teil!\n")

frage_31 = "Frage 3.1: \nWie viele der 16 Bundesländer sind Stadtstaaten? Antworte mit einer Zahl."
lösung_31 = 3

_f_num_frage(frage_31, lösung_31)

print("Sehr gut, die richtige Antwort lautet 3. Kommen wir zum zweiten Teil der Frage.\n")

frage_32 = input("Frage 3.2: \nNenne einen Stadtstaat.Bedenke, dass für eine richtige Einabe nur einer benötigt wird.")
lösung_32 = ["hamburg", "berlin", "bremen"]

while _f_correct(frage_32) not in lösung_32:
    print(falsch)
    frage_32 = input("Nenne einen Stadtstaat. Bedenke, dass für dir richtige Einabe nur einer benötigt wird.")