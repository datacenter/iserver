import time
import traceback


class K8sSspApi():
    def __init__(self):
        self.ssp_mo = None

    def get_ssp_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.ssp_mo is not None:
                return self.ssp_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='ssp.kubevirt.io/v1beta3',
                kind='SSP'
            )
            self.ssp_mo = response.get().to_dict()['items']
            self.log.k8s(
                'get',
                'ssp',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_ssp_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'ssp',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return None

        self.log.k8s_mo(
            'ssp',
            self.ssp_mo
        )

        return self.ssp_mo
