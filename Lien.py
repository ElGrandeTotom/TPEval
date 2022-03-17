class Lien:

    def __init__(self, source, destination, setupCost, id):
        self.__source = source
        self.__destination = destination
        self.__setupCost = setupCost
        self.__id = id

    def __str__(self):
        print('Lien -> id: {0}, noeud 1: {1}, noeud 2: {2}, setup cost: {3}'.format(self.__id, self.__source.getId(), self.__destination.getId(), self.__setupCost))

    def getSource(self):
        return self.__source

    def getDestination(self):
        return self.__destination

    def getSetupCost(self):
        return self.__setupCost

    def getId(self):
        return self.__id
