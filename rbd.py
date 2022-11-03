class RBD():

    def __init__(self, alternative, availability, cost):
        self.alternative = alternative
        self.availability = availability
        self.cost = cost
        self.unavailability = (1 - availability)
        self.norm_unav = None
        self.norm_cost = None
        self.distance = None
        self.unav_month = (self.unavailability * (30*24))
        self.unav_year = self.unav_month * 12
