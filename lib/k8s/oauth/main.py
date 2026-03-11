from lib.k8s.oauth.api import K8sOAuthApi
from lib.k8s.oauth.info import K8sOAuthInfo
from lib.k8s.oauth.delete import K8sOAuthDelete
from lib.k8s.oauth.htpasswd import K8sOAuthHtpasswd
from lib.k8s.oauth.ldap import K8sOAuthLdap


class K8sOAuth(
        K8sOAuthApi,
        K8sOAuthInfo,
        K8sOAuthDelete,
        K8sOAuthHtpasswd,
        K8sOAuthLdap
        ):
    def __init__(self):
        K8sOAuthApi.__init__(self)
        K8sOAuthInfo.__init__(self)
        K8sOAuthDelete.__init__(self)
        K8sOAuthHtpasswd.__init__(self)
        K8sOAuthLdap.__init__(self)
