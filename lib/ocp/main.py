from lib import log_helper
from lib import output_helper

from lib.k8s import main as k8s
from lib.kubevirt import main as kubevirt

from lib.ocp import settings

from lib.ocp.cluster.main import OcpCluster
from lib.ocp.node.main import OcpNode
from lib.ocp.task.main import OcpTask
from lib.ocp.vm.main import OcpVm


class Ocp(OcpCluster, OcpNode, OcpTask, OcpVm):
    def __init__(self, ocp_cluster_name, verbose=False, debug=False, log_id=None):
        self.verbose = verbose
        self.debug = debug
        self.log_id = log_id

        self.my_output = output_helper.OutputHelper(
            log_id=log_id,
            verbose=verbose,
            debug=debug
        )
        self.log = log_helper.Log(log_id=log_id)
        self.log_id = log_id

        self.settings_handler = settings.OcpSettings(log_id=log_id)
        self.ocp_cluster_settings = self.settings_handler.get_ocp_cluster(ocp_cluster_name)
        if self.ocp_cluster_settings is None:
            raise ValueError('OCP cluster handler initialization failed')

        self.k8s_handler = k8s.K8s(
            self.ocp_cluster_settings['kubeconfig'],
            cluster_type='ocp',
            verbose=verbose,
            debug=debug,
            log_id=log_id
        )

        self.kubevirt_handler = kubevirt.Kubevirt(
            self.ocp_cluster_settings['kubeconfig'],
            verbose=verbose,
            debug=debug,
            log_id=log_id
        )

        OcpCluster.__init__(self)
        OcpNode.__init__(self)
        OcpTask.__init__(self)
        OcpVm.__init__(self)
