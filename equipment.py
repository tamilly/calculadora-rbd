class Equipment():

    def __init__(self, availability, cost, equipment, is_parallel):
        self.availability = availability
        self.cost = cost
        self.equipment = equipment
        self.is_parallel = is_parallel
        self.qtd_parallel = 0
        self.unavailability = (1 - availability)
        self.unav_month = (self.unavailability * (30*24))
        self.unav_year = self.unav_month * 12