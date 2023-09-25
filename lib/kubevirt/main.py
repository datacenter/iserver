from lib import log_helper

from lib.kubevirt.api import KubevirtApi
from lib.kubevirt.common import KubevirtCommon
from lib.kubevirt.virtual_machine.main import KubevirtVirtualMachine
from lib.kubevirt.virtual_machine_instance.main import KubevirtVirtualMachineInstance


class Kubevirt(
        KubevirtApi,
        KubevirtCommon,
        KubevirtVirtualMachine,
        KubevirtVirtualMachineInstance
        ):
    def __init__(self, kubeconfig_filename, verbose=False, debug=False, log_id=None):
        self.verbose = verbose
        self.debug = debug
        self.log_id = log_id
        self.log = log_helper.Log(log_id=log_id)

        KubevirtApi.__init__(self, kubeconfig_filename)
        KubevirtCommon.__init__(self)
        KubevirtVirtualMachine.__init__(self)
        KubevirtVirtualMachineInstance.__init__(self)
