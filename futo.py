from lepes import lepes


def futo(tabla, honnan, hova):
    szin = tabla[int(honnan[0]) - 1][int(honnan[1]) - 1][0]
    if abs(int(honnan[0])-int(hova[0])) == abs(int(honnan[1])-int(hova[1])):
        lephete = True
        jx = min(int(honnan[1]), int(hova[1]))
        for ix in range(min(int(honnan[0]), int(hova[0])), max(int(honnan[0]), int(hova[0])) - 1):
            if tabla[ix][jx][0] != " ":
                lephete = False
                break
        if lephete and tabla[int(hova[0]) - 1][int(hova[1]) - 1][0] != szin:
            lepes(tabla, honnan, hova)