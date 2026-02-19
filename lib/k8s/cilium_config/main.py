from lib.k8s.cilium_config.api import K8sCiliumConfigApi
from lib.k8s.cilium_config.info import K8sCiliumConfigInfo
from lib.k8s.cilium_config.bgp import K8sCiliumConfigBgp
from lib.k8s.cilium_config.mesh import K8sCiliumConfigMesh
from lib.k8s.cilium_config.pnet import K8sCiliumConfigPrivateNetwork
from lib.k8s.cilium_config.status import K8sCiliumConfigStatus
from lib.k8s.cilium_config.timescape import K8sCiliumConfigTimescape
from lib.k8s.cilium_config.update import K8sCiliumConfigUpdate


class K8sCiliumConfig(
        K8sCiliumConfigApi,
        K8sCiliumConfigInfo,
        K8sCiliumConfigBgp,
        K8sCiliumConfigMesh,
        K8sCiliumConfigPrivateNetwork,
        K8sCiliumConfigStatus,
        K8sCiliumConfigTimescape,
        K8sCiliumConfigUpdate
        ):
    def __init__(self):
        K8sCiliumConfigApi.__init__(self)
        K8sCiliumConfigInfo.__init__(self)
        K8sCiliumConfigBgp.__init__(self)
        K8sCiliumConfigMesh.__init__(self)
        K8sCiliumConfigPrivateNetwork.__init__(self)
        K8sCiliumConfigStatus.__init__(self)
        K8sCiliumConfigTimescape.__init__(self)
        K8sCiliumConfigUpdate.__init__(self)

        if self.cluster_type == 'standard':
            self.cilium_namespace = 'kube-system'
        else:
            self.cilium_namespace = 'cilium'
            
        self.cilium_operator = 'cilium-operator'
        self.cilium_agent = 'cilium'