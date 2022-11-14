# program.py
# DAT120 Prosjekt
# Prosjektgruppe 32
#

#Import

import funksjonerDel1 as fu
import funksjonerDel2 as fu2


#Progam kode start

avtaler = fu.leseAvtalerFraFil()
aktivAvtaler = list()
avtalerLoaded = False

Kategori = fu2.leseKategoriFraFil()
aktivKategori = list()
kategoriLoaded = False

Sted = fu2.leseStedFraFil()
aktivSted = list()
stedLoaded = False

while True:
    print('Avtale Bok Meny:')
    fu.menyValg()
    valg = str(input("Input: "))
    if valg == "1":
        aktivAvtaler = fu.leseAvtalerFraFil()
        avtalerLoaded = True
        
        aktivKategori = fu2.leseKategoriFraFil()
        kategoriLoaded = True
        
        aktivSted = fu2.leseStedFraFil()
        stedLoaded = True

    elif valg == "2":
        fu.lagreAvtalerTilFil(aktivAvtaler,avtaler,avtalerLoaded)
        fu2.lagreKategoriTilFil(aktivKategori,Kategori,kategoriLoaded)
        fu2.lagreStedTilFil(aktivSted,Sted,stedLoaded)

    elif valg == "3":
        aktivAvtaler.append(fu.nyAvtale())
    elif valg == "4":
        fu.lesAvtaleListe(aktivAvtaler)
    elif valg == "5":
        fu.sletteAvtale(aktivAvtaler)
    elif valg == "6":
        aktivAvtaler = fu.redigereAvtale(aktivAvtaler)
    elif valg == "7":
        aktivKategori.append(fu2.nyKategori())
    elif valg == "8":
        aktivSted.append(fu2.nySted())
    elif valg == "0":
        exit()
    else:
        print("Feil input")
    input()
    
    
    #Program kode slutt
