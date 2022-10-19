def lepes(tabla, honnan, hova):
    tabla[int(hova[0]) - 1][int(hova[1]) - 1] = tabla[int(honnan[0]) - 1][int(honnan[1]) - 1]
    if tabla[int(hova[0]) - 1][int(hova[1]) - 1][1]=="k":
        print("játék vége")
        tabla[int(honnan[0]) - 1][int(honnan[1]) - 1] = "  "
        exit()
    tabla[int(honnan[0]) - 1][int(honnan[1]) - 1] = "  "
