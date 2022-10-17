from lepes import lepes


def gyalog(tabla, honnan, hova):

    if tabla[int(honnan[0])-1][int(honnan[1])-1][0] == "b":
        if tabla[int(honnan[0])][int(honnan[1]) - 1] == "  " and honnan[1] == hova[1] and\
                int(hova[0])-int(honnan[0]) == 1:
            lepes(tabla, honnan, hova)

        if (tabla[int(honnan[0])][int(honnan[1])][1] == "w" or
                tabla[int(honnan[0])][int(honnan[1])-2][0] == "w") and \
                (int(honnan[1])+1 == int(hova[1]) or int(honnan[1]) - 1 == int(hova[1])) and\
                int(honnan[0]) == int(hova[0])-1:
            lepes(tabla, honnan, hova)

    else:
        if tabla[int(honnan[0])-2][int(honnan[1]) - 1] == "  " and honnan[1] == hova[1] and\
                int(honnan[0])-int(hova[0]) == 1:
            lepes(tabla, honnan, hova)

        if (tabla[int(honnan[0])-2][int(honnan[1])][1] == "b" or
                tabla[int(honnan[0])-2][int(honnan[1])-2][0] == "b") and \
                (int(honnan[1])+1 == int(hova[1]) or int(honnan[1]) - 1 == int(hova[1])) and\
                int(honnan[0]) == int(hova[0])+1:
            lepes(tabla, honnan, hova)
