import math
from collections import deque
from copy import deepcopy
from sys import path


class Graph:

    def __init__(self, id):
        self.__id = id
        self.__nbNoeuds = 0
        self.__noeuds = {}
        self.__liens = {}
        self.__demands = {}

    def getNbNoeuds(self):
        return self.__nbNoeuds

    def ajoutNoeud(self, noeud):
        self.__noeuds[noeud.getId()] = noeud
        self.__nbNoeuds += 1

    def ajoutLien(self, lien):
        self.__liens[lien.getId()] = lien
        lien.getSource().ajoutIdentifiantLien(lien.getId())
        lien.getDestination().ajoutIdentifiantLien(lien.getId())

    def ajoutDemande(self, demande):
        self.__demands[demande.getId()] = demande

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

    def getTotalCost(self):
        sum = 0
        for lien in self.__liens.values():
            sum += lien.getCost()
        return sum

    def getCostOfPath(self, p):
        copyLinks = deepcopy(self.__liens)

        cost = 0
        for j in range(0, len(p) - 1):
            node1 = p[j]
            node2 = p[j + 1]
            linkid = "Link" + node1 + "_" + node2
            linkidAlt = "Link" + node2 + "_" + node1
            if linkid in copyLinks:
                cost += float(copyLinks[linkid].getSetupCost())
            elif linkidAlt in copyLinks:
                cost += float(copyLinks[linkidAlt].getSetupCost())

        return cost

    def dijkstra(self, sourceNode, destNode):
        nodesCopy = deepcopy(self.__noeuds)
        assert sourceNode in nodesCopy, 'such source node does not exist'
        assert destNode in nodesCopy, 'such destination node does not exist'

        path = []

        inf = float('inf')
        setupCosts = {node: inf for node in nodesCopy}
        setupCosts[sourceNode] = 0

        previousNodes = {node: None for node in nodesCopy}

        while nodesCopy:
            current_node = min(nodesCopy, key=lambda node: setupCosts[node])
            del nodesCopy[current_node]
            liensVoisins = self.obtenirLiensVoisins(current_node)
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

    def glouton(self):
        for demand_key, demand_value in self.__demands.items():
            path = self.dijkstra(demand_value.getSource(), demand_value.getTarget())
            for i in range(0, len(path) - 1):
                linkid = "Link" + path[i] + "_" + path[i + 1]
                linkidAlt = "Link" + path[i + 1] + "_" + path[i]
                if linkid in self.__liens:
                    self.__liens[linkid].addToCapacity(float(demand_value.getDemandValue()))
                elif linkidAlt in self.__liens:
                    self.__liens[linkidAlt].addToCapacity(float(demand_value.getDemandValue()))
        return self.getTotalCost()

    def yen(self, sourceNode, destNode, K):
        copyNodes = deepcopy(self.__noeuds)
        copyLinks = deepcopy(self.__liens)

        A = [self.dijkstra(sourceNode, destNode)]

        B = []

        for k in range(1, K):
            for i in range(0, len(A[k - 1]) - 2):

                spurNode = A[k - 1][i]
                rootPath = A[k - 1][0:i]

                for p in A:
                    if rootPath == p[0:i]:
                        node1 = p[i]
                        node2 = p[i + 1]
                        linkid = "Link" + node1 + "_" + node2
                        linkidAlt = "Link" + node2 + "_" + node1
                        if linkid in self.__liens:
                            del self.__liens[linkid]
                        elif linkidAlt in self.__liens:
                            del self.__liens[linkidAlt]

                for node in rootPath:
                    if node != spurNode:
                        liensVoisins = self.obtenirLiensVoisins(node)
                        for key, lien in liensVoisins.items():
                            del self.__liens[lien.getId()]
                        del self.__noeuds[node]

                spurPath = self.dijkstra(spurNode, destNode)
                totalPath = rootPath + spurPath

                if totalPath not in B:
                    B.append(totalPath)

                self.__noeuds = deepcopy(copyNodes)
                self.__liens = deepcopy(copyLinks)

            if len(B) == 0:
                # A verif
                break

            costMin = float('inf')
            minPath = []
            for p in B:
                cost = self.getCostOfPath(p)
                if cost < costMin:
                    costMin = cost
                    minPath = p

            A.append(minPath)

            B.remove(minPath)

        return A
