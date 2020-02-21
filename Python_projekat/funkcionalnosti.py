from OISISI_Python.Python_projekat.parser import *
from OISISI_Python.Python_projekat.Strukture.graph import *
from OISISI_Python.Python_projekat.Strukture.set import *
import os
import time
parser = Parser()

graph = Graph()
skup = Set()
def load(directory) :

    for file in os.listdir(directory):
        if os.path.isdir(os.path.join(directory, file)):
            load(os.path.join(directory, file))
        else:
            if file.endswith(".html"):
                skup.add(os.path.join(directory, file))
                list = parser.parse(os.path.join(directory, file))
                links = list[0]
                for link in links:
                    cvor1 = Vertex(os.path.join(directory, file))
                    graph.insert_vertex(cvor1)
                    cvor2 = Vertex(link)
                    graph.insert_vertex(cvor2)
                    graph.insert_edges(cvor1, cvor2)




directory = str(input("Unesi korenski direktorijum"))
start_time = time.time()
load(directory)
print("vreme: " + str(time.time() - start_time))
print(len(skup))
