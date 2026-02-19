from lib.k8s.oauth.api import K8sOAuthApi
from lib.k8s.oauth.info import K8sOAuthInfo


class K8sOAuth(
        K8sOAuthApi,
        K8sOAuthInfo
        ):
    def __init__(self):
        K8sOAuthApi.__init__(self)
        K8sOAuthInfo.__init__(self)
