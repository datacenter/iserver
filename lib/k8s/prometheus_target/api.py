import json
import traceback
from lib import filter_helper


class K8sPrometheusTargetApi():
    def __init__(self):
        self.prometheus_target_platform_mo = None
        self.prometheus_target_user_mo = None

    def get_prometheus_target_platform_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.prometheus_target_platform_mo is not None:
                return self.prometheus_target_platform_mo

        output = self.get_openshift_prometheus_platform_exec(
            'curl --no-progress-meter -k http://localhost:9090/api/v1/targets'
        )
        if output is None:
            return None
    
        try:
            self.prometheus_target_platform_mo = json.loads(
                filter_helper.json_fixup(
                    output
                )
            )[0]['data']['activeTargets']
        except BaseException:
            print(traceback.format_exc())
            return None
    
        self.log.k8s_mo(
            'prometheus_target_platform',
            self.prometheus_target_platform_mo
        )

        return self.prometheus_target_platform_mo

    def get_prometheus_target_user_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.prometheus_target_user_mo is not None:
                return self.prometheus_target_user_mo

        output = self.get_openshift_prometheus_user_exec(
            'curl --no-progress-meter -k http://localhost:9090/api/v1/targets'
        )
        if output is None:
            return None
    
        try:
            self.prometheus_target_user_mo = json.loads(
                filter_helper.json_fixup(
                    output
                )
            )[0]['data']['activeTargets']
        except BaseException:
            return None
    
        self.log.k8s_mo(
            'prometheus_target_user',
            self.prometheus_target_user_mo
        )

        return self.prometheus_target_user_mo
    