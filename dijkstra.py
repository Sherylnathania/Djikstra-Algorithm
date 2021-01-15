import sys

class Node:
    def __init__(self, name): #init itu nama fungsi yang akan dikerjakan saat fungsi dipanggil
        self.name = name;
        self.distance = sys.maxsize
        self.visited = False
        self.edges = set()
        self.neighbours = set()
        self.parent = None

class Edge:
    def __init__(self, frm, to, length):
        self.frm = frm
        self.to = to
        self.length = length

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = set()
        self.start = None
        self.finish = None

    def add_node(self, name):
        self.nodes.add(Node(name))
        
    def find_node(self, name):
        for node in self.nodes:
            if node.name == name:
                return node

    def add_edge(self, frm, to, length):
        frm = self.find_node(frm)
        to = self.find_node(to)
        self.edges.add(Edge(frm, to, length))
        self.edges.add(Edge(to, frm, length))
        if to != frm:
            to.neighbours.add(frm)
            frm.neighbours.add(to)

    def add_distance_neighbour(self, a, b):
        self.find_node(a).edges.add(self.find_edge(a,b))
        self.find_node(b).edges.add(self.find_edge(b,a))

    def find_edge(self, frm, to):
        for edge in self.edges:
            if edge.frm == frm and edge.to == to:
                return edge

    def check_neighbour(self, node):
        for neighbour in node.neighbours:
            if neighbour.visited == False:
                if neighbour.distance > node.distance + self.find_edge(node, neighbour).length:
                    neighbour.distance = node.distance + self.find_edge(node, neighbour).length
                    neighbour.parent = node

    def visit(self):
        minimum = sys.maxsize
        for node in self.nodes:
            if node.visited == False and node.distance < minimum:
                minimum = node.distance
        for node in self.nodes:
            if node.visited == False and node.distance == minimum:
                node.visited = True
                return node

    def set_start(self, name):
        start = self.find_node(name)
        start.distance = 0
        start.visited = True
        self.start = start

    def set_finish(self, name):
        self.finish = self.find_node(name)

    def find_path(self):
        current = self.start
        while(not self.finish.visited):
            self.check_neighbour(current)
            current = self.visit()
        print(self.print_path(self.finish))
        print("Total distance:", self.finish.distance)

    def print_path(self, node):
        if node.parent == None:
            return node.name
        else:
            return self.print_path(node.parent) + '-' + node.name


maze = Graph()

maze.add_node('A')
maze.add_node('B')
maze.add_node('C')
maze.add_node('D')
maze.add_node('E')
maze.add_node('F')
maze.add_node('G')
maze.add_node('H')
maze.add_node('I')
maze.add_node('J')

maze.add_edge('A','B',2)
maze.add_edge('A','C',3)
maze.add_edge('A','E',4)
maze.add_edge('A','F',1)
maze.add_edge('C','G',5)
maze.add_edge('F','G',2)
maze.add_edge('F','E',5)
maze.add_edge('B','D',6)
maze.add_edge('E','D',2)
maze.add_edge('E','H',3)
maze.add_edge('D','H',2)
maze.add_edge('F','I',4)
maze.add_edge('I','H',1)
maze.add_edge('F','J',8)
maze.add_edge('G','J',7)
maze.add_edge('H','J',1)
maze.add_edge('F','E',5)
maze.add_edge('C','F',2)

maze.set_start('A')
maze.set_finish('J')

maze.find_path()
