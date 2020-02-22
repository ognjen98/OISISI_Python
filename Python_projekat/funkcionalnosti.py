from OISISI_Python.Python_projekat.parser import *
from OISISI_Python.Python_projekat.Strukture.graph import *
from OISISI_Python.Python_projekat.Strukture.set import *
from OISISI_Python.Python_projekat.Strukture.trie import *
import os
import time

parser = Parser()

graph = Graph()
skup = Set()
trie = Trie()

def traziSaNot(rec):
    skup2, dict = trie.pronadjiRec(rec)
    fajlovi = skup - skup2

    return fajlovi


def traziSaAnd(rec1, rec2):
    fajl1, dict1 = trie.pronadjiRec(rec1)
    fajl2, dict2 = trie.pronadjiRec(rec2)

    fajlovi = fajl1 & fajl2

    return fajlovi, dict1, dict2


def traziSaOr(rec1, rec2):
    fajl1, dict1 = trie.pronadjiRec(rec1)
    fajl2, dict2 = trie.pronadjiRec(rec2)

    fajlovi = fajl1 | fajl2

    return fajlovi,dict1,dict2


def load(directory):
    for file in os.listdir(directory):
        if os.path.isdir(os.path.join(directory, file)):
            load(os.path.join(directory, file))
        else:
            if file.endswith(".html"):
                skup.add(os.path.join(directory, file))
                list = parser.parse(os.path.join(directory, file))
                links = list[0]
                cvor1 = graph.insert_vertex(os.path.join(directory, file))
                for link in links:
                    cvor2 = graph.insert_vertex(link)
                    graph.insert_edge(cvor1, cvor2)


directory = str(input("Unesi korenski direktorijum"))
start_time = time.time()
load(directory)
print("vreme: " + str(time.time() - start_time))

print(len(graph.vertices))
print(len(graph.edges))
