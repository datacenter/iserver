from lib.k8s.profile.api import K8sProfileApi
from lib.k8s.profile.info import K8sProfileInfo


class K8sProfile(
        K8sProfileApi,
        K8sProfileInfo
        ):
    def __init__(self):
        K8sProfileApi.__init__(self)
        K8sProfileInfo.__init__(self)
