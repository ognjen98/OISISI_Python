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


def traziSaOr(reci):
    skup = Set()
    lista = []


    for rec in reci:
        file, recnik = trie.pronadjiRec(rec)
        if file is not None:
            skup = skup | file

        lista.append(recnik)

    return skup, lista


def traziSaNot(rec1,rec2):
    lista = []
    skup1, dict1 = trie.pronadjiRec(rec1)
    skup2, dict2 = trie.pronadjiRec(rec2)
    fajlovi = Set()

    if skup1 is not None and skup2 is not None:
        fajlovi = skup1 - skup2
    elif skup1 is not None and skup2 is None:
        fajlovi = skup1

    lista.append(dict1)

    return fajlovi,lista


def traziSaAnd(rec1, rec2):
    lista = []
    fajl1, dict1 = trie.pronadjiRec(rec1)
    fajl2, dict2 = trie.pronadjiRec(rec2)
    fajlovi = Set()

    if fajl1 is not None and fajl2 is not None:
        fajlovi = fajl1 & fajl2

    lista.append(dict1)
    lista.append(dict2)

    return fajlovi, lista


def parsiranje(tekst):
    reci = tekst.split()

    if len(reci) == 3 and reci[1].lower() == "or":
        lista = []
        lista.append(reci[0].lower().strip())
        lista.append(reci[2].lower().strip())
        skup, listaRecnika = traziSaOr(lista)
        return skup, listaRecnika
    elif len(reci) == 3 and reci[1].lower() == "and":
        skup,listaRecnika = traziSaAnd(reci[0].lower().strip(),reci[2].lower().strip())
        return skup,listaRecnika
    elif len(reci) == 3 and reci[1].lower() == "not":
        skup,listaRecnika = traziSaNot(reci[0].lower().strip(),reci[2].lower().strip())
        return skup,listaRecnika
    else:
        lista = []
        for rec in reci:
            lista.append(rec.lower().strip())
        skup,listaRecnika = traziSaOr(lista)
        return skup,listaRecnika




def load(directory):
    for file in os.listdir(directory):
        if os.path.isdir(os.path.join(directory, file)):
            load(os.path.join(directory, file))
        else:
            if file.endswith(".html"):
                skup.add(os.path.join(directory, file))
                list = parser.parse(os.path.join(directory, file))
                links = list[0]
                reci = list[1]

                for rec in reci:
                    trie.dodajRec(rec.lower(),os.path.join(directory,file))
                cvor1 = graph.insert_vertex(os.path.join(directory, file))
                for link in links:
                    cvor2 = graph.insert_vertex(link)
                    graph.insert_edge(cvor1, cvor2)


def ranking(document, dict1):
    if document is None or dict1 is None:
        return 0
    result = 0
    vertex = graph.get_vertex(document)
    edges = graph.incident_edges(vertex, False)
    links_number = len(edges)
    if document not in dict1.keys():
        words_number = 0
    else:
        words_number = dict1[document]
    words = words_number * 0.2
    words_in_links = 0
    for edge in edges:
        doc = str(edge.origin)
        if doc in dict1.keys():
            words_in_links += dict1[doc]
            links_number = links_number - 1

    links = links_number * 0.8
    link_words = words_in_links * 1.2
    result = words + link_words + links
    return result


def rangiraj(documents, words):
    list = []
    for document in documents:
        rank = 0
        for word in words:
            rank += ranking(document, word)
        tupple = (str(document), rank)
        list.append(tupple)
    return list


def prikaz(list):
    string = "Putanje do doukmenata" + " " * 100 + "Rang"
    print(string)
    for value in list:
        print(value[0] + " " * (len(string) - len(value[0]) - 4) + str(round(value[1], 2)))

def paginacija(list, start, end, n):
    string = string = " " *15 + "PUTANJE DO DOKUMENATA" + " " * 100 + "RANG"
    print(string)
    for i in range(start*n, end*n):
        if i > len(list) - 1:
            return
        print(" " *15 + str(list[i][0]) + " " * (len(string) - len(list[i][0]) - 19) + str(round(list[i][1], 2)))