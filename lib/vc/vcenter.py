from lib.vc.common import VcCommon
from lib.vc.connect import VcConnect
from lib.vc.datacenter import VcDatacenter
from lib.vc.datastore import VcDatastore
from lib.vc.helper import VcHelper
from lib.vc.host.main import VcHost
from lib.vc.network import VcNetwork
from lib.vc.virtual_machine import VcVirtualMachine
from lib.vc.virtual_machine_deployment_lcm import VcVirtualMachineDeploymentLcm
from lib.vc.virtual_machine_lcm import VcVirtualMachineLcm
from lib.vc.vm_cluster import VcVmCluster
from lib.vc.vm_folder import VcVmFolder

from lib import log_helper
from lib import output_helper


class Vcenter(
        VcCommon,
        VcConnect,
        VcDatacenter,
        VcDatastore,
        VcHost,
        VcHelper,
        VcNetwork,
        VcVirtualMachine,
        VcVirtualMachineDeploymentLcm,
        VcVirtualMachineLcm,
        VcVmCluster,
        VcVmFolder
        ):
    def __init__(self, vcenter_ip, vcenter_username, vcenter_password, port=443, disable_ssl_verification=True, verbose=False, debug=False, log_id=None):
        VcCommon.__init__(self)
        VcHelper.__init__(self)
        VcConnect.__init__(
            self,
            vcenter_ip,
            port,
            vcenter_username,
            vcenter_password,
            disable_ssl_verification=disable_ssl_verification
        )
        VcDatacenter.__init__(self)
        VcDatastore.__init__(self)
        VcHost.__init__(self)
        VcNetwork.__init__(self)
        VcVirtualMachine.__init__(self)
        VcVirtualMachineLcm.__init__(self)
        VcVirtualMachineDeploymentLcm.__init__(self, log_id=log_id, verbose=verbose, debug=debug)
        VcVmCluster.__init__(self)
        VcVmFolder.__init__(self)

        self.my_output = output_helper.OutputHelper(
            log_id=log_id,
            verbose=verbose,
            debug=debug
        )
        self.log = log_helper.Log(log_id=log_id)

        self.vc_connect()
