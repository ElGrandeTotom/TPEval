class Demand:
    def __init__(self, demand_id, source, target, demand_value):
        self.demand_id = demand_id
        self.source = source
        self.target = target
        self.demand_value = demand_value

    def printDemand(self):
        print("Demand : " + self.demand_id + "  " + self.source + " " + self.target + " " + self.demand_value)

    def getId(self):
        return self.demand_id

    def getSource(self):
        return self.source

    def getTarget(self):
        return self.target
    
    def getDemandValue(self):
        return self.demand_value