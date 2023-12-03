from lib import filter_helper


class NsoCnfmReleaseInfo():
    def __init__(self):
        self.cnfm_release = {}

    def get_cnfm_release_info(self, cnfm_release_mo):
        if cnfm_release_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        info['cluster'] = self.get(
            cnfm_release_mo,
            'cluster'
        )

        info['namespace'] = self.get(
            cnfm_release_mo,
            'namespace'
        )

        info['name'] = self.get(
            cnfm_release_mo,
            'name'
        )

        info['chart'] = self.get(
            cnfm_release_mo,
            'chart-name'
        )

        info['version'] = self.get(
            cnfm_release_mo,
            'chart-version'
        )

        info['values'] = self.get(
            cnfm_release_mo,
            'values:key-value'
        )

        return info

    def get_cnfm_releases_info(self, device_name, cache_enabled=True):
        if cache_enabled:
            if device_name in self.cnfm_release:
                return self.cnfm_release[device_name]

        managed_objects = self.get_cnfm_release_mo(device_name, cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.cnfm_release[device_name] = []
        for managed_object in managed_objects:
            cnfm_release_info = self.get_cnfm_release_info(
                managed_object
            )
            self.cnfm_release[device_name].append(
                cnfm_release_info
            )

        return self.cnfm_release[device_name]

    def match_cnfm_release(self, cnfm_release_info, cnfm_release_filter):
        if cnfm_release_filter is None or len(cnfm_release_filter) == 0:
            return True

        for ap_rule in cnfm_release_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, cnfm_release_info['name']):
                    return False

            if not key_found:
                self.log.error(
                    'match_cnfm_release',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_cnfm_releases(self, device_name, object_filter=None, cache_enabled=True):
        all_cnfm_releases = self.get_cnfm_releases_info(device_name, cache_enabled=cache_enabled)
        if all_cnfm_releases is None:
            return None

        cnfm_releases = []

        for cnfm_release_info in all_cnfm_releases:
            if not self.match_cnfm_release(cnfm_release_info, object_filter):
                continue

            cnfm_releases.append(
                cnfm_release_info
            )

        return cnfm_releases
