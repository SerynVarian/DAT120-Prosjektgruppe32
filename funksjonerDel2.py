# funksjonerDel2.py
# DAT120 Prosjekt
# Prosjektgruppe 32
#

import funksjonerDel1 as fu

#Kategori Klasse
class kategori:

    def __init__(self,id, navn, prioritet = 1) -> None:
        self.id = id
        self.navn = navn
        self.prioritet = prioritet


    def __str__(self):
        return f"Kategori, Id: {self.id}, Navn: {self.navn}, Prioritet: {self.prioritet}"

def nyKategori():
    try:
        print("Ny avtale:")
        tempId = input("  Kategori Id: ")
        tempNavn = input("  Kategori Navn: ")
        tempPri = int(input("  Kategori Prioritet: "))

        return kategori(tempId,tempNavn,tempPri)

    except Exception as err:
        print("\nERROR, Feil input type:", err)



#Funksjon for aa skrive ut en liste av avtaler med posisjonen i lista og tittelen til avtalen
def lesKategoriListe(liste):
    print("Kategorier:")
    for i in range(0,len(liste)):
        print( f"   Index [{i}], Id: ", liste[i].id,", ", liste[i].navn)

#Funksjon for aa skrive avtale liste til fil
def lagreKategoriTilFil(liste, grunnliste,listelastet):
    if listelastet == True:
        f = open("kategorier.txt", "w")
        for i in range(0,len(liste)):
            f.write(f"{liste[i].id};{liste[i].navn};{liste[i].prioritet}\n")
        f.close()
    elif listelastet == False:
        for i in range(0, len(liste)):
            grunnliste.append(liste[i])

        f = open("kategorier.txt", "w")
        for i in range(0,len(grunnliste)):
            f.write(f"{grunnliste[i].id};{grunnliste[i].sted};{grunnliste[i].prioritet}\n")
        f.close()

#Funksjon for aa lese avtale liste fra fil
def leseKategoriFraFil():
    tempList = []
    with open('kategorier.txt', 'r', encoding='UTF-8') as file:
        while (line := file.readline().rstrip()):
            tempLineList = line.split(";")
            tempList.append(kategori(tempLineList[0],tempLineList[1],int(tempLineList[2])))
    return tempList






###################################################################

#Kategori Klasse
class sted:

    def __init__(self,id, navn, adresse) -> None:
        self.id = id
        self.navn = navn
        self.adresse = adresse


def __str__(self):
        return f"Sted, Id: {self.id}, Navn: {self.navn}, Adresse: {self.adresse}"

def nySted():
    try:
        print("Nyt Sted:")
        tempId = input("  Sted Id: ")
        tempNavn = input("  Sted Navn: ")
        tempAdresse = int(input("  Sted Adresse: "))

        return kategori(tempId,tempNavn,tempAdresse)

    except Exception as err:
        print("\nERROR, Feil input type:", err)



#Funksjon for aa skrive ut en liste av avtaler med posisjonen i lista og tittelen til avtalen
def lesStedListe(liste):
    print("Kategorier:")
    for i in range(0,len(liste)):
        print( f"   Index [{i}], Id: ", liste[i].id,", ", liste[i].navn)

#Funksjon for aa skrive avtale liste til fil
def lagreStedTilFil(liste, grunnliste,listelastet):
    if listelastet == True:
        f = open("sted.txt", "w")
        for i in range(0,len(liste)):
            f.write(f"{liste[i].id};{liste[i].navn};{liste[i].adresse}\n")
        f.close()
    elif listelastet == False:
        for i in range(0, len(liste)):
            grunnliste.append(liste[i])

        f = open("sted.txt", "w")
        for i in range(0,len(grunnliste)):
            f.write(f"{grunnliste[i].id};{grunnliste[i].sted};{grunnliste[i].adresse}\n")
        f.close()

#Funksjon for aa lese avtale liste fra fil
def leseStedFraFil():
    tempList = []
    with open('sted.txt', 'r', encoding='UTF-8') as file:
        while (line := file.readline().rstrip()):
            tempLineList = line.split(";")
            tempList.append(kategori(tempLineList[0],tempLineList[1],int(tempLineList[2])))
    return tempList