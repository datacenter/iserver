from lib import filter_helper
from lib import ip_helper


class MonApiInfo():
    def __init__(self):
        self.api = None

    def get_api_info(self, api_mo):
        if api_mo is None:
            return None

        info = {}
        info['__Output'] = {}
        info['nexus_name'] = self.nexus_name

        for key in api_mo:
            info[key] = api_mo[key]

        info['mac'] = info['remote_intf_mac']

        return info

    def get_apis_info(self, local_cache_enabled=True, cache_enabled=True):
        if local_cache_enabled:
            if self.api is not None:
                return self.api

        managed_objects = self.get_api_mo(
            local_cache_enabled=local_cache_enabled,
            cache_enabled=cache_enabled
        )
        if managed_objects is None:
            self.log.error(
                'get_apis_info',
                'No api neighbor managed objects: %s' % (self.nexus_name)
            )
            return None

        self.api = []
        for managed_object in managed_objects['TABLE_api_neighbor_detail_info']['ROW_api_neighbor_detail_info']:
            api_info = self.get_api_info(
                managed_object
            )
            self.api.append(
                api_info
            )

        return self.api

    def match_api(self, api_info, api_filter):
        if api_filter is None or len(api_filter) == 0:
            return True

        for ap_rule in api_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if key == 'mac':
                key_found = True

                if api_info['mac'] is None:
                    return False

                found = False
                for mac_address in value.split(','):
                    if ip_helper.is_mac_match(mac_address, api_info['mac']):
                        found = True
                        break

                if not found:
                    return False

            if not key_found:
                self.log.error(
                    'match_api',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_apis(self, object_filter=None, local_cache_enabled=True, cache_enabled=True):
        all_apis = self.get_apis_info(
            local_cache_enabled=local_cache_enabled,
            cache_enabled=cache_enabled
        )
        if all_apis is None:
            self.log.error(
                'get_apis',
                'Failed to get api neighbors: %s' % (self.nexus_name)
            )
            return None

        apis = []

        for api_info in all_apis:
            if not self.match_api(api_info, object_filter):
                continue

            apis.append(
                api_info
            )

        return apis
