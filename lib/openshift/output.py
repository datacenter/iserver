from lib import output_helper

from lib.openshift.assistedinstall.output import AssistedInstallOutput


class OpenshiftOutput(
    AssistedInstallOutput
    ):
    def __init__(self, verbose=False, debug=False, log_id=None):
        self.my_output = output_helper.OutputHelper(
            log_id=log_id,
            verbose=verbose,
            debug=debug
        )
