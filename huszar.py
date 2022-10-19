from lepes import lepes


def huszar(tabla, honnan, hova):
    szin = tabla[int(honnan[0]) - 1][int(honnan[1]) - 1][0]
    if ((int(honnan[0]) + 2 == int(hova[0]) and (int(honnan[1])+1 == int(hova[1]) or int(honnan[1])-1 == int(hova[1]))) or
        (int(honnan[0]) + 1 == int(hova[0]) and (int(honnan[1]) + 2 == int(hova[1]) or int(honnan[1]) - 2 == int(hova[1]))) or
        (int(honnan[0]) - 1 == int(hova[0]) and (int(honnan[1])+2 == int(hova[1]) or int(honnan[1])-2 == int(hova[1]))) or
        (int(honnan[0]) - 2 == int(hova[0]) and (int(honnan[1])+1 == int(hova[1]) or int(honnan[1])-1 == int(hova[1])))) and\
            tabla[int(hova[0]) - 1][int(hova[1]) - 1][0] != szin:
        lepes(tabla, honnan, hova)



