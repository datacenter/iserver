from lib.k8s.certificate.api import K8sCertificateApi
from lib.k8s.certificate.info import K8sCertificateInfo


class K8sCertificate(
        K8sCertificateApi,
        K8sCertificateInfo
        ):
    def __init__(self):
        K8sCertificateApi.__init__(self)
        K8sCertificateInfo.__init__(self)
