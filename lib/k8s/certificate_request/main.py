from lib.k8s.certificate_request.api import K8sCertificateRequestApi
from lib.k8s.certificate_request.info import K8sCertificateRequestInfo


class K8sCertificateRequest(
        K8sCertificateRequestApi,
        K8sCertificateRequestInfo
        ):
    def __init__(self):
        K8sCertificateRequestApi.__init__(self)
        K8sCertificateRequestInfo.__init__(self)