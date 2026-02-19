from lib.ocp.cluster.cnv.main import OcpClusterCnv
from lib.ocp.cluster.console.main import OcpClusterConsole
from lib.ocp.cluster.kubeconfig.main import OcpClusterKubeconfig
from lib.ocp.cluster.manager.main import OcpClusterManager
from lib.ocp.cluster.vcenter.main import OcpClusterVcenter


class OcpCluster(
    OcpClusterCnv,
    OcpClusterConsole,
    OcpClusterKubeconfig,
    OcpClusterManager,
    OcpClusterVcenter
    ):
    def __init__(self, log_id=None):
        OcpClusterCnv.__init__(self)
        OcpClusterConsole.__init__(self, log_id=log_id)
        OcpClusterKubeconfig.__init__(self, log_id=log_id)
        OcpClusterManager.__init__(self)
        OcpClusterVcenter.__init__(self)
