from lib.k8s.ceph_object_zone_group.api import K8sCephObjectZoneGroupApi
from lib.k8s.ceph_object_zone_group.info import K8sCephObjectZoneGroupInfo


class K8sCephObjectZoneGroup(
        K8sCephObjectZoneGroupApi,
        K8sCephObjectZoneGroupInfo
        ):
    def __init__(self):
        K8sCephObjectZoneGroupApi.__init__(self)
        K8sCephObjectZoneGroupInfo.__init__(self)
