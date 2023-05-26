import os
import time
import traceback

from kubernetes import config
from kubernetes import client
from openshift.dynamic import DynamicClient

from lib.ocp.api.csv import OcpApiCsv
from lib.ocp.api.dv import OcpApiDv
from lib.ocp.api.operator_group import OcpApiOperatorGroup
from lib.ocp.api.sriov_network_node_policy import OcpApiSriovNetworkNodePolicy
from lib.ocp.api.sriov_network import OcpApiSriovNetwork
from lib.ocp.api.subscription import OcpApiSubscription


class OcpApi(
    OcpApiCsv,
    OcpApiDv,
    OcpApiOperatorGroup,
    OcpApiSriovNetworkNodePolicy,
    OcpApiSriovNetwork,
    OcpApiSubscription
    ):
    def __init__(self, kubeconfig_filename):
        self.kubeconfig_filename = kubeconfig_filename
        self.api = None

        OcpApiCsv.__init__(self)
        OcpApiDv.__init__(self)
        OcpApiOperatorGroup.__init__(self)
        OcpApiSriovNetworkNodePolicy.__init__(self)
        OcpApiSriovNetwork.__init__(self)
        OcpApiSubscription.__init__(self)

    def connect(self):
        # https://github.com/openshift/openshift-restclient-python
        if self.api is not None:
            return True

        if not os.path.isfile(self.kubeconfig_filename):
            self.log.error(
                'ocp.connect',
                'Kubeconfig file not found: %s' % (self.kubeconfig_filename)
            )
            return False

        try:
            start_time = int(time.time() * 1000)

            config.load_kube_config(self.kubeconfig_filename)
            k8s_client = client.ApiClient()
            self.api = DynamicClient(k8s_client)

            self.log.ocp(
                'connect',
                '-',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error(
                'ocp.connect',
                'Kubeconfig file failed: %s' % (self.kubeconfig_filename)
            )
            self.log.error('ocp.connect', traceback.format_exc())
            return False

        return True
