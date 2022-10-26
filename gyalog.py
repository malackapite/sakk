from lepes import lepes


def gyalog(tabla, honnan, hova):
    elojel = -1
    if tabla[int(honnan[0]) - 1][int(honnan[1]) - 1][0] == "b":
        elojel = 1
    megy(tabla, honnan, hova, elojel)
    tamad(tabla, honnan, hova, elojel)


def megy(tabla, honnan, hova, elojel):
    szin = tabla[int(honnan[0]) - 1][int(honnan[1]) - 1][0]
    if tabla[int(honnan[0]) - 1 + elojel][int(honnan[1]) - 1] == "  " and honnan[1] == hova[1]:
        if int(hova[0]) - int(honnan[0]) == 1 or (int(hova[0]) - int(honnan[0]) == 2 == int(honnan[0])) and szin == "b":
            lepes(tabla, honnan, hova)
        elif int(honnan[0]) - int(hova[0]) == 1 or (int(honnan[0]) - int(hova[0]) == 2 and int(honnan[0])) == 7 and szin == "w":
            lepes(tabla, honnan, hova)


def tamad(tabla, honnan, hova, elojel):
    ellenseg1 = tabla[int(honnan[0]) - 1 + elojel][int(honnan[1])][0]
    ellenseg2 = tabla[int(honnan[0]) - 1 + elojel][int(honnan[1]) - 2][0]
    if (tabla[int(honnan[0]) - 1 + elojel][int(honnan[1])][0] == ellenseg1 or
        tabla[int(honnan[0]) - 1 + elojel][int(honnan[1]) - 2][0] == ellenseg2) and \
            (int(honnan[1]) + 1 == int(hova[1]) or int(honnan[1]) - 1 == int(hova[1])) and \
            int(honnan[0]) == int(hova[0]) - elojel:
        lepes(tabla, honnan, hova)


"""
    else:
        if tabla[int(honnan[0])-2][int(honnan[1]) - 1] == "  " and honnan[1] == hova[1] and\
                int(honnan[0])-int(hova[0]) == 1:
            lepes(tabla, honnan, hova)

        if (tabla[int(honnan[0])-2][int(honnan[1])][0] == "b" or
                tabla[int(honnan[0])-2][int(honnan[1])-2][0] == "b") and \
                (int(honnan[1])+1 == int(hova[1]) or int(honnan[1]) - 1 == int(hova[1])) and\
                int(honnan[0]) == int(hova[0])+1:
            lepes(tabla, honnan, hova)
"""
