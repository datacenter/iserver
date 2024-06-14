import time
import traceback


class OspAvailabilityZoneApi():
    def __init__(self):
        self.availability_zone_mo = None

    def get_availability_zone_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.availability_zone_mo is not None:
                return self.availability_zone_mo

        api_handler = self.get_api_nova(cache_enabled=cache_enabled)
        if api_handler is None:
            self.log.error(
                'get_availability_zone_mo',
                'No api handler'
            )
            return None

        try:
            start_time = int(time.time() * 1000)
            self.availability_zone_mo = api_handler.availability_zones.list()
            self.log.osp(
                'get',
                'availability_zones',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('osp.get_availability_zone_mo', traceback.format_exc())
            self.log.osp(
                'get',
                'availability_zones',
                True,
                int(time.time() * 1000) - start_time
            )
            return None

        return self.availability_zone_mo
