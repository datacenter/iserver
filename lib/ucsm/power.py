from lib.ucsm.power_modules.chassis import ChassisPower
from lib.ucsm.power_modules.server import ServerPower
from lib.ucsm.power_modules.fi import FiPower


class Power(ChassisPower, ServerPower, FiPower):
    def __init__(self):
        ChassisPower.__init__(self)
        ServerPower.__init__(self)
        FiPower.__init__(self)
