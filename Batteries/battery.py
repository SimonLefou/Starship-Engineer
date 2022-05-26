import IElectricalSystem

class Battery(IElectricalSystem):

    def __init__(self, env):
        self.id = id
        self.max_capacity = max_capacity    # max_capacity = capacity * depth_of_discharge 
        self.efficiency = 0.95              # efficacité de 95% ou plus
        self.capacity = capacity            # capacité en Amp-Hr
        self.voltage = voltage              # voltage de la batterie : self.capacity * self.voltage = energy storage capacity
        self.temperature = temperature
        self.battery_state_of_charge = battery_state_of_charge      # ratio of the amount of energy presently stored in the battery
        self.depth_of_discharge = depth_of_discharge                # The Depth of Discharge (DOD) of a battery determines the fraction of power that can be withdrawn from the battery
        self.discharge_rate = discharge_rate                        # discharge_rate = capacity / time_to_full_discharge
        self.time_to_full_discharge = 20                            # temps necessaire au déchargement de la batterie approx 20h
        self.power_delivery = power_delivery                        # = discharge_rate * voltage    en Watt : puissance maximale théorique
        self.actual_power_delivery = capacity * DOD / time_to_full_discharge * voltage

    def battery_charging(self):
        battery_charge_state = False
        if bus.power_input > self.power_delivery:
            return battery_charge_state == True
        else:
            return battery_charge_state == False