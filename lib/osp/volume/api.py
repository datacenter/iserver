import time
import traceback


class OspVolumeApi():
    def __init__(self):
        self.volume_mo = None

    def get_volume_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.volume_mo is not None:
                return self.volume_mo

        api_handler = self.get_api_cinder(cache_enabled=cache_enabled)
        if api_handler is None:
            self.log.error(
                'get_volume_mo',
                'No api handler'
            )
            return None

        try:
            start_time = int(time.time() * 1000)
            self.volume_mo = api_handler.volumes.list()
            self.log.osp(
                'get',
                'volumes.list',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('osp.get_volume_mo', traceback.format_exc())
            self.log.osp(
                'get',
                'volumes.list',
                True,
                int(time.time() * 1000) - start_time
            )
            return None

        return self.volume_mo
