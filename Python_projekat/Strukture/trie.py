from OISISI_Python.Python_projekat.Strukture.set import *

class TrieNode:
    def __init__(self, slovo = None):
        self.slovo = slovo
        self.fajlovi = {}
        self.skupFajlova = Set()
        self.deca = {}

    def __getitem__(self, slovo):
        return self.deca[slovo]

    def dodajCvorDete(self,slovo):
        self.deca[slovo] = TrieNode(slovo)

class Trie:
    def __init__(self):
        self.koren = TrieNode()

    def __getitem__(self, data):
        return self.koren.deca[data]

    def dodajRec(self,rec,fajl):
        """
        Funkcija dodaje reci iz fajlova koji se parsiraju u trie
        :param rec: rec koja se dodaje u trie
        :param fajl: fajl iz kog se dodaje rec
        :return:
        """
        cvor = self.koren
        recPostoji = True

        for i in range(len(rec)):
            if rec[i] in cvor.deca:
                cvor = cvor.deca[rec[i]]
            else:
                recPostoji = False
                break

        if not recPostoji:
            while i < len(rec):
                cvor.dodajCvorDete(rec[i])
                cvor = cvor.deca[rec[i]]
                i += 1

        if fajl not in cvor.fajlovi:
            cvor.fajlovi[fajl] = 1
        else:
            cvor.fajlovi[fajl] += 1


        for f in cvor.fajlovi:
            if f not in cvor.skupFajlova:
                cvor.skupFajlova.add(f)


    def pronadjiRec(self, rec):
        """

        :param rec: rec koja se trazi
        :return: vraca fajlove u kojima se nalazi trazena rec
        """
        cvor = self.koren
        for char in rec:
            if char in cvor.deca:
                cvor = cvor.deca[char]
            else:
                return None

        return cvor.skupFajlova,cvor.fajlovi
