from lib.k8s.openstack_volume_populator.api import K8sOpenstackVolumePopulatorApi
from lib.k8s.openstack_volume_populator.info import K8sOpenstackVolumePopulatorInfo


class K8sOpenstackVolumePopulator(
        K8sOpenstackVolumePopulatorApi,
        K8sOpenstackVolumePopulatorInfo
        ):
    def __init__(self):
        K8sOpenstackVolumePopulatorApi.__init__(self)
        K8sOpenstackVolumePopulatorInfo.__init__(self)
