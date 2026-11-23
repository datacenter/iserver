from lib.osp.availability_zone.api import OspAvailabilityZoneApi
from lib.osp.availability_zone.info import OspAvailabilityZoneInfo


class OspAvailabilityZone(
        OspAvailabilityZoneApi,
        OspAvailabilityZoneInfo
        ):
    def __init__(self):
        OspAvailabilityZoneApi.__init__(self)
        OspAvailabilityZoneInfo.__init__(self)
