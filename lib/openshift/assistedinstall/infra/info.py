import json

from lib import filter_helper


class AssistedInstallInfraInfo():
    def __init__(self):
        self.assisted_install_infra = None

    def get_assisted_install_infra_info(self, managed_object):
        info = {}
        info['__Output'] = {}
        for key in managed_object:
            info[key] = managed_object[key]

        for key in ['download_url', 'type']:
            if key not in info:
                info[key] = None

        if 'static_network_config' in info:
            info['static_network_config'] = json.loads(info['static_network_config'])

        return info

    def get_assisted_install_infras_info(self, cache_enabled=True):
        if cache_enabled and self.assisted_install_infra is not None:
            return self.assisted_install_infra

        managed_objects = self.get_assisted_install_infra_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.assisted_install_infra = []
        for managed_object in managed_objects:
            self.assisted_install_infra.append(
                self.get_assisted_install_infra_info(
                    managed_object
                )
            )

        self.log.openshift_mo(
            'assisted_install_infra.info',
            self.assisted_install_infra
        )

        return self.assisted_install_infra

    def match_assisted_install_infra(self, assisted_install_infra_info, assisted_install_infra_filter):
        if assisted_install_infra_filter is None or len(assisted_install_infra_filter) == 0:
            return True

        for ap_rule in assisted_install_infra_filter:
            (key, value) = ap_rule.split(':')

            key_found = False

            if key == 'cluster_id':
                key_found = True
                if not filter_helper.match_string(value, assisted_install_infra_info['cluster_id']):
                    return False

            if not key_found:
                self.log.error(
                    'match_assisted_install_infra',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_assisted_install_infras(self, assisted_install_infra_filter=None, cache_enabled=True):
        all_infras = self.get_assisted_install_infras_info(cache_enabled=cache_enabled)
        if all_infras is None:
            return None

        infras = []

        for infra_info in all_infras:
            if not self.match_assisted_install_infra(infra_info, assisted_install_infra_filter):
                continue

            infras.append(infra_info)

        return infras
