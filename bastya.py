from lepes import lepes


def bastya(tabla, honnan, hova):
    szin = tabla[int(honnan[0]) - 1][int(honnan[1]) - 1][0]

    elojel=-1
    if int(honnan[1]) - 1 == int(hova[1]) - 1:
        elojel=0
    if int(honnan[0]) - 1 == int(hova[0]) - 1:
        elojel=1
    if(elojel!=-1):
        if int(honnan[1]) - 1 == int(hova[1]) - 1:
            lephete = True
            for ix in range(min(int(honnan[0]), int(hova[0])), max(int(honnan[0]), int(hova[0])) - 1):
                if tabla[ix][int(honnan[1]) - 1][0] != " ":
                    lephete = False
                    break
            if lephete and tabla[int(hova[0]) - 1][int(hova[1]) - 1][0] != szin:
                lepes(tabla, honnan, hova)
        elif int(honnan[0]) - 1 == int(hova[0]) - 1:
            lephete = True
            for ix in range(min(int(honnan[1]), int(hova[1])), max(int(honnan[1]), int(hova[1])) - 1):
                if tabla[int(honnan[0]) - 1][ix][0] != " ":
                    lephete = False
                    break
            if lephete and tabla[int(hova[0]) - 1][int(hova[1]) - 1][0] != szin:
                lepes(tabla, honnan, hova)
                """
                if(elojel!=-1):
        lephete = True
        if elojel==0:
            for ix in range(min(int(honnan[0]), int(hova[0])), max(int(honnan[0]), int(hova[0])) - 1):
                if tabla[ix][int(honnan[1]) - 1][0] != " ":
                    lephete = False
                    break
        else:
            for ix in range(min(int(honnan[1]), int(hova[1])), max(int(honnan[1]), int(hova[1])) - 1):
                if tabla[int(honnan[0]) - 1][ix][0] != " ":
                    lephete = False
                    break
        if lephete and tabla[int(hova[0]) - 1][int(hova[1]) - 1][0] != szin:
            lepes(tabla, honnan, hova)
                """
