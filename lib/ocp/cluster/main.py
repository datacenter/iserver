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
    def __init__(self):
        OcpClusterCnv.__init__(self)
        OcpClusterConsole.__init__(self)
        OcpClusterKubeconfig.__init__(self)
        OcpClusterManager.__init__(self)
        OcpClusterVcenter.__init__(self)
