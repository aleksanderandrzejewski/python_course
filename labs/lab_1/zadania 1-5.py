def test(fun, *args):
    print "".join(['-' for i in range(40)])
    print fun.__name__[:-1].upper() + " " + fun.__name__[-1]
    res = fun(*args[:-1])
    if isinstance(args[0], str):
        decoded = "".join([chr(i) for i in args[-1]])
        if res == decoded:
            print "Yes, " + decoded.replace("my", "your")
        else:
            print "No, " + decoded.replace("my", "your").replace("has", "has not") + " yet"
    else:
        print "Is correct? " + str(res == args[-1])
    print "".join(['-' for i in range(40)])


# zadanie 1
def zadanie1(listobject):
    wynik = []
    poprzedni = ""
    for obiekt in listobject:
        if obiekt != poprzedni:
            wynik.append(obiekt)
        poprzedni = obiekt
    return wynik


print zadanie1([1, 2, 3, 3, 5, 68, 68, 24])
test(zadanie1, [1, 2, 3, 3, 5, 68, 68, 24], [1, 2, 3, 5, 68, 24])


# zadanie2
def zadanie2(list1, list2):
    listwynik = []
    for i in range(len(list1) + len(list2)):
        try:
            listwynik.append(list1[i])
        except IndexError:
            pass
        try:
            listwynik.append(list2[i])
        except IndexError:
            pass
    return listwynik


test(zadanie2, [1, 2, 19, 'dd', ':P', ":("], [12, 'c', '5'], [1, 12, 2, 'c', 19, '5', 'dd', ':P', ':('])


# zadanie3
def zadanie3(listtuples):
    lista3 = [list(element) for element in listtuples]
    for element3 in lista3:
        element3.reverse()
    lista3.sort()
    for element3 in lista3:
        element3.reverse()
    lista3 = [tuple(element) for element in lista3]
    return lista3


test(zadanie3, [(1, 3), (3, 3, 2), (2, 1)], [(2, 1), (3, 3, 2), (1, 3)])


# zadanie4
def zadanie4(text):
    # lista = [kod(s) for s in lista if warunek(s)]
    lista = text.split("ok")
    wynikowalista = []
    for element in lista:
        podstawienie = ""
        for indeks in range(0, element.find("$")):
            podstawienie += element[indeks]
        wynikowalista.append(podstawienie)
    return " ".join(wynikowalista).strip()


test(zadanie4, "okmy$aiaetiaigaafbaf??a$okwatch$oafbusd$okhas$asbrsi31480$okended$aq340af",
     [109, 121, 32, 119, 97, 116, 99, 104, 32, 104, 97, 115, 32, 101, 110, 100, 101, 100])

# zadanie 5
from random import randint

a = randint(1, 9)
print a
b = input("Podaj liczbe:\n")
print "Podales", a
while a != b:
    b = input("Zle. Podaj inna liczbe:\n")
    print "Podales", a
print "Dobrze!", a, 'to prawidlowa liczba'
