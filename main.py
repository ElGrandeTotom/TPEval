from init import *
import math
from collections import deque

# nodesList = createNodesFromFile("network_instance.txt")
# for node in nodesList:
#     node.printNode()

# linksList = createLinksFromFile("network_instance.txt")
# for link in linksList:
#     link.printLink()

# demandsList = createDemandsFromFile("network_instance.txt")
# for demand in demandsList:
#     demand.printDemand()

graph = createGraphFromFile("network_instance.txt")
# graph.__str__()
path = graph.dijkstra2("N01","N17")
print(path)