from gyalog import gyalog
from huszar import huszar
from bastya import bastya
from futo import futo
from kiraly import kiraly
from kiralyno import kiralyno


def melyikFigura(tabla, honnan, hova):
    figura = tabla[int(honnan[0]) - 1][int(honnan[1]) - 1][1]

    if figura == "p":
        gyalog(tabla, honnan, hova)
    elif figura == "h":
        huszar(tabla, honnan, hova)
    elif figura == "r":
        bastya(tabla, honnan, hova)
    elif figura == "b":
        futo(tabla, honnan, hova)
    elif figura == "k":
        kiraly(tabla, honnan, hova)
    elif figura == "q":
        kiralyno(tabla, honnan, hova)
