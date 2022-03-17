class Lien:

    def __init__(self, source, destination, setupCost, id):
        self.__source = source
        self.__destination = destination
        self.__setupCost = float(setupCost)
        self.__id = id
        self.__capacity = 0

    def __str__(self):
        print('Lien -> id: {0}, noeud 1: {1}, noeud 2: {2}, setup cost: {3}, capacity: {4}'.format(self.__id, self.__source.getId(), self.__destination.getId(), self.__setupCost, self.__capacity))

    def getSource(self):
        return self.__source

    def getDestination(self):
        return self.__destination

    def getSetupCost(self):
        return self.__setupCost

    def getId(self):
        return self.__id

    def getCapacity(self):
        return self.__capacity

    def addToCapacity(self, capacity):
        self.__capacity += capacity
    
    def getCost(self):
        if self.__capacity <= 200:
            return self.__setupCost + 2*self.__setupCost
        elif self.__capacity <= 800:
            return 8*self.__setupCost*0.9
        elif self.__capacity <= 1600:
            return 16*self.__setupCost*0.85
        elif self.__capacity <= 3200:
            return 32*self.__setupCost*0.75
        elif self.__capacity <= 6400:
            return 32*self.__setupCost*0.75*2
        elif self.__capacity <= 12800:
            return 32*self.__setupCost*0.75*4
        elif self.__capacity <= 25600:
            return 32*self.__setupCost*0.75*8
        elif self.__capacity <= 51200:
            return 32*self.__setupCost*0.75*16
