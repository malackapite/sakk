from lepes import lepes


def bastya(tabla, honnan, hova):
    if tabla[int(honnan[0]) - 1][int(honnan[1]) - 1][0] == "b":
        if int(honnan[1]) - 1 == int(hova[1]) - 1:
            lephete = True
            for ix in range(min(int(honnan[0]), int(hova[0])), max(int(honnan[0]), int(hova[0])) - 1):
                if tabla[ix][int(honnan[1]) - 1][0] != " ":
                    lephete = False
                    break
            if lephete and tabla[int(hova[0]) - 1][int(hova[1]) - 1][0] != "b":
                lepes(tabla, honnan, hova)
        elif int(honnan[0]) - 1 == int(hova[0]) - 1:
            lephete = True
            for ix in range(min(int(honnan[1]), int(hova[1])), max(int(honnan[1]), int(hova[1])) - 1):
                if tabla[int(honnan[0]) - 1][ix][0] != " ":
                    lephete = False
                    break
            if lephete and tabla[int(hova[0]) - 1][int(hova[1]) - 1][0] != "b":
                lepes(tabla, honnan, hova)
    else:
        if int(honnan[1]) - 1 == int(hova[1]) - 1:
            lephete = True
            for ix in range(min(int(honnan[0]), int(hova[0])), max(int(honnan[0]), int(hova[0])) - 1):
                if tabla[ix][int(honnan[1]) - 1][0] != " ":
                    lephete = False
                    break
            if lephete and tabla[int(hova[0]) - 1][int(hova[1]) - 1][0] != "w":
                lepes(tabla, honnan, hova)
        elif int(honnan[0]) - 1 == int(hova[0]) - 1:
            lephete = True
            for ix in range(min(int(honnan[1]), int(hova[1])), max(int(honnan[1]), int(hova[1])) - 1):
                if tabla[int(honnan[0]) - 1][ix][0] != " ":
                    lephete = False
                    break
            if lephete and tabla[int(hova[0]) - 1][int(hova[1]) - 1][0] != "w":
                lepes(tabla, honnan, hova)
