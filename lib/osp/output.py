from lib import output_helper
from lib.osp.availability_zone.output import OspAvailabilityZoneOutput
from lib.osp.flavor.output import OspFlavorOutput
from lib.osp.floating_ip.output import OspFloatingIpOutput
from lib.osp.hypervisor.output import OspHypervisorOutput
from lib.osp.image.output import OspImageOutput
from lib.osp.network.output import OspNetworkOutput
from lib.osp.port.output import OspPortOutput
from lib.osp.quota.output import OspQuotaOutput
from lib.osp.role.output import OspRoleOutput
from lib.osp.router.output import OspRouterOutput
from lib.osp.security_group.output import OspSecurityGroupOutput
from lib.osp.snapshot.output import OspSnapshotOutput
from lib.osp.subnet.output import OspSubnetOutput
from lib.osp.tenant.output import OspTenantOutput
from lib.osp.user.output import OspUserOutput
from lib.osp.virtual_machine.output import OspVirtualMachineOutput
from lib.osp.volume.output import OspVolumeOutput


class OspOutput(
        OspAvailabilityZoneOutput,
        OspFlavorOutput,
        OspFloatingIpOutput,
        OspHypervisorOutput,
        OspImageOutput,
        OspNetworkOutput,
        OspPortOutput,
        OspQuotaOutput,
        OspRoleOutput,
        OspRouterOutput,
        OspSecurityGroupOutput,
        OspSnapshotOutput,
        OspSubnetOutput,
        OspTenantOutput,
        OspUserOutput,
        OspVirtualMachineOutput,
        OspVolumeOutput
        ):
    def __init__(self, verbose=False, debug=False, log_id=None):
        self.my_output = output_helper.OutputHelper(
            log_id=log_id,
            verbose=verbose,
            debug=debug
        )

        OspAvailabilityZoneOutput.__init__(self)
        OspFlavorOutput.__init__(self)
        OspFloatingIpOutput.__init__(self)
        OspHypervisorOutput.__init__(self)
        OspImageOutput.__init__(self)
        OspNetworkOutput.__init__(self)
        OspPortOutput.__init__(self)
        OspQuotaOutput.__init__(self)
        OspRoleOutput.__init__(self)
        OspRouterOutput.__init__(self)
        OspSecurityGroupOutput.__init__(self)
        OspSnapshotOutput.__init__(self)
        OspSubnetOutput.__init__(self)
        OspTenantOutput.__init__(self)
        OspUserOutput.__init__(self)
        OspVirtualMachineOutput.__init__(self)
        OspVolumeOutput.__init__(self)
