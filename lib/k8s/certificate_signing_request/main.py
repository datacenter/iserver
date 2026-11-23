from lib.k8s.certificate_signing_request.api import K8sCsrApi
from lib.k8s.certificate_signing_request.info import K8sCsrInfo
from lib.k8s.certificate_signing_request.wait import K8sCsrWait


class K8sCsr(
        K8sCsrApi,
        K8sCsrInfo,
        K8sCsrWait
        ):
    def __init__(self):
        K8sCsrApi.__init__(self)
        K8sCsrInfo.__init__(self)
        K8sCsrWait.__init__(self)
