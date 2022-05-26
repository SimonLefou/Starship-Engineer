from typing_extensions import Self
import IElectricalSystem


class SolarPanel(IElectricalSystem):
    __output = None
 

    def __init__(self, output: IElectricalSystem, max_wattage):
        self.__output = output
        self.max_wattage = max_wattage


    def get_wattage():
        pass

        Self.move_panel()


    def move_panel():
        """
        Method that moves the solar panels toward any solar source to max power output
        
        max_wattage: int Max theorical solar panel power output

        return current_wattage

        """

        """
        pan = 0   # You could choose any max angle, such as 5 to correspond to voltage input
        pan_max_angle = 45    

        last_voltage = 0
        voltage = 0
        
        pan_angle = 0   #Set initial angles
       
        #Read voltage then rotate until it finds max
        
        for pan_angle in range (0, pan_max_angle):
            if get_solar_angle(voltage) > max_voltage+0.01:
                max_voltage = voltage
                pan_angle += 1

            elif voltage
        """

    def get_solar_angle():
        pass