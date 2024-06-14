import time
import traceback


class K8sPvApi():
    def __init__(self):
        self.pv_mo = None

    def get_pv_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.pv_mo is not None:
                return self.pv_mo

        api_handler = self.get_api()
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.list_persistent_volume(
                timeout_seconds=self.api_timeout_seconds
            )
            self.log.k8s(
                'get',
                'pv',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_pv', traceback.format_exc())
            self.log.k8s(
                'get',
                'pv',
                True,
                int(time.time() * 1000) - start_time
            )
            return None

        self.pv_mo = []
        for item in response.items:
            pv_mo = self.convert_object(item.to_dict())
            self.pv_mo.append(
                pv_mo
            )

        self.log.k8s_mo(
            'pv',
            self.pv_mo
        )

        return self.pv_mo
