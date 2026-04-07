from lib.k8s.frr_configuration.api import K8sFrrConfigurationApi
from lib.k8s.frr_configuration.info import K8sFrrConfigurationInfo
from lib.k8s.frr_configuration.create import K8sFrrConfigurationCreate
from lib.k8s.frr_configuration.delete import K8sFrrConfigurationDelete
from lib.k8s.frr_configuration.update import K8sFrrConfigurationUpdate
from lib.k8s.frr_configuration.wait import K8sFrrConfigurationWait


class K8sFrrConfiguration(
        K8sFrrConfigurationApi,
        K8sFrrConfigurationInfo,
        K8sFrrConfigurationCreate,
        K8sFrrConfigurationDelete,
        K8sFrrConfigurationUpdate,
        K8sFrrConfigurationWait
        ):
    def __init__(self):
        K8sFrrConfigurationApi.__init__(self)
        K8sFrrConfigurationInfo.__init__(self)
        K8sFrrConfigurationCreate.__init__(self)
        K8sFrrConfigurationDelete.__init__(self)
        K8sFrrConfigurationUpdate.__init__(self)
        K8sFrrConfigurationWait.__init__(self)
