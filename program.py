# program.py
# DAT120 Prosjekt Del 1
# Prosjektgruppe 32
#

#Import
import Funksjoner as fu



#Program
if __name__ == "__main__":
    #Progam kode start

    #Avtale liste variabel
    avtaler = []
    
    #Legge inn ny avtale
    avtaler.append(fu.nyAvtale())

    #lese av listen
    fu.lesAvtaleListe(avtaler)
    #Program kode slutt
    pass