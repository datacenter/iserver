from lib.k8s.ceph_client_profile_mapping.api import K8sCephClientProfileMappingApi
from lib.k8s.ceph_client_profile_mapping.info import K8sCephClientProfileMappingInfo


class K8sCephClientProfileMapping(
        K8sCephClientProfileMappingApi,
        K8sCephClientProfileMappingInfo
        ):
    def __init__(self):
        K8sCephClientProfileMappingApi.__init__(self)
        K8sCephClientProfileMappingInfo.__init__(self)
