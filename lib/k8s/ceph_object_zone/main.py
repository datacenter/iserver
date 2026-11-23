from lib.k8s.ceph_object_zone.api import K8sCephObjectZoneApi
from lib.k8s.ceph_object_zone.info import K8sCephObjectZoneInfo


class K8sCephObjectZone(
        K8sCephObjectZoneApi,
        K8sCephObjectZoneInfo
        ):
    def __init__(self):
        K8sCephObjectZoneApi.__init__(self)
        K8sCephObjectZoneInfo.__init__(self)
