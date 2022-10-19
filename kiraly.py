from lepes import lepes


def kiraly(tabla, honnan, hova):
    szin = tabla[int(honnan[0]) - 1][int(honnan[1]) - 1][0]
    if int(honnan[0]) - 1 <= int(hova[0]) <= int(honnan[0]) + 1 and \
            int(honnan[1]) - 1 <= int(hova[1]) <= int(honnan[1]) + 1 and\
            tabla[int(hova[0]) - 1][int(hova[1]) - 1][0] != szin:
        lepes(tabla, honnan, hova)
