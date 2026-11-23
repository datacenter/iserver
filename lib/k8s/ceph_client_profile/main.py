from lib.k8s.ceph_client_profile.api import K8sCephClientProfileApi
from lib.k8s.ceph_client_profile.info import K8sCephClientProfileInfo


class K8sCephClientProfile(
        K8sCephClientProfileApi,
        K8sCephClientProfileInfo
        ):
    def __init__(self):
        K8sCephClientProfileApi.__init__(self)
        K8sCephClientProfileInfo.__init__(self)
