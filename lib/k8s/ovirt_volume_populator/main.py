from lib.k8s.ovirt_volume_populator.api import K8sOvirtVolumePopulatorApi
from lib.k8s.ovirt_volume_populator.info import K8sOvirtVolumePopulatorInfo


class K8sOvirtVolumePopulator(
        K8sOvirtVolumePopulatorApi,
        K8sOvirtVolumePopulatorInfo
        ):
    def __init__(self):
        K8sOvirtVolumePopulatorApi.__init__(self)
        K8sOvirtVolumePopulatorInfo.__init__(self)
