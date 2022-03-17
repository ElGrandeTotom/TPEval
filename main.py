from init import *
import math
from collections import deque

graph = createGraphFromFile("network_instance.txt")
# path = graph.dijkstra("N01","N05")
createDemandsFromFile("network_instance.txt", graph)
total_cost = graph.glouton()
print(total_cost)