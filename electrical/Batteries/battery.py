# import IElectricalSystem
# import battery_constants

class Battery():
    """Class for the starship batteries

            Ce que l'on connait des batteries:
                leur voltage                constants 240
                leur capacité max           30000 Ah
                leur efficacité             95%
                leur c-rate                 0.2
                leur nombre de cycle max    3500

            permet d'obtenir
                la puissance max en KWh théorique                       Voltage * Capacité Max
                le courant de décharge max en A                         c-rate * puissance_max * efficacité         Battery.voltage * Battery.max_capacity
                temps de fonctionnement à pleine capacité (en mins)     = capacité max * efficacité / output * 60   Battery.c_rate * max_theoretical_power * Battery.efficiency

    """

    def __init__(self, battery_fail=False, voltage=240, max_capacity=30000, efficiency=0.95, c_rate=0.2, max_cycle= 3500):
        self.battery_fail = battery_fail
        self.voltage = voltage
        self.max_capacity = max_capacity
        self.efficiency = efficiency
        self.c_rate = c_rate
        self.max_cycle = max_cycle

    def max_power(self):
        max_theoretical_power = self.voltage * self.max_capacity
        return max_theoretical_power

    def max_discharge_current(self):
        max_discharge = self.c_rate * self.max_power() * self.efficiency
        return max_discharge

    def running_time(self):
        running_time = self.max_capacity * self.efficiency / _output
        return running_time

    def battery_fail(self):
        if _output > self.max_discharge_current():
            self.battery_fail = True
        self.battery_fail = False

"""
 a implementer
        __output = None
        __input = None
        low_batt
        full_batt
        charging if low_batt and input > 0
"""


battery1 = Battery()
power = battery1.max_power()
discharge = battery1.max_discharge_current()
_output = 1000
running = battery1.running_time()


print(f"Capacity = {int(power/1000)}KWh")
print(f"Evailable power = {discharge}A")
print(f"{int(running)}h and {(running % 1)*60}mins ")

"""           

Version 0

                # input: IElectricalSystem,
                 # output: IElectricalSystem,
                 # battery_state_of_charge,
                 discharge_rate,
                 power_delivery,
                 current_capacity=0.0,
                 capacity_deliverable=0.0,
                 actual_power_delivery=0,
                 energy_stored=300,
                 depth_of_discharge=55 / 100,
                 temperature=24.0,
                 number_charge_discharge=155,
                 voltage=240.0,
                 current_voltage=56.0,
                 time_to_full_discharge=20,
                 battery_lifetime=6000,
                 max_capacity=3000.0,
                 charge_speed=40 / 60
                 
        
        self.max_capacity = max_capacity                            # en Ah
        self.efficiency = 0.95                                      # efficacité de 95% ou plus
        self.capacity_deliverable = capacity_deliverable            # capacity deliverable au maximum = self.max_capacity / self.depth_of_discharge * self.efficiency
        self.charge_speed = charge_speed                            # Capacité de charge de la batterie 40 Kw / 60 mins soit 40KwH
        self.current_capacity = current_capacity                    # intensité acutelle de la batterie = 1 * capacity_deliverable
        self.voltage = voltage                                      # voltage de la batterie : self.capacity * self.voltage = energy storage capacity
        self.current_voltage = current_voltage                      # = Energy_stored / capacity
        self.temperature = temperature
        # self.battery_state_of_charge = battery_state_of_charge      # ratio of the amount of energy presently stored in the battery
        self.depth_of_discharge = depth_of_discharge                # The Depth of Discharge (DOD) of a battery determines the fraction of power that can be withdrawn from the battery
        self.discharge_rate = discharge_rate                        # discharge_rate = max_capacity / time_to_full_discharge soit ici soit ici 150A / h
        self.time_to_full_discharge = time_to_full_discharge        # temps necessaire au déchargement de la batterie approx 20h
        self.power_delivery = power_delivery                        # = discharge_rate * voltage    en Watt : puissance maximale théorique
        self.actual_power_delivery = actual_power_delivery
        self.battery_lifetime = battery_lifetime                    # nombre de cycles charge / décharge max que la batterie peut supporter
        self.number_charge_discharge = number_charge_discharge
        self.energy_stored = energy_stored






    def battery_charging(self):

        Method to set the batteries in charging state

        Returns:
            Bool: charging_mode
        

        if input.power_input > self.power_delivery:
            return self.charging_mode == True
        else:
            return self.charging_mode == False

    def get_wattage(self):

        if self.max_capacity >= self.capacity_deliverable:
            self.actual_power_delivery = self.max_capacity * self.depth_of_discharge / self.time_to_full_discharge * self.voltage
            return self.actual_power_delivery
        else:
            self.actual_power_delivery = 0
            return self.actual_power_delivery

    def charge(self):
        if self.power_delivery <= 0 and self.current_capacity != self.capacity_deliverable:
            self.charging_mode == True
            while self.charging_mode:  # tant que le mode de la batterie est en charge
                self.energy_stored += self.charge_speed  # charge la batterie
        else:
            return self.charging_mode == False

    def current_voltage(self):

         Return current battery voltage
            = energy_stored / current_capacity
        
        current_voltage = self.energy_stored / self.current_capacity
        return current_voltage

    def capacity_deliverable(self):
        # capacity deliverable au maximum = self.max_capacity / self.depth_of_discharge * self.efficiency
        capacity_deliverable = self.max_capacity / self.depth_of_discharge * self.efficiency
        return capacity_deliverable

    def current_capacity(self):
        # intensité actuelle de la batterie = 1 * capacity_deliverable
        current_capacity = 1 * self.capacity_deliverable
        return current_capacity

    def battery_state_of_charge(self):
        # ratio of the amount of energy presently stored in the battery
        battery_state_of_charge = self.current_capacity / self.max_capacity * 100
        return battery_state_of_charge

    def discharge_rate(self):
        # discharge_rate = max_capacity / time_to_full_discharge soit ici soit ici 150A / h
        self.discharge_rate = self.max_capacity / self.time_to_full_discharge
        return self.discharge_rate

"""

