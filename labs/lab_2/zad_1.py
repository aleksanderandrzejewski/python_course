import shutil
import os
from os import path

katalog_plikow = '.' + os.sep + 'files'
source = os.listdir(katalog_plikow)
print source
if not path.exists('.' + os.sep + 'posortowane'):
    print "utworzono folder posortowane"
    os.mkdir("posortowane", 0777)
for nazwa_pliku in source:
    with open(katalog_plikow + os.sep + nazwa_pliku, "r") as plik:
        for linia in plik:
            nowy_katalog = '.' + os.sep + 'posortowane' + os.sep + linia.split()[1]
        if not path.exists(nowy_katalog):
            os.mkdir(nowy_katalog, 0777)
            print 'utworzono folder', nowy_katalog
        shutil.copy(katalog_plikow + os.sep + nazwa_pliku, nowy_katalog)
        print 'skopiowano plik', nazwa_pliku
