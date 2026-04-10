from lib.k8s.pod.api import K8sPodApi
from lib.k8s.pod.info import K8sPodInfo
from lib.k8s.pod.cilium_agent import K8sPodCiliumAgent
from lib.k8s.pod.cilium_operator import K8sPodCiliumOperator
from lib.k8s.pod.cilium_private_network import K8sPodCiliumPrivateNetwork
from lib.k8s.pod.cilium_timescape import K8sPodCiliumTimescape
from lib.k8s.pod.create import K8sPodCreate
from lib.k8s.pod.delete import K8sPodDelete
from lib.k8s.pod.metallb import K8sPodMetallb
from lib.k8s.pod.nvidia_driver import K8sPodNvidiaDriver
from lib.k8s.pod.oauth import K8sPodOauth
from lib.k8s.pod.openshift_prometheus import K8sPodOpenshiftPrometheus
from lib.k8s.pod.ovn_frr import K8sPodOvnFrr
from lib.k8s.pod.template.main import K8sPodTemplate
from lib.k8s.pod.wait import K8sPodWait


class K8sPod(
        K8sPodApi,
        K8sPodInfo,
        K8sPodCiliumAgent,
        K8sPodCiliumOperator,
        K8sPodCiliumPrivateNetwork,
        K8sPodCiliumTimescape,
        K8sPodCreate,
        K8sPodDelete,
        K8sPodMetallb,
        K8sPodNvidiaDriver,
        K8sPodOauth,
        K8sPodOpenshiftPrometheus,
        K8sPodOvnFrr,
        K8sPodTemplate,
        K8sPodWait
        ):
    def __init__(self):
        K8sPodApi.__init__(self)
        K8sPodInfo.__init__(self)
        K8sPodCiliumAgent.__init__(self)
        K8sPodCiliumOperator.__init__(self)
        K8sPodCiliumPrivateNetwork.__init__(self)
        K8sPodCiliumTimescape.__init__(self)
        K8sPodCreate.__init__(self)
        K8sPodDelete.__init__(self)
        K8sPodMetallb.__init__(self)
        K8sPodNvidiaDriver.__init__(self)
        K8sPodOauth.__init__(self)
        K8sPodOpenshiftPrometheus.__init__(self)
        K8sPodOvnFrr.__init__(self)
        K8sPodTemplate.__init__(self)
        K8sPodWait.__init__(self)
