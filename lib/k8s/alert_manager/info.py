from lib import filter_helper


class K8sAlertManagerInfo():
    def __init__(self):
        self.alert_manager = None

    def get_alert_manager_info(self, alert_manager_mo):
        if alert_manager_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            alert_manager_mo
        )
        info.update(metadata_info)

        info['version'] = self.get(
            alert_manager_mo,
            'metadata:labels:app.kubernetes.io/version'
        )

        info['replicas'] = self.get(
            alert_manager_mo,
            'spec:replicas'
        )

        return info

    def get_alert_managers_info(self, cache_enabled=True):
        if cache_enabled:
            if self.alert_manager is not None:
                return self.alert_manager

        managed_objects = self.get_alert_manager_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.alert_manager = []
        for managed_object in managed_objects:
            alert_manager_info = {}
            alert_manager_info['info'] = self.get_alert_manager_info(
                managed_object
            )
            alert_manager_info['mo'] = managed_object
            self.alert_manager.append(
                alert_manager_info
            )

        return self.alert_manager

    def match_alert_manager(self, alert_manager_info, alert_manager_filter):
        if alert_manager_filter is None or len(alert_manager_filter) == 0:
            return True

        for ap_rule in alert_manager_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if not key_found:
                self.log.error(
                    'match_alert_manager',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_alert_managers(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_alert_managers = self.get_alert_managers_info(cache_enabled=cache_enabled)
        if all_alert_managers is None:
            return None

        alert_managers = []

        for alert_manager_info in all_alert_managers:
            if not self.match_alert_manager(alert_manager_info['info'], object_filter):
                continue

            if return_mo:
                alert_managers.append(
                    alert_manager_info['mo']
                )
                continue

            alert_managers.append(
                alert_manager_info['info']
            )

        return alert_managers
