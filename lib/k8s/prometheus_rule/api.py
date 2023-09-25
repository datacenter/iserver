import time
import traceback


class K8sPrometheusRuleApi():
    def __init__(self):
        self.prometheus_rule_mo = None

    def get_prometheus_rule_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.prometheus_rule_mo is not None:
                return self.prometheus_rule_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='monitoring.coreos.com/v1',
                kind='PrometheusRule'
            )
            self.prometheus_rule_mo = response.get().to_dict()['items']
            self.log.k8s(
                'get',
                'prometheus_rule',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_prometheus_rule_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'prometheus_rule',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return None

        self.log.k8s_mo(
            'prometheus_rule',
            self.prometheus_rule_mo
        )

        return self.prometheus_rule_mo
