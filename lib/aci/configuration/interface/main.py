from lib.aci.configuration.interface.api import ConfigurationInterfaceApi
from lib.aci.configuration.interface.create import ConfigurationInterfaceCreate
from lib.aci.configuration.interface.delete import ConfigurationInterfaceDelete
from lib.aci.configuration.interface.info import ConfigurationInterfaceInfo


class ConfigurationInterface(
        ConfigurationInterfaceApi,
        ConfigurationInterfaceCreate,
        ConfigurationInterfaceDelete,
        ConfigurationInterfaceInfo
    ):
    def __init__(self):
        ConfigurationInterfaceApi.__init__(self)
        ConfigurationInterfaceCreate.__init__(self)
        ConfigurationInterfaceDelete.__init__(self)
        ConfigurationInterfaceInfo.__init__(self)
