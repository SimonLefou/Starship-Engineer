from abc import *


class IPiping(ABC):
    @abstractmethod
    def pipe_type(self):
        """ Inteface method
            Type of pipe :
                Hydraulic,
                Fuel,
                liquid hydrogene LH2,
                liquid nitrogen,
                low pressure Water,
                high pressure oxygen,
                low pressure air
        """
        pass

    @abstractmethod
    def get_pressure(self):
        """ Inteface method """
        pass

    @abstractmethod
    def get_flow(self):
        """ Inteface method """
        pass

    @abstractmethod
    def get_temp(self):
        """ Inteface method """
        pass
