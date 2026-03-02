from lib.ocp.cluster.console.main import OcpClusterConsole
from lib.ocp.cluster.kubeconfig.main import OcpClusterKubeconfig
from lib.ocp.cluster.vcenter.main import OcpClusterVcenter


class OcpCluster(
    OcpClusterConsole,
    OcpClusterKubeconfig,
    OcpClusterVcenter
    ):
    def __init__(self, log_id=None):
        OcpClusterConsole.__init__(self, log_id=log_id)
        OcpClusterKubeconfig.__init__(self, log_id=log_id)
        OcpClusterVcenter.__init__(self)
