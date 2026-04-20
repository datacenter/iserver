from lib.k8s.bare_metal_host.api import K8sBareMetalHostApi
from lib.k8s.bare_metal_host.info import K8sBareMetalHostInfo
from lib.k8s.bare_metal_host.attach import K8sBareMetalHostAttach
from lib.k8s.bare_metal_host.bmc import K8sBareMetalHostBmc
from lib.k8s.bare_metal_host.create import K8sBareMetalHostCreate
from lib.k8s.bare_metal_host.delete import K8sBareMetalHostDelete
from lib.k8s.bare_metal_host.detach import K8sBareMetalHostDetach
from lib.k8s.bare_metal_host.inspect import K8sBareMetalHostInspect
from lib.k8s.bare_metal_host.power_on import K8sBareMetalHostPowerOn
from lib.k8s.bare_metal_host.power_off import K8sBareMetalHostPowerOff
from lib.k8s.bare_metal_host.reboot import K8sBareMetalHostReboot
from lib.k8s.bare_metal_host.secret import K8sBareMetalHostSecret
from lib.k8s.bare_metal_host.wait import K8sBareMetalHostWait


class K8sBareMetalHost(
        K8sBareMetalHostApi,
        K8sBareMetalHostInfo,
        K8sBareMetalHostAttach,
        K8sBareMetalHostBmc,
        K8sBareMetalHostCreate,
        K8sBareMetalHostDelete,
        K8sBareMetalHostDetach,
        K8sBareMetalHostInspect,
        K8sBareMetalHostPowerOn,
        K8sBareMetalHostPowerOff,
        K8sBareMetalHostReboot,
        K8sBareMetalHostSecret,
        K8sBareMetalHostWait
        ):
    def __init__(self):
        K8sBareMetalHostApi.__init__(self)
        K8sBareMetalHostInfo.__init__(self)
        K8sBareMetalHostAttach.__init__(self)
        K8sBareMetalHostBmc.__init__(self)
        K8sBareMetalHostCreate.__init__(self)
        K8sBareMetalHostDelete.__init__(self)
        K8sBareMetalHostDetach.__init__(self)
        K8sBareMetalHostInspect.__init__(self)
        K8sBareMetalHostPowerOn.__init__(self)
        K8sBareMetalHostPowerOff.__init__(self)
        K8sBareMetalHostReboot.__init__(self)
        K8sBareMetalHostSecret.__init__(self)
        K8sBareMetalHostWait.__init__(self)
