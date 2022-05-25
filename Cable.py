import IElectricalSystem


class Cable(IElectricalSystem):
    __input = None
    __output = None
    __resistance = 1    # Ohm

    def __int__(self, entree: IElectricalSystem, output: IElectricalSystem, resistance=1, ):
        self.__input = entree
        self.__output = output
        self.__resistance = resistance

    def get_temp(self):
        power = self.__input.get_wattage()
        temp = power * self.__resistance
        # TODO Calculer inertie thermique
        return temp

    def get_wattage(self):
        """ TODO trouver la formule elctrique de la resistance electrique
                P = U * I = R ** I au carré

                R = p * L/S
                    R = Resistance elect en ohm R
                    p = Resistivite en ohm - m
                    L = Longueur du cable
                    S = Section en m2
                pour du 4mm2 R = 4.39 Ohm / Km

            Calculer la puissance effective en sortie
        """
        return self.__input.get_wattage()


# if voltage < 0 COUILLE
