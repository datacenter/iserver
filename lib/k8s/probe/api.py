import time
import traceback


class K8sProbeApi():
    def __init__(self):
        self.probe_mo = None

    def get_probe_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.probe_mo is not None:
                return self.probe_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='monitoring.coreos.com/v1',
                kind='Probe'
            )
            self.probe_mo = response.get().to_dict()['items']
            self.log.k8s(
                'get',
                'probe',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_probe_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'probe',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return None

        self.log.k8s_mo(
            'probe',
            self.probe_mo
        )

        return self.probe_mo
