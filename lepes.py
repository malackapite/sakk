def lepes(tabla, honnan, hova):
    if tabla[int(hova[0]) - 1][int(hova[1]) - 1][1] == "k":
        print("játék vége")
        if tabla[int(hova[0]) - 1][int(hova[1]) - 1][0] == "b":
            print("fehér nyert")
        else:
            print("fekete nyert")
        exit()
    tabla[int(hova[0]) - 1][int(hova[1]) - 1] = tabla[int(honnan[0]) - 1][int(honnan[1]) - 1]
    tabla[int(honnan[0]) - 1][int(honnan[1]) - 1] = "  "
