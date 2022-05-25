import IPiping


class Pipe(IPiping):
    def __init__(self):
        pass

    def get_flow(self):
        pass

    def get_pressure(self):
        """
            Pression hydrostatique = masse volumique * Acceleration de la Pesanteur * hauteur(dans l'espace on s'en fout)
            Pression =

            return fuel_pipe_pressure
        """
        pass

    def get_temp(self):
        pass


class FuelPipe(IPiping):
    def __init__(self):
        super().__init__()
        self.masse_volumique_fuel = 70.973  # Masse Volumique de l'hygrogene liquide: 70.973 Kg/m3

class HydraulicPipe(IPiping):
    pass

class LiquidNitrogenPipe(IPiping):
    pass

class LowPressureO2Pipe(IPiping):
    pass

class HighPressureO2Pipe(IPiping):
    pass

class LowPressureWaterPipe(IPiping):
    pass


class PipeFactory(IPiping):
    @staticmethod
    def build_pipe(pipe_type):
        if pipe_type == "Fuel":
            return FuelPipe()

        if pipe_type == "HydraulicPipe":
            return HydraulicPipe()

        if pipe_type == "LowPressureWaterPipe":
            return LowPressureWaterPipe()

        if pipe_type == "LiquidNitrogenPipe":
            return LiquidNitrogenPipe()

        print("Invalid Type")
        return -1