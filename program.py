# program.py
# DAT120 Prosjekt Del 1
# Prosjektgruppe 32
#

#Import

import funksjoner as fu
from time import sleep



#Program
    #Progam kode start

avtaler = fu.leseAvtalerFraFil()
aktivAvtaler = list()
listLoaded = False

while True:
    print('Avtale Bok Meny:')
    fu.menyValg()
    valg = str(input("Input: "))
    if valg == "1":
        aktivAvtaler = fu.leseAvtalerFraFil()
        listLoaded = True
    elif valg == "2":
        fu.lagreAvtalerTilFil(aktivAvtaler,avtaler,listLoaded)
    elif valg == "3":
        aktivAvtaler.append(fu.nyAvtale())
    elif valg == "4":
        fu.lesAvtaleListe(aktivAvtaler)
    elif valg == "5":
        fu.sletteAvtale(aktivAvtaler)
    elif valg == "6":
        aktivAvtaler = fu.redigereAvtale(aktivAvtaler)
    elif valg == "7":
        exit()
    else:
        print("Feil input")
    input()
    
    
    #Program kode slutt
