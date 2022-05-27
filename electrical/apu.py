import IElectricalSystem


class apu(IElectricalSystem):
    """
        APU (auxiliary power unit) class -

        Provides electricity (for batteries and level 0 equipments)
        and pneumatic power for AC and equipment cooling

        WIP
        version 0.01
    """

    def __init__(self) -> None:
        super().__init__()

    def start(self):            # y a t il de l’electricité et du fuel pour le démarrer
        """
            try:
                batteries.voltage >= X:
            Except:
                batteries.power = False
            return batteries.power

            if fuel_level and batteries.power:
                generator_start = True
                
                
        """
        pass


    def fuel_consumption(self):  # consomme du fuel
        return fuel_consumption()

    def get_wattage(self):  # Produit de l’electricité
        pass


    def maintenance(self):  # Augmente la durée de vie mais pas la production
        pass
