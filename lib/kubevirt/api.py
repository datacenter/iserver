import os
import time
import traceback

from kubernetes import config
import kubevirt


class KubevirtApi():
    def __init__(self, kubeconfig_filename):
        self.kubeconfig_filename = kubeconfig_filename
        self.api = None

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

            kubevirt_configuration = kubevirt.configuration
            kubevirt_configuration.verify_ssl = False
            config_loader.load_and_set(
                kubevirt_configuration
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
