from OISISI_Python.Python_projekat.parser import *
from OISISI_Python.Python_projekat.Strukture.graph import *
from OISISI_Python.Python_projekat.Strukture.set import *
import os
import time

parser = Parser()

graph = Graph()
skup = Set()


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


def ranking(documents, dict1, dict2=None):
    result = []
    pom = []
    for document in documents:

        vertex = graph.get_vertex(document)
        links_number = graph.degree(vertex, False)
        links = links_number * 0.8
        if document not in dict1.keys():
            words_doc1 = 0
        else:
            words_doc1 = dict1[document]
        if  dict2 is None or document not in dict2.keys():
            words_doc2 = 0
        else:
            words_doc2 = dict2[document]
        words = words_doc1 * 0.2 + words_doc2 * 0.2
        words_in_links = 0
        edges = graph.incident_edges(vertex, False)
        for edge in edges:
            doc = edge.origin.get_element
            if doc not in dict1.keys():
                word1 = 0
            else:
                word1 = dict1[doc]
            if doc not in dict1.keys():
                word2 = 0
            else:
                word2 = dict2[doc]
            words_in_links += word1 + word2
        words_in_links = words_in_links * 1.4
        pom.append(str(document))
        pom.append(words + links + words_in_links)
        print(pom)
        result.append(pom)
        pom.pop(1)
        pom.pop(0)
    return result





directory = str(input("Unesi korenski direktorijum"))
start_time = time.time()
load(directory)
print("vreme: " + str(time.time() - start_time))

print(len(graph.vertices))
print(len(graph.edges))
