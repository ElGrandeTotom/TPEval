from Graph import Graph
from Lien import Lien
from Demand import Demand
from Noeud import Noeud


def createDemandsFromFile(filename, graph):
    file = open(filename, 'r')
    lines = file.readlines()
    for i in range(92, 392):
        line_split = lines[i].split(" ")
        d = Demand(line_split[2], line_split[4], line_split[5], line_split[8])
        graph.ajoutDemande(d)


def createGraphFromFile(filename):
    file = open(filename, 'r')
    graph = Graph("Super graphe")
    lines = file.readlines()
    """Création des noeuds"""
    for i in range(8, 33):
        graph.ajoutNoeud(Noeud(lines[i].split(" ")[2]))
    """Création des liens"""
    for j in range(40, 85):
        line = lines[j].split(" ")
        graph.ajoutLien(Lien(graph.getNoeud(line[4]), graph.getNoeud(line[5]), float(line[10]), line[2]))
    return graph
