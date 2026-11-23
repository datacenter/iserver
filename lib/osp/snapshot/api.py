import time
import traceback


class OspSnapshotApi():
    def __init__(self):
        self.snapshot_mo = None

    def get_snapshot_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.snapshot_mo is not None:
                return self.snapshot_mo

        api_handler = self.get_api_cinder(cache_enabled=cache_enabled)
        if api_handler is None:
            self.log.error(
                'get_snapshot_mo',
                'No api handler'
            )
            return None

        try:
            start_time = int(time.time() * 1000)
            self.snapshot_mo = api_handler.volume_snapshots.list()
            self.log.osp(
                'get',
                'snapshots',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('osp.get_snapshot_mo', traceback.format_exc())
            self.log.osp(
                'get',
                'snapshots',
                True,
                int(time.time() * 1000) - start_time
            )
            return None

        return self.snapshot_mo
