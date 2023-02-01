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

    kapott: str = eredmeny(jatekosP, gepP)
    vart: str = "Játékos veszített"
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

def dontetlen():
    jatekosP: list[int] = [10, 8]
    gepP: list[int] = [10, 8]

    kapott: str = eredmeny(jatekosP, gepP)
    vart: str = "Döntetlen"
    if kapott == vart:
        print("A teszteset jó!")
    else:
        print("A teszteset nem jó!")


def tesztek():
    jatekos_vesztett_teszt()
    gep_vesztett_teszt()
    dontetlen()
tesztek()
