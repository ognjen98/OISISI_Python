
from Strukture.trie import *
from Strukture.graph import *
from Strukture.set import *

import os
import time
from pars import Parser

parser = Parser()




graph = Graph()
skup = Set()
trie = Trie()

def traziSaNot(rec):
    try:
        skup2, dict = trie.pronadjiRec(rec)
    except AttributeError:
        print("Nije pronadjen nijedan rezultat")
        return
    fajlovi = skup - skup2

    return fajlovi


def traziSaAnd(rec1, rec2):
    fajl1, dict1 = trie.pronadjiRec(rec1)
    fajl2, dict2 = trie.pronadjiRec(rec2)
    print("Kurac")
    try:
        fajlovi = fajl1 & fajl2
    except AttributeError:
        print("Nije pronadjen nijedan rezultat")
        return
    return fajlovi, dict1, dict2


def traziSaOr(rec1, rec2):
    fajl1, dict1 = trie.pronadjiRec(rec1)
    fajl2, dict2 = trie.pronadjiRec(rec2)
    try:
        fajlovi = fajl1 | fajl2
    except AttributeError:
        print("Nije pronadjen nijedan rezultat")
        return

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
                words = list[1]
                for word in words:
                    trie.dodajRec(word, os.path.join(directory, file))
                cvor1 = graph.insert_vertex(os.path.join(directory, file))
                for link in links:
                    cvor2 = graph.insert_vertex(link)
                    graph.insert_edge(cvor1, cvor2)


def ranking(documents, dict1, dict2=None):
    result = []
    for document in documents:
        vertex = graph.get_vertex(document)
        links_number = graph.degree(vertex, False)
        links = links_number * 0.8
        if document not in dict1.keys():
            words_doc1 = 0
        else:
            words_doc1 = dict1[document]
        if dict2 is None or document not in dict2.keys():
            words_doc2 = 0
        else:
            words_doc2 = dict2[document]
        words = words_doc1 * 0.2 + words_doc2 * 0.2
        words_in_links = 0
        edges = graph.incident_edges(vertex, False)
        for edge in edges:
            doc = str(edge.origin)
            if doc not in dict1.keys():
                word1 = 0
            else:
                word1 = dict1[doc]
            if dict2 is None or doc not in dict2.keys():
                word2 = 0
            else:
                word2 = dict2[doc]
            words_in_links += word1 + word2
        words_in_links = words_in_links * 1.4
        tupple = (str(document), words + links + words_in_links)
        result.append(tupple)

    return result

def prikaz(list):
    string = "Putanje do doukmenata" + " "*100 + "Rang"
    print(string)
    for value in list:
        print(value[0] + " "*(len(string)-len(value[0])-4) +  str(round(value[1], 2)))


