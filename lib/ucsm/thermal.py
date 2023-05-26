from lib.ucsm.thermal_modules.chassis import ChassisThermal
from lib.ucsm.thermal_modules.server import ServerThermal
from lib.ucsm.thermal_modules.fi import FiThermal


class Thermal(ChassisThermal, ServerThermal, FiThermal):
    def __init__(self, log_id=None):
        ChassisThermal.__init__(self, log_id=log_id)
        ServerThermal.__init__(self, log_id=log_id)
        FiThermal.__init__(self, log_id=log_id)
