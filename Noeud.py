class Noeud:

    def __init__(self, id):
        self.__id = id
        self.__liens = list()

    def __str__(self):
        print('Noeud -> id: {0}'.format(self.__id))

    def affichageIdentifiantLien(self):
        for index in self.__liens:
            print(index)

    def ajoutIdentifiantLien(self, id):
        self.__liens.append(id)

    def getId(self):
        return self.__id