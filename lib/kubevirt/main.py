import os
import time
import traceback

from kubernetes import config
import kubevirt

from lib import log_helper
from lib import output_helper

from lib.kubevirt.vm import KubevirtVm
from lib.kubevirt.vmi import KubevirtVmi


class Kubevirt(KubevirtVm, KubevirtVmi):
    def __init__(self, kubeconfig_filename, verbose=False, debug=False, log_id=None):
        self.verbose = verbose
        self.debug = debug
        self.log_id = log_id

        self.my_output = output_helper.OutputHelper(
            log_id=log_id,
            verbose=verbose,
            debug=debug
        )
        self.log = log_helper.Log(log_id=log_id)

        self.kubeconfig_filename = kubeconfig_filename

        self.api = None

        KubevirtVm.__init__(self)
        KubevirtVmi.__init__(self)

    def connect(self):
        # https://github.com/kubevirt/client-python
        if self.api is not None:
            return True

        if not os.path.isfile(self.kubeconfig_filename):
            self.log.error(
                'k8s.connect',
                'Kubeconfig file not found: %s' % (self.kubeconfig_filename)
            )
            return False

        try:
            start_time = int(time.time() * 1000)

            config_loader = config.kube_config._get_kube_config_loader_for_yaml_file(
                self.kubeconfig_filename
            )
            config_loader.load_and_set(
                kubevirt.configuration
            )

            api_client = kubevirt.ApiClient()
            self.api = kubevirt.DefaultApi(api_client=api_client)

            self.log.kubevirt(
                'connect',
                '-',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error(
                'kubevirt.connect',
                'Kubeconfig file failed: %s' % (self.kubeconfig_filename)
            )
            self.log.error('k8s.connect', traceback.format_exc())
            return False

        return True
