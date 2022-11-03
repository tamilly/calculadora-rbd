class RBD():

    def __init__(self, alternative, availability, cost):
        self.alternative = alternative
        self.availability = availability
        self.cost = cost
        self.unavailability = (1 - availability)
