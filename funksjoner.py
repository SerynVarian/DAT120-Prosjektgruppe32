# funksjoner.py
# DAT120 Prosjekt Del 1
# Prosjektgruppe 32
#

#Import
from datetime import datetime as Dati
import keyboard


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
        tempTittel = input("  Mote Tittel: ")
        tempSted = input("  Mote Sted: ")
        tempTid = input("  Mote StartTid (Format: YYYY-MM-DD HH:MM:SS): ")
        tempVarighet = int(input("  Mote Varighet: "))

        #Konvertere Str input til datetime format
        tempTid = Dati.strptime(tempTid,  '%Y-%m-%d %H:%M:%S')

        return avtale(tempTittel,tempSted,tempTid,tempVarighet)

    except Exception as err:
        print("\nERROR, Feil input type:", err)


#Funksjon for aa skrive ut en liste av avtaler med posisjonen i lista og tittelen til avtalen
def lesAvtaleListe(liste):
    print("Avtaler:")
    for i in range(0,len(liste)):
        print( f"   Index [{i}], Tittel: ", liste[i].tittel)

#Funksjon for aa skrive avtale liste til fil
def lagreAvtalerTilFil(liste, grunnliste,listelastet):
    if listelastet == True:
        f = open("avtaler.txt", "w")
        for i in range(0,len(liste)):
            f.write(f"{liste[i].tittel};{liste[i].sted};{liste[i].startTid};{liste[i].varighet}\n")
        f.close()
    elif listelastet == False:
        for i in range(0, len(liste)):
            grunnliste.append(liste[i])

        f = open("avtaler.txt", "w")
        for i in range(0,len(grunnliste)):
            f.write(f"{grunnliste[i].tittel};{grunnliste[i].sted};{grunnliste[i].startTid};{grunnliste[i].varighet}\n")
        f.close()

#Funksjon for aa lese avtale liste fra fil
def leseAvtalerFraFil():
    tempList = []
    with open('avtaler.txt', 'r', encoding='UTF-8') as file:
        while (line := file.readline().rstrip()):
            tempLineList = line.split(";")
            tempList.append(avtale(str(tempLineList[0]),str(tempLineList[1]),Dati.strptime(tempLineList[2], '%Y-%m-%d %H:%M:%S'),tempLineList[3]))
    return tempList

#Funksjon for aa finne alle avtaler med samme dato
def avtalerSammeDato(liste):
    templist = []
    tempTid = input("Finn Moter paa datoer (Format: YYYY-MM-DD): ")
    tempTid = Dati.strptime(tempTid,  '%Y-%m-%d')
    
    for i in range(0, len(liste)):
        if liste[i].startTid.date() == tempTid.date():
            templist.insert(i,liste[i])
    print(templist)
    return templist

#Funksjon for aa finne alle avtaler med samme tittel
def avtalerSammeTittel(liste):
    templist = list()
    tempTittel = input("Finn Moter med samme tittel: ")
    
    for i in range(0, len(liste)):
        if liste[i].tittel.lower() == tempTittel.lower():
            templist.insert(i,liste[i])
    print(templist)
    return templist

#Funksjon for alle meny valgene
def menyValg():
    print('valg:')
    print('     Laste inn fil[1]')
    print('     Skrive til fil[2]')
    print('     Lage ny avtale[3]')
    print('     Skrive ut avtalene[4]')
    print('     Slette Avtale[5]')
    print('     Redigere Avtale[6]')
    print('     Avslutte[7]')

#Funksjon for aa slette en avtale
def sletteAvtale(liste):
    print('Slette Avtale')
    lesAvtaleListe(liste)
    indx = int(input('Skriv inn Index paa avtale som skal slettes: '))
    del liste[indx]

#Funksjon for aa redigere en avtale
def redigereAvtale(liste):
    print('Redigere Avtale')
    lesAvtaleListe(liste)
    indx = int(input('Skriv inn Index paa avtale som skal redigeres: '))
    print(liste[indx])

    print('\nRedigere Verdi:')
    print('     tittel[1]')
    print('     sted[2]')
    print('     startTid[3]')
    print('     varighet[4]')

    valg = input("Input: ")
    if valg == "1":
        liste[indx].tittel = input('Ny tittel: ')
    elif valg == "2":
        liste[indx].sted = input('Ny sted: ')
    elif valg == "3":
        liste[indx].startTid = input('Ny startTid: ')
    elif valg == "4":
        liste[indx].varighet = input('Ny varighet: ')
    else:
        print("Feil input")
    return liste
