from abc import *
from multiprocessing.sharedctypes import Value


class IElectricalSystem(ABC):
    def __init__(self, n):
        self.wattage = n

    @abstractmethod
    def get_wattage(self):
        pass



    # Proposition pour remplacer les methodes get_wattage

    @property
    def wattage(self):          # method getter
        return self._wattage
        

    @wattage.setter
    def wattage(self, value):   # method setter
        self._wattage = value
