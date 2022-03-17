class Demand:
    def __init__(self, demand_id, source, target, routing_unit, demand_value, max_path_length):
        self.demand_id = demand_id
        self.source = source
        self.target = target
        self.routing_unit = routing_unit
        self.demand_value = demand_value
        self.max_path_lenght = max_path_length

    def printDemand(self):
        print("Demand : " + self.demand_id + "  " + self.source + " " + self.target + " " + self.routing_unit + " " + self.demand_value + " " + self.max_path_lenght)