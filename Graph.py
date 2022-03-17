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
            if element.getSource() == id:
                dictionnaire[element.getDestination()] = element.getDestination()
            else:
                if element.getDestination() == id:
                    dictionnaire[element.getSource()] = element.getSource()
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
        """Recherche du plus court chemin dans le graphe entre deux noeuds dont les identifiants sont passés en paramètre"""
        assert sourceNode in self.__noeuds, 'such source node does not exist'
        assert destNode in self.__noeuds, 'such destination node does not exist'

        inf = float('inf')

        setupCosts = {node: inf for node in self.__noeuds}
        previous_nodes = {
            node: None for node in self.__noeuds
        }
        setupCosts[sourceNode] = 0

        nddict = self.__noeuds.copy()
        nodes = set()
        for nd in nddict.keys():
            nodes.add(nd)

        while nodes:

            current_node = min(nodes, key=lambda node: setupCosts[node])
            print(nodes)
            # if setupCosts[current_node] == inf:
            #     break

            for neighbour, cost in self.obtenirProchainsNoeuds(current_node).items():
                alternative_route = setupCosts[current_node] + cost

                if alternative_route < setupCosts[neighbour]:
                    setupCosts[neighbour] = alternative_route
                    previous_nodes[neighbour] = current_node

            nodes.remove(current_node)

        path, current_node = deque(), destNode
        while previous_nodes[current_node] is not None:
            path.appendleft(current_node)
            current_node = previous_nodes[current_node]
        if path:
            path.appendleft(current_node)
        return path

    def dijkstra2(self, sourceNode, destNode):
        """Recherche du plus court chemin dans le graphe entre deux noeuds dont les identifiants sont passés en paramètre"""
        assert sourceNode in self.__noeuds, 'such source node does not exist'
        assert destNode in self.__noeuds, 'such destination node does not exist'

        inf = float('inf')
        setupCosts = {node: inf for node in self.__noeuds}
        setupCosts[sourceNode] = 0

        # previous_nodes = {
        #     node: None for node in self.__noeuds
        # }

        nodesCopy = self.__noeuds.copy()
        # nodesIds = []
        # for node in nodesCopy:
        #     print(node)
        #     nodesIds.append(node)

        while nodesCopy:
            print(nodesCopy)