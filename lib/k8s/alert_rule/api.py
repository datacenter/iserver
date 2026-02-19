import time
import traceback


class K8sAlertRuleApi():
    def __init__(self):
        self.alert_rule_mo = None

    def get_alert_rule_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.alert_rule_mo is not None:
                return self.alert_rule_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='cilium.io/v1alpha1',
                kind='AlertRule'
            )
            self.alert_rule_mo = response.get().to_dict()['items']
            self.log.k8s(
                'get',
                'alert_rule',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_alert_rule_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'alert_rule',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return None

        self.log.k8s_mo(
            'alert_rule',
            self.alert_rule_mo
        )

        return self.alert_rule_mo

    def create_alert_rule_mo(self, alert_rule):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='cilium.io/v1alpha1', kind='AlertRule')
            success = True
            response = obj_list.create(
                body=alert_rule,
                name=alert_rule['metadata']['name']
            )
        except BaseException:
            success = False
            self.log.error('ocp.create_alert_rule', traceback.format_exc())

        self.log.ocp(
            'create',
            'alert_rule',
            success,
            int(time.time() * 1000) - start_time
        )

        return success

    def replace_alert_rule_mo(self, alert_rule):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='cilium.io/v1alpha1', kind='AlertRule')
            success = True
            response = obj_list.replace(
                body=alert_rule,
                name=alert_rule['metadata']['name'],
            )
        except BaseException:
            success = False
            self.log.error('ocp.replace_alert_rule', traceback.format_exc())

        self.log.ocp(
            'replace',
            'alert_rule',
            success,
            int(time.time() * 1000) - start_time
        )

        return success

    def delete_alert_rule(self, alert_rule_name):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='cilium.io/v1alpha1', kind='AlertRule')
            success = True
            response = obj_list.delete(
                alert_rule_name
            )
        except BaseException:
            success = False
            self.log.error('ocp.create_alert_rule', traceback.format_exc())

        self.log.ocp(
            'create',
            'alert_rule',
            success,
            int(time.time() * 1000) - start_time
        )

        return success
