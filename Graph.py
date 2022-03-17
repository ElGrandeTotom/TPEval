import math
from collections import deque

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


    def glouton(self):
        for demand_key, demand_value in self.__demands.items():
            path = self.dijkstra(demand_value.getSource(), demand_value.getTarget())
            for i in range(0,len(path)-1):
                # print("--- New link ---")
                linkid = "Link"+path[i]+"_"+path[i+1]
                linkidAlt = "Link"+path[i+1]+"_"+path[i]
                if linkid in self.__liens:
                    # self.__liens[linkid].__str__() 
                    self.__liens[linkid].addToCapacity(float(demand_value.getDemandValue())) 
                    # self.__liens[linkid].__str__() 
                elif linkidAlt in self.__liens:
                    # self.__liens[linkidAlt].__str__() 
                    self.__liens[linkidAlt].addToCapacity(float(demand_value.getDemandValue()))   
                    # self.__liens[linkidAlt].__str__()
        return self.getTotalCost()