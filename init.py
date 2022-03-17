from Graph import Graph
from Lien import Lien
from Demand import Demand
from Noeud import Noeud

# def createNodesFromFile(filename):
#     file = open(filename,'r')
#     lines = file.readlines()

#     nodesList = []

#     for i in range(8,33):
#         line = lines[i].split(" ")
#         nodeToAdd = Noeud(line[2], line[4], line[5])
#         nodesList.append(nodeToAdd)

#     return nodesList

# def createLinksFromFile(filename):
#     file = open(filename,'r')
#     lines = file.readlines()

#     linksList = []

#     for i in range(40,85):
#         line = lines[i].split(" ")
#         linkToAdd = Lien(line[2],line[4],line[5],line[7],line[8],line[9],line[10],line[12],line[13])
#         linksList.append(linkToAdd)
    
#     return linksList

def createDemandsFromFile(filename):
    file = open(filename,'r')
    lines = file.readlines()

    demands = []

    for i in range(92, 392):
        line_split = lines[i].split(" ")
        d = Demand(line_split[2], line_split[4], line_split[5], line_split[7], line_split[8], line_split[9])
        demands.append(d)

    return demands

def createGraphFromFile(filename):
    
    file = open(filename, 'r')
    graph = Graph("Super graphe")

    lines = file.readlines()

    nbNodes = 25

    """Création des noeuds"""
    for i in range(8, 33):
        graph.ajoutNoeud(Noeud(lines[i].split(" ")[2]))

    for j in range(40,85):
        line = lines[j].split(" ")
        graph.ajoutLien(Lien(graph.getNoeud(line[4]), graph.getNoeud(line[5]), float(line[10]), line[2]))

    return graph