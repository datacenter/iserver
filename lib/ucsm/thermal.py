from lib.ucsm.thermal_modules.chassis import ChassisThermal
from lib.ucsm.thermal_modules.server import ServerThermal
from lib.ucsm.thermal_modules.fi import FiThermal


class Thermal(ChassisThermal, ServerThermal, FiThermal):
    def __init__(self):
        ChassisThermal.__init__(self)
        ServerThermal.__init__(self)
        FiThermal.__init__(self)
