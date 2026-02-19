from lib.k8s.upload_token_request.api import K8sUploadTokenRequestApi
from lib.k8s.upload_token_request.info import K8sUploadTokenRequestInfo


class K8sUploadTokenRequest(
        K8sUploadTokenRequestApi,
        K8sUploadTokenRequestInfo
        ):
    def __init__(self):
        K8sUploadTokenRequestApi.__init__(self)
        K8sUploadTokenRequestInfo.__init__(self)
