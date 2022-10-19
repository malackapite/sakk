from kiir import kiir
from melyikFigura import melyikFigura

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
    melyikFigura(tabla, honnan, hova)
    kiir(tabla)
