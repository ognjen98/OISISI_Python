from OISISI_Python.Python_projekat.Strukture.set import *


class Vertex:

    def __init__(self, x):
        self.element = x

    def __key(self):
        return (self.element)

    def get_element(self):
        return self.element

    def __eq__(self, other):
        return self.element == other.element

    def __hash__(self):
        return hash(id(self))

    def __str__(self):
        return str(self.element)


class Edge:
    def __init__(self, o, d, x):
        self.origin = o
        self.destination = d
        self.element = x

    def endspoint(self):
        return (self.origin, self.destination)

    def oposite(self, v):
        return self.destination if v is self.origin else self.origin

    def element(self):
        return self.element

    def __hash__(self):
        return hash((self.origin, self.destination))

    def __str__(self):
        result = "Izvorni cvor: " + str(self.origin) + " Odredisni cvor: " + str(self.destination) + " Grana: " + str(
            self.element)
        return result


class Graph:
    def __init__(self):
        self.outgoing = {}
        self.incoming = {}

    def vertex_count(self):
        return len(self.outgoing)

    def vertices(self):
        return self.outgoing.keys()

    def edge_count(self, v):
        return sum(len(self.outgoing[v]) for v in self.outgoing)

    def edges(self):
        result = Set()
        for secondary_map in self.outgoing.values():
            result.add(secondary_map.values())
        return result

    def get_edge(self, o, d):
        return self.outgoing[o].get(d)

    def degree(self, v, outgoing = True):
        adj = self.outgoing if outgoing else self.incoming
        return len(adj[v])

    def incident_edges(self, v, outgoing = True):
        list = []
        adj = self.outgoing if outgoing else self.incoming
        for edge in adj:
            list.append(edge)
        return list

    def insert_vertex(self, v=None):
        self.outgoing[v] = {}
        self.incoming[v] = {}
        return v

    def insert_edges(self, o, d, x=None):
        e = Edge(o, d, x)
        self.outgoing[o][d] = e
        self.incoming[d][o] = e

    def __str__(self):
        res = 'Cvorovi: '
        for el in self.outgoing.keys():
            res += str(el)
        return res


graph = Graph()
vertex1 = Vertex('a')
vertex2 = Vertex('b')
graph.insert_vertex(vertex1)
graph.insert_vertex(vertex2)
vertex3 = Vertex("c")
graph.insert_vertex(vertex3)
graph.insert_edges(vertex1, vertex2, "ab")
graph.insert_edges(vertex1, vertex3, "ac")

outgoing = {}
outgoing['b'] = {}
outgoing['b']['a'] = "gdgdksgkdsl"
for value in graph.incoming.values():
    for value1 in value.values():
        print(value1)
list = graph.incident_edges(vertex2)
for value in list:
    print(value)
print(graph.degree(vertex2))