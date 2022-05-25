import IElectricalSystem
import random

class Generator(IElectricalSystem):
    __input = None
    __ouput = None

    def __init__(self):
        pass

    def get_wattage(self):
        max_power = 15000
        runing_power = max_power * 0.75
        # TODO calculer l'output en fonction du fuel (par ex X Watt / Fuel / sec), puissance,....
        return runing_power

    def execute_maintenance(self):
        pass

    def get_repair_state(self):
        pass
