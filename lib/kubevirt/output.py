from lib import output_helper

from lib.kubevirt.virtual_machine.output import KubevirtVirtualMachineOutput
from lib.kubevirt.virtual_machine_instance.output import KubevirtVirtualMachineInstanceOutput


class KubevirtOutput(
    KubevirtVirtualMachineOutput,
    KubevirtVirtualMachineInstanceOutput
    ):
    def __init__(self, verbose=False, debug=False, log_id=None):
        self.my_output = output_helper.OutputHelper(
            log_id=log_id,
            verbose=verbose,
            debug=debug
        )

        KubevirtVirtualMachineOutput.__init__(self)
        KubevirtVirtualMachineInstanceOutput.__init__(self)
