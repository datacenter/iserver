from lib import filter_helper


class K8sAlertManagerConfigInfo():
    def __init__(self):
        self.alert_manager_config = None

    def get_alert_manager_config_info(self, alert_manager_config_mo):
        if alert_manager_config_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            alert_manager_config_mo
        )
        info.update(metadata_info)

        return info

    def get_alert_manager_configs_info(self, cache_enabled=True):
        if cache_enabled:
            if self.alert_manager_config is not None:
                return self.alert_manager_config

        managed_objects = self.get_alert_manager_config_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.alert_manager_config = []
        for managed_object in managed_objects:
            alert_manager_config_info = {}
            alert_manager_config_info['info'] = self.get_alert_manager_config_info(
                managed_object
            )
            alert_manager_config_info['mo'] = managed_object
            self.alert_manager_config.append(
                alert_manager_config_info
            )

        return self.alert_manager_config

    def match_alert_manager_config(self, alert_manager_config_info, alert_manager_config_filter):
        if alert_manager_config_filter is None or len(alert_manager_config_filter) == 0:
            return True

        for ap_rule in alert_manager_config_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if not key_found:
                self.log.error(
                    'match_alert_manager_config',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_alert_manager_configs(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_alert_manager_configs = self.get_alert_manager_configs_info(cache_enabled=cache_enabled)
        if all_alert_manager_configs is None:
            return None

        alert_manager_configs = []

        for alert_manager_config_info in all_alert_manager_configs:
            if not self.match_alert_manager_config(alert_manager_config_info['info'], object_filter):
                continue

            if return_mo:
                alert_manager_configs.append(
                    alert_manager_config_info['mo']
                )
                continue

            alert_manager_configs.append(
                alert_manager_config_info['info']
            )

        return alert_manager_configs
