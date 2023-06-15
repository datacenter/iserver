import time
import traceback


class K8sPvApi():
    def __init__(self):
        self.pvs = None

    def is_pv(self, name, cache=True):
        if self.get_pv(name, cache=cache) is None:
            return False
        return True

    def get_pv(self, name, cache=True):
        pvs = self.get_pvs(cache=cache)
        if pvs is None:
            return None

        for pv in pvs:
            if pv['metadata']['name'] == name:
                return pv

        return None

    def get_pvs(self, cache=True):
        if not self.connect():
            return None

        if self.pvs is not None and cache:
            return self.pvs

        try:
            start_time = int(time.time() * 1000)
            response = self.api.list_persistent_volume(
                timeout_seconds=self.api_timeout_seconds
            )
            self.log.k8s(
                'get',
                'pvs',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_pvs', traceback.format_exc())
            self.log.k8s(
                'get',
                'pvs',
                True,
                int(time.time() * 1000) - start_time
            )
            return None

        self.pvs = []
        for item in response.items:
            pv = self.convert_object(item.to_dict())
            self.pvs.append(
                pv
            )

        self.log.k8s_mo(
            'pv',
            self.pvs
        )

        return self.pvs
