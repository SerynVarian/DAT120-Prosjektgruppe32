# Funksjoner.py
# DAT120 Prosjekt Del 1
# Prosjektgruppe 32
#

#Import
from datetime import datetime as Dati


#Avtale klasse
class avtale:

    #Definere variabler til klassen som blir egenskapene til objektet
    def __init__(self, tittel, sted, startTid, varighet) -> None:
        self.tittel = tittel
        self.sted = sted
        self.startTid = startTid
        self.varighet = varighet

    #Returnerer en string med alle egenskapene paa et leselig format
    def __str__(self):
        return f"Mote type: {self.tittel}, Sted: {self.sted}, startid: {self.startTid}, Varighet: {self.varighet}"

#Funksjon for aa lage ny avtale.
#Ta inn input fra bruker for alle egenskapene
def nyAvtale():
    try:
        print("Ny avtale:")
        tempTittel = input("    Mote Tittel: ")
        tempSted = input("  Mote Sted: ")
        tempTid = input("   Mote StartTid (Format: YYYY-MM-DD-HH-MM): ")
        tempVarighet = int(input("  Mote Varighet: "))

        #Konvertere Str input til datetime format
        tempTid = Dati.strptime(tempTid, "%Y-%m-%d-%H-%M")

        return avtale(tempTittel,tempSted,tempTid,tempVarighet)

    except Exception as err:
        print("\nERROR, Feil input type:", err)


#Funksjon for aa skrive ut en liste av avtaler med posisjonen i lista og tittelen til avtalen
def avtaleListe(liste):
    print("Avtaler:")
    for i in range(0,len(liste)):
        print( f"   Index [{i}], Tittel: ", liste[i].tittel)

