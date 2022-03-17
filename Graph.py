import math
from collections import deque

class Graph:

    def __init__(self, id):
        self.__id = id
        self.__nbNoeuds = 0
        self.__noeuds = {}
        self.__liens = {}

    def getNbNoeuds(self):
        return self.__nbNoeuds

    def ajoutNoeud(self, noeud):
        self.__noeuds[noeud.getId()] = noeud
        self.__nbNoeuds += 1

    def ajoutLien(self, lien):
        self.__liens[lien.getId()] = lien
        lien.getSource().ajoutIdentifiantLien(lien.getId())
        lien.getDestination().ajoutIdentifiantLien(lien.getId())

    def obtenirProchainsNoeuds(self, id):
        dictionnaire = {}
        for element in self.__liens.values():
            if element.getSource().getId() == id:
                dictionnaire[element.getDestination().getId()] = element.getDestination()
            else:
                if element.getDestination().getId() == id:
                    dictionnaire[element.getSource().getId()] = element.getSource()
        return dictionnaire

    def obtenirLiensVoisins(self, id):
        dictionnaire = {}
        for element in self.__liens.values():
            if element.getSource().getId() == id:
                dictionnaire[element.getDestination().getId()] = element
            else:
                if element.getDestination().getId() == id:
                    dictionnaire[element.getSource().getId()] = element
        return dictionnaire

    def __str__(self):
        print("Liste des noeuds : ")
        for value in self.__noeuds.values():
            value.__str__()
        print("Liste des liens : ")
        for value in self.__liens.values():
            value.__str__()


    def getNoeud(self, id):
        return self.__noeuds[id]

    def dijkstra(self, sourceNode, destNode):
        assert sourceNode in self.__noeuds, 'such source node does not exist'
        assert destNode in self.__noeuds, 'such destination node does not exist'

        inf = float('inf')
        setupCosts = {node: inf for node in self.__noeuds}
        setupCosts[sourceNode] = 0

        nodesCopy = self.__noeuds.copy()

        path = []
        previousNodes = {node: None for node in self.__noeuds}

        while nodesCopy:
            current_node = min(nodesCopy, key=lambda node: setupCosts[node])
            # path.append(current_node)
            del nodesCopy[current_node]
            liensVoisins = self.obtenirLiensVoisins(current_node)
            minSetupCost = inf
            for key, value in liensVoisins.items():
                if setupCosts[current_node] + value.getSetupCost() < setupCosts[key]:
                    setupCosts[key] = setupCosts[current_node] + value.getSetupCost()
                    previousNodes[key] = current_node
        current_node = destNode
        while previousNodes[current_node] is not None:
            path.append(current_node)
            current_node = previousNodes[current_node]
        path.append(current_node)
        path.reverse()
        return path
