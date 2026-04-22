from lib.k8s.subscription.api import K8sSubscriptionApi
from lib.k8s.subscription.info import K8sSubscriptionInfo
from lib.k8s.subscription.match import K8sSubscriptionMatch
from lib.k8s.subscription.create import K8sSubscriptionCreate
from lib.k8s.subscription.delete import K8sSubscriptionDelete
from lib.k8s.subscription.wait import K8sSubscriptionWait
from lib.k8s.subscription.cnv import K8sSubscriptionCnv
from lib.k8s.subscription.gpu import K8sSubscriptionGpu
from lib.k8s.subscription.grafana import K8sSubscriptionGrafana
from lib.k8s.subscription.intersight import K8sSubscriptionIntersight
from lib.k8s.subscription.lso import K8sSubscriptionLocalStorage
from lib.k8s.subscription.lvm import K8sSubscriptionLvm
from lib.k8s.subscription.metallb import K8sSubscriptionMetallb
from lib.k8s.subscription.minio import K8sSubscriptionMinio
from lib.k8s.subscription.mtv import K8sSubscriptionMtv
from lib.k8s.subscription.nfd import K8sSubscriptionNfd
from lib.k8s.subscription.nim import K8sSubscriptionNim
from lib.k8s.subscription.nmstate import K8sSubscriptionNmstate
from lib.k8s.subscription.ocs import K8sSubscriptionOcs
from lib.k8s.subscription.odf import K8sSubscriptionOdf
from lib.k8s.subscription.ods import K8sSubscriptionOds
from lib.k8s.subscription.portworx import K8sSubscriptionPortworx
from lib.k8s.subscription.serverless import K8sSubscriptionServerless
from lib.k8s.subscription.service_mesh import K8sSubscriptionServiceMesh
from lib.k8s.subscription.splunk import K8sSubscriptionSplunk
from lib.k8s.subscription.sriov import K8sSubscriptionSriov
from lib.k8s.subscription.tetragon import K8sSubscriptionTetragon
from lib.k8s.subscription.trident import K8sSubscriptionTrident
from lib.k8s.subscription.vast import K8sSubscriptionVast
from lib.k8s.subscription.web_terminal import K8sSubscriptionWebTerminal


class K8sSubscription(
        K8sSubscriptionApi,
        K8sSubscriptionInfo,
        K8sSubscriptionMatch,
        K8sSubscriptionCreate,
        K8sSubscriptionDelete,
        K8sSubscriptionWait,
        K8sSubscriptionCnv,
        K8sSubscriptionGpu,
        K8sSubscriptionGrafana,
        K8sSubscriptionIntersight,
        K8sSubscriptionLocalStorage,
        K8sSubscriptionLvm,
        K8sSubscriptionMetallb,
        K8sSubscriptionMinio,
        K8sSubscriptionMtv,
        K8sSubscriptionNfd,
        K8sSubscriptionNim,
        K8sSubscriptionNmstate,
        K8sSubscriptionOcs,
        K8sSubscriptionOdf,
        K8sSubscriptionOds,
        K8sSubscriptionPortworx,
        K8sSubscriptionServerless,
        K8sSubscriptionServiceMesh,
        K8sSubscriptionSplunk,
        K8sSubscriptionSriov,
        K8sSubscriptionTetragon,
        K8sSubscriptionTrident,
        K8sSubscriptionVast,
        K8sSubscriptionWebTerminal
        ):
    def __init__(self):
        K8sSubscriptionApi.__init__(self)
        K8sSubscriptionInfo.__init__(self)
        K8sSubscriptionMatch.__init__(self)
        K8sSubscriptionCreate.__init__(self)
        K8sSubscriptionDelete.__init__(self)
        K8sSubscriptionWait.__init__(self)
        K8sSubscriptionCnv.__init__(self)
        K8sSubscriptionGpu.__init__(self)
        K8sSubscriptionGrafana.__init__(self)
        K8sSubscriptionIntersight.__init__(self)
        K8sSubscriptionLocalStorage.__init__(self)
        K8sSubscriptionLvm.__init__(self)
        K8sSubscriptionMetallb.__init__(self)
        K8sSubscriptionMinio.__init__(self)
        K8sSubscriptionMtv.__init__(self)
        K8sSubscriptionNfd.__init__(self)
        K8sSubscriptionNim.__init__(self)
        K8sSubscriptionNmstate.__init__(self)
        K8sSubscriptionOcs.__init__(self)
        K8sSubscriptionOdf.__init__(self)
        K8sSubscriptionOds.__init__(self)
        K8sSubscriptionPortworx.__init__(self)
        K8sSubscriptionServerless.__init__(self)
        K8sSubscriptionServiceMesh.__init__(self)
        K8sSubscriptionSplunk.__init__(self)
        K8sSubscriptionSriov.__init__(self)
        K8sSubscriptionTetragon.__init__(self)
        K8sSubscriptionTrident.__init__(self)
        K8sSubscriptionVast.__init__(self)
        K8sSubscriptionWebTerminal.__init__(self)
