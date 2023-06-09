class VanagonBus:
    """This class models the engine and
    working requirements of the Volkswagen Vanagon bus"""
    def __init__(self):
        self.bus_requirements = {
            "petrol": 350,
            "engine_oil": 70,
            "radiator_water": 100,
        }

    def report(self):
        """This method prints a report of engine resources"""
        print(f"petrol: {self.bus_requirements['petrol']}l")
        print(f"engine oil: {self.bus_requirements['engine_oil']}l")
        print(f"radiator water: {self.bus_requirements['radiator_water']}l")

    def is_resource_sufficient(self, destination):
        """This method returns True when the bus can get to a destination,
        and False when there are insufficient resources"""
        can_go = True
        for item in destination.bus_requirements:
            if destination.bus_requirements[item] > self.bus_requirements[item]:
                print(f"Oga koshi bole, mi o ni {item} lati de ibe yen.")
                can_go = False
        return can_go

    def go_to_destination(self, customer_destination):
        """This method subtracts the resources required
        to move the bus to customer destination from the resources available"""
        for item in customer_destination.bus_requirements:
            self.bus_requirements[item] -= customer_destination.bus_requirements[item]
        print(f"O wa oooooo. "
              f"Oya bole, O loyun, O ponmo ooo. Aunty e smart up jare!!!!😠😠😠😠 ")
