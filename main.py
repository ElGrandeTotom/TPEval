from init import *
import math
from collections import deque

graph = createGraphFromFile("network_instance.txt")
path = graph.dijkstra("N01","N17")
print(path)