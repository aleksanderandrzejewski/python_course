
zdanie = "bla blabeeeeee labla eeeeeeee"

with open("teks.txt", "w") as plik:
    for slowo in zdanie.split():
        plik.write(slowo+ "\n")
