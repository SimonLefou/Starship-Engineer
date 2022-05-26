import IElectricalSystem
import battery_constants
import constants

class Battery(IElectricalSystem):
    __output = None
    __input = None


    def __init__(self,  input: IElectricalSystem,
                        output: IElectricalSystem,
                        capacity_deliverable,
                        current_capacity,
                        temperature,
                        battery_state_of_charge, 
                        depth_of_discharge,
                        discharge_rate,
                        power_delivery,
                        actual_power_delivery,
                        number_charge_discharge,
                        energy_stored,
                        voltage = 240,
                        current_voltage = 56,
                        time_to_full_discharge = 20,
                        battery_lifetime = 6000,
                        max_capacity = 3000,
                        chargeSpeed = 40/60
                ):


        self.max_capacity = max_capacity                            # en Ah
        self.efficiency = 0.95                                      # efficacité de 95% ou plus
        self.capacity_deliverable = capacity_deliverable            # capacity deliverable au maximum = self.max_capacity / self.depth_of_discharge * self.efficiency
        self.chargeSpeed = chargeSpeed                              # Capacité de charge de la batterie 40 Kw / 60 mins soit 40KwH 
        self.current_capacity = current_capacity                    # intensité acutelle de la batterie = 1 * capacity_deliverable
        self.voltage = voltage                                      # voltage de la batterie : self.capacity * self.voltage = energy storage capacity
        self.current_voltage = current_voltage                      # = Energy_stored / capacity
        self.temperature = temperature
        self.battery_state_of_charge = battery_state_of_charge      # ratio of the amount of energy presently stored in the battery
        self.depth_of_discharge = depth_of_discharge                # The Depth of Discharge (DOD) of a battery determines the fraction of power that can be withdrawn from the battery
        self.discharge_rate = discharge_rate                        # discharge_rate = max_capacity / time_to_full_discharge soit ici soit ici 150A / h
        self.time_to_full_discharge = time_to_full_discharge        # temps necessaire au déchargement de la batterie approx 20h
        self.power_delivery = power_delivery                        # = discharge_rate * voltage    en Watt : puissance maximale théorique
        self.actual_power_delivery = actual_power_delivery
        self.battery_lifetime = battery_lifetime                    # nombre de cycles charge / décharge max que la batterie peut supporter
        self.number_charge_discharge = number_charge_discharge
        self.energy_stored = energy_stored


    def battery_charging(self):
        if input.power_input > self.power_delivery:
            return self.chargingMode == True
        else:
            return self.chargingMode == False
        
    
    def get_wattage(self):
        if self.max_capacity >= self.capacity_deliverable:
            self.actual_power_delivery = self.max_capacity * self.depth_of_discharge / self.time_to_full_discharge * self.voltage
            return self.actual_power_delivery
        else:
            self.actual_power_delivery = 0
            return self.actual_power_delivery
    

    def charge(self):
        if input.power_input > self.power_delivery:
            self.chargingMode == True
            self.energy_stored += self.chargeSpeed
            return self.energy_stored
        else:
            return self.chargingMode == False


    def current_voltage(self):
        """
            Return current battery voltage
            = energy_stored / current_capacity
        """
        self.current_voltage = self.energy_stored / self.current_capacity
        print(self.current_voltage)
        return self.current_voltage

    
    def capacity_deliverable(self):
        self.capacity_deliverable = self.max_capacity / self.depth_of_discharge * self.efficiency
        return self.capacity_deliverable
    
