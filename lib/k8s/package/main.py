from lib.k8s.package.api import K8sPackageApi
from lib.k8s.package.info import K8sPackageInfo
from lib.k8s.package.cnv import K8sPackageCnv
from lib.k8s.package.gpu import K8sPackageGpu
from lib.k8s.package.mtv import K8sPackageMtv
from lib.k8s.package.nfd import K8sPackageNfd
from lib.k8s.package.ods import K8sPackageOds
from lib.k8s.package.nmstate import K8sPackageNmstate
from lib.k8s.package.portworx import K8sPackagePortworx
from lib.k8s.package.tetragon import K8sPackageTetragon


class K8sPackage(
        K8sPackageApi,
        K8sPackageInfo,
        K8sPackageCnv,
        K8sPackageGpu,
        K8sPackageMtv,
        K8sPackageNfd,
        K8sPackageOds,
        K8sPackageNmstate,
        K8sPackagePortworx,
        K8sPackageTetragon
        ):
    def __init__(self):
        K8sPackageApi.__init__(self)
        K8sPackageInfo.__init__(self)
        K8sPackageCnv.__init__(self)
        K8sPackageGpu.__init__(self)
        K8sPackageMtv.__init__(self)
        K8sPackageNfd.__init__(self)
        K8sPackageOds.__init__(self)
        K8sPackageNmstate.__init__(self)
        K8sPackagePortworx.__init__(self)
        K8sPackageTetragon.__init__(self)
