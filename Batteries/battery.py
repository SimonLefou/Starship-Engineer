from socket import CAN_RAW_FILTER
import IElectricalSystem

class Battery(IElectricalSystem):

    def __init__(self,  max_capacity = 100, 
                        capacity_deliverable,
                        current_capacity,
                        c_rate = 1, 
                        voltage = 48,
                        actual_voltage,
                        temperature,
                        battery_state_of_charge, 
                        depth_of_discharge,
                        discharge_rate,
                        time_to_full_discharge = 20,
                        power_delivery,
                        actual_power_delivery,
                        number_charge_discharge,
                        battery_lifetime = 6000

                        ):


        self.max_capacity = max_capacity                            # en Ah
        self.efficiency = 0.95                                      # efficacité de 95% ou plus
        self.capacity_deliverable = capacity_deliverable            # capacity deliverable au maximum = Max_capacity / depth_of_discharge
        self.c_rate = c_rate                                        # coefficient de charge de la batterie : 1C = 1 heure de charge pour charger 100Ah (si recoit 100Ah en entrée. Si recoit plus ca reste 1h. Si recoit moins le temps est multiplié)
        self.current_capacity = current_capacity                    # intensité acutelle de la batterie = 1 * capacity_deliverable
        self.voltage = voltage                                      # voltage de la batterie : self.capacity * self.voltage = energy storage capacity
        self.actual_voltage = actual_voltage                        # = Energy_stored / capacity
        self.temperature = temperature
        self.battery_state_of_charge = battery_state_of_charge      # ratio of the amount of energy presently stored in the battery
        self.depth_of_discharge = depth_of_discharge                # The Depth of Discharge (DOD) of a battery determines the fraction of power that can be withdrawn from the battery
        self.discharge_rate = discharge_rate                        # discharge_rate = capacity / time_to_full_discharge
        self.time_to_full_discharge = time_to_full_discharge        # temps necessaire au déchargement de la batterie approx 20h
        self.power_delivery = power_delivery                        # = discharge_rate * voltage    en Watt : puissance maximale théorique
        self.actual_power_delivery = actual_power_delivery
        self.battery_lifetime = battery_lifetime                    # nombre de cycles charge / décharge max que la batterie peut supporter
        self.number_charge_discharge = number_charge_discharge


    def battery_charging(self):
        battery_charge_state = False
        if electrical_bus.power_input > self.power_delivery:
            return battery_charge_state == True
        else:
            return battery_charge_state == False
        
    
    def get_wattage(self):
        self.actual_power_delivery = self.capacity * self.depth_of_discharge / self.time_to_full_discharge * self.voltage
        return self.actual_power_delivery

    
