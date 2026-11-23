from lib import log_helper

from lib.osp.api import OspApi
from lib.osp.common import OspCommon

from lib.osp.availability_zone.main import OspAvailabilityZone
from lib.osp.flavor.main import OspFlavor
from lib.osp.floating_ip.main import OspFloatingIp
from lib.osp.hypervisor.main import OspHypervisor
from lib.osp.image.main import OspImage
from lib.osp.network.main import OspNetwork
from lib.osp.port.main import OspPort
from lib.osp.quota.main import OspQuota
from lib.osp.role.main import OspRole
from lib.osp.router.main import OspRouter
from lib.osp.security_group.main import OspSecurityGroup
from lib.osp.snapshot.main import OspSnapshot
from lib.osp.subnet.main import OspSubnet
from lib.osp.tenant.main import OspTenant
from lib.osp.user.main import OspUser
from lib.osp.virtual_machine.main import OspVirtualMachine
from lib.osp.volume.main import OspVolume


class Osp(
        OspApi,
        OspCommon,
        OspAvailabilityZone,
        OspFlavor,
        OspFloatingIp,
        OspHypervisor,
        OspImage,
        OspNetwork,
        OspPort,
        OspQuota,
        OspRole,
        OspRouter,
        OspSecurityGroup,
        OspSnapshot,
        OspSubnet,
        OspTenant,
        OspUser,
        OspVirtualMachine,
        OspVolume
        ):
    def __init__(self, openrc_filename, cert_filename=None, log_id=None):
        self.log_id = log_id
        self.log = log_helper.Log(log_id=log_id)

        OspApi.__init__(self, openrc_filename, cert_filename)
        OspCommon.__init__(self)
        OspAvailabilityZone.__init__(self)
        OspFlavor.__init__(self)
        OspFloatingIp.__init__(self)
        OspHypervisor.__init__(self)
        OspImage.__init__(self)
        OspNetwork.__init__(self)
        OspPort.__init__(self)
        OspQuota.__init__(self)
        OspRole.__init__(self)
        OspRouter.__init__(self)
        OspSecurityGroup.__init__(self)
        OspSnapshot.__init__(self)
        OspSubnet.__init__(self)
        OspTenant.__init__(self)
        OspUser.__init__(self)
        OspVirtualMachine.__init__(self)
        OspVolume.__init__(self)
