import time
import traceback


class K8sEgressIpApi():
    def __init__(self):
        self.egress_ip_mo = None

    def get_egress_ip_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.egress_ip_mo is not None:
                return self.egress_ip_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='k8s.ovn.org/v1',
                kind='EgressIP'
            )
            self.egress_ip_mo = response.get().to_dict()['items']
            self.log.k8s(
                'get',
                'egress_ip',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_egress_ip_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'egress_ip',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return None

        self.log.k8s_mo(
            'egress_ip',
            self.egress_ip_mo
        )

        return self.egress_ip_mo
