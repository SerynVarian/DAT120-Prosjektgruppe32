# program.py
# DAT120 Prosjekt Del 1
# Prosjektgruppe 32
#

#Import

import funksjoner as fu
from time import sleep



#Program
    #Progam kode start

avtaler = []
    #aktivAvtaleListe = []
print('Avtale Bok Meny:')
fu.menyValg()
while True:
    valg = str(input("Input: "))
    if valg == "1":
        avtaler = fu.leseAvtalerFraFil()
    elif valg == "2":
        fu.lagreAvtalerTilFil(avtaler)
    elif valg == "3":
        avtaler.append(fu.nyAvtale())
    elif valg == "4":
        fu.lesAvtaleListe(avtaler)
    elif valg == "5":
        exit()
    else:
        print("Feil input")
    input()
    fu.menyValg()
    
    #Program kode slutt
