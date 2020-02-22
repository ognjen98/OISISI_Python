class Vertex:
    def __init__(self, x):
        self.element = x

    def get_element(self):
        return self.element

    def __str__(self):
        return str(self.element)

    def __eq__(self, other):
        return self.element == other.element


class Edge:
    def __init__(self, o, d, x=None):
        self.origin = o
        self.destination = d
        self.element = x

    def __str__(self):
        result = 'Izvor: ' + str(self.origin) + ' Odrediste: ' + str(self.destination)
        return result


class Graph:
    def __init__(self):
        self.vertices = []
        self.edges = []

    def get_vertices(self):
        return self.vertices

    def get_edges(self):
        return self.edges

    def edge_count(self):
        return len(self.edges)

    def vertex_count(self):
        return len(self.vertices)

    def insert_vertex(self, x=None):
        v = Vertex(x)
        if v not in self.vertices:
            self.vertices.append(v)
        return v

    def insert_edge(self, o, d, x=None):
        e = Edge(o, d, x)
        self.edges.append(e)

    def incident_edges(self, v, out=True):
        edges_list = []
        if out:
            for edge in self.edges:
                if edge.origin == v:
                    list.append(edge)
        else:
            for edge in self.edges:
                if edge.destination == v:
                    list.append(edge)
        return edges_list

    def degree(self, v, out=True):
        return len(self.incident_edges(v, out))
