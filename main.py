from init import *
import math
from collections import deque

graph = createGraphFromFile("network_instance.txt")
path = graph.dijkstra("N01", "N07")
# print(path)
createDemandsFromFile("network_instance.txt", graph)
total_cost = graph.glouton()
A = graph.yen("N01", "N07", 3)

print(A)
