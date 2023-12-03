from lib import filter_helper


class K8sDeploymentConfigInfo():
    def __init__(self):
        self.deployment_config = None

    def get_deployment_config_info(self, deployment_config_mo):
        if deployment_config_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            deployment_config_mo
        )
        info.update(metadata_info)

        return info

    def get_deployment_configs_info(self, cache_enabled=True):
        if cache_enabled:
            if self.deployment_config is not None:
                return self.deployment_config

        managed_objects = self.get_deployment_config_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.deployment_config = []
        for managed_object in managed_objects:
            deployment_config_info = {}
            deployment_config_info['info'] = self.get_deployment_config_info(
                managed_object
            )
            deployment_config_info['mo'] = managed_object
            self.deployment_config.append(
                deployment_config_info
            )

        return self.deployment_config

    def match_deployment_config(self, deployment_config_info, deployment_config_filter):
        if deployment_config_filter is None or len(deployment_config_filter) == 0:
            return True

        for ap_rule in deployment_config_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if not key_found:
                self.log.error(
                    'match_deployment_config',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_deployment_configs(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_deployment_configs = self.get_deployment_configs_info(cache_enabled=cache_enabled)
        if all_deployment_configs is None:
            return None

        deployment_configs = []

        for deployment_config_info in all_deployment_configs:
            if not self.match_deployment_config(deployment_config_info['info'], object_filter):
                continue

            if return_mo:
                deployment_configs.append(
                    deployment_config_info['mo']
                )
                continue

            deployment_configs.append(
                deployment_config_info['info']
            )

        return deployment_configs
