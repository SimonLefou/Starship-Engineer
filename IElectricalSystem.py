from abc import *


class IElectricalSystem(ABC):
    @abstractmethod
    def get_wattage(self):
        pass

