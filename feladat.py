#megoldás
def eredmeny(jatekosPontja: list[int], gepPontja: list[int]) -> str:
    if pontokOsszeg(jatekosPontja) > 21:
        return "Játékos vesztett"
    elif pontokOsszeg(gepPontja) > 21:
        return "Gép vesztett"

def pontokOsszeg(lista: list[int]) -> int:
    osszeg = 0
    for ertek in lista:
        osszeg += ertek
    return osszeg
# teszt

def jatekos_vesztett_teszt():
    jatekosP: list[int] = [7, 8, 10]
    gepP: list[int] = [10, 9, 2]
    if jatekosP == gepP:
       jatekosP > gepP
    kapott: str = eredmeny(jatekosP, gepP)
    vart: str = "Játékos veszített"
    if kapott == vart:
        print("A teszteset jó!")
    else:
        print("A teszteset nem jó!")
def jatekos_veszitet_tullepel():
    jatekosP: list[int] = [10, 12]
    if jatekosP > 21:
        kapott: str = eredmeny(jatekosP)
        vart: str = "Játékos veszített"
        if kapott == vart:
            print("A teszteset jó!")
        else:
            print("A teszteset nem jó!")


def jatekos_veszitet_dontetlennel():
    jatekosP: list[int] = [5, 5, 6]
    gepP: list[int] = [8, 8]
    print("játékos veszített döntetlennél")
    vart: str = "döntetlen"
    kapott: str = eredmeny(jatekosP, gepP)
    if vart == kapott and len(jatekosP) >len(gepP):
        if kapott == vart:
            print("A teszteset jó!")
        else:
            print("A teszteset nem jó!")

def jatekos_vesztet_kozelebb():
    jatekosP: list[int] = [5, 5, 6]
    gepP: list[int] = [8, 8]
    print("játékos veszítt mert messzebb volt")
    if jatekosP > 21 or jatekosP < gepP:
        kapott: str = eredmeny(jatekosP)
        vart: str = "Játékos veszített"
        if kapott == vart:
            print("A teszteset jó!")
        else:
            print("A teszteset nem jó!")

def gep_vesztet_kozelebb():
    jatekosP: list[int] = [8, 8]
    gepP: list[int] = [5, 5, 6]
    print("játékos veszítt mert messzebb volt")
    if gepP > 21 or jatekosP > gepP:
        kapott: str = eredmeny(gepP)
        vart: str = "Gép veszített"
        if kapott == vart:
            print("A teszteset jó!")
        else:
            print("A teszteset nem jó!")
def gep_vesztett_teszt():
    jatekosP: list[int] = [7, 8, 10]
    gepP: list[int] = [10, 9, 2]
    kapott: str = eredmeny(jatekosP, gepP)
    vart: str = "Gép veszített"
    if kapott == vart:
        print("A teszteset jó!")
    else:
        print("A teszteset nem jó!")
def gep_veszitet_dontetlennel():
    jatekosP: list[int] = [8, 8]
    gepP: list[int] = [5, 5, 6]
    print("Gép veszített döntetlennél")
    vart: str = "döntetlen"
    kapott: str = eredmeny(jatekosP, gepP)
    if vart == kapott and len(jatekosP) <len(gepP):
        if kapott == vart:
            print("A teszteset jó!")
        else:
            print("A teszteset nem jó!")
def gep_veszitet_tullepel():
    gepP: list[int] = [10, 12]
    if gepP > 21:
        kapott: str = eredmeny(gepP)
        vart: str = "Játékos veszített"
        if kapott == vart:
            print("A teszteset jó!")
        else:
            print("A teszteset nem jó!")

def dontetlen_teszt():
    jatekosP: list[int] = [10, 8]
    gepP: list[int] = [10, 8]
    kapott: str = eredmeny(jatekosP, gepP)
    vart: str = "Döntetlen"
    if kapott == vart:
        print("A teszteset jó!")
    else:
        print("A teszteset nem jó!")
def dontettlen_teszt_mindketto_veszit():
    jatekosP: list[int] = [10, 12]
    gepP: list[int] = [10, 12]
    print("Döntetlen")
    kapott: str = eredmeny(jatekosP, gepP)
    vart: str = "Döntetlen"
    if kapott == vart:
        print("A teszteset jó!")
    else:
        print("A teszteset nem jó!")

def tesztek():
    jatekos_vesztett_teszt()
    jatekos_veszitet_tullepel()
    jatekos_veszitet_dontetlennel()
    jatekos_vesztet_kozelebb()
    gep_vesztet_kozelebb()
    gep_vesztett_teszt()
    gep_veszitet_dontetlennel()
    gep_veszitet_tullepel()
    dontetlen_teszt()
tesztek()
