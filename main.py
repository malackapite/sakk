from kiir import kiir
import melyikFigura

tabla = [["br", "bh", "bb", "bq", "bk", "bb", "bh", "br"],
         ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
         ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
         ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
         ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
         ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
         ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
         ["wr", "wh", "wb", "wq", "wk", "wb", "wh", "wr"]]
jatekVege = 0

kiir(tabla)
while not jatekVege:
    honnan = str(input("Melyik figura (sor/oszlop): "))
    hova = str(input("Hova lépjen: "))
    melyikFigura.melyikFigura(tabla, honnan, hova)
    kiir(tabla)
