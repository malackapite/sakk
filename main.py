from kiir import kiir
from melyikFigura import melyikFigura

# w = 0, b = 1
kiLep = "w"
tabla = [["br", "bh", "bb", "bq", "bk", "bb", "bh", "br"],
         ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
         ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
         ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
         ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
         ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
         ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
         ["wr", "wh", "wb", "wq", "wk", "wb", "wh", "wr"]]

kiir(tabla)
while True:
    honnan = str(input("Melyik figura (sor/oszlop): "))
    hova = str(input("Hova lépjen: "))
    if tabla[int(honnan[0]) - 1][int(honnan[1]) - 1][0] == kiLep and honnan != hova:
        melyikFigura(tabla, honnan, hova)
        kiir(tabla)
        if tabla[int(honnan[0]) - 1][int(honnan[1]) - 1][0] == "w":
            kiLep = "b"
        else:
            kiLep = "w"
    else:
        print("rossz szín")
