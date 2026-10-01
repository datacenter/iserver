from lib.k8s.certificate.api import K8sCertificateApi
from lib.k8s.certificate.info import K8sCertificateInfo
from lib.k8s.certificate.create import K8sCertificateCreate
from lib.k8s.certificate.delete import K8sCertificateDelete
from lib.k8s.certificate.wait import K8sCertificateWait


class K8sCertificate(
        K8sCertificateApi,
        K8sCertificateInfo,
        K8sCertificateCreate,
        K8sCertificateDelete,
        K8sCertificateWait
        ):
    def __init__(self):
        K8sCertificateApi.__init__(self)
        K8sCertificateInfo.__init__(self)
        K8sCertificateCreate.__init__(self)
        K8sCertificateDelete.__init__(self)
        K8sCertificateWait.__init__(self)
