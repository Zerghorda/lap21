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
# teszteset
def jatekos_vesztett_teszt():
    jatekosP: list[int] = [7, 8, 10]
    gepP: list[int] = [10, 9, 2]

    print(eredmeny(jatekosP, gepP))

def tesztek():
    jatekos_vesztett_teszt()

tesztek()
