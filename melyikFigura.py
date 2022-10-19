from gyalog import gyalog
from huszar import huszar
from bastya import bastya
from futo import futo
from kiraly import kiraly
from kiralyno import kiralyno


def melyikFigura(tabla, honnan, hova):
    if tabla[int(honnan[0]) - 1][int(honnan[1]) - 1][1] == "p":
        gyalog(tabla, honnan, hova)
    elif tabla[int(honnan[0]) - 1][int(honnan[1]) - 1][1] == "h":
        huszar(tabla, honnan, hova)
    elif tabla[int(honnan[0]) - 1][int(honnan[1]) - 1][1] == "r":
        bastya(tabla, honnan, hova)
    elif tabla[int(honnan[0]) - 1][int(honnan[1]) - 1][1] == "b":
        futo(tabla, honnan, hova)
    elif tabla[int(honnan[0]) - 1][int(honnan[1]) - 1][1] == "k":
        kiraly(tabla, honnan, hova)
    elif tabla[int(honnan[0]) - 1][int(honnan[1]) - 1][1] == "q":
        kiralyno(tabla, honnan, hova)
