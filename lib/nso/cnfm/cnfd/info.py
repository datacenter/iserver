from lib import filter_helper


class NsoCnfmCnfdInfo():
    def __init__(self):
        self.cnfm_cnfd = None

    def get_cnfm_cnfd_info(self, cnfm_cnfd_mo):
        if cnfm_cnfd_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        info['name'] = self.get(
            cnfm_cnfd_mo,
            'name'
        )

        info['chart'] = self.get(
            cnfm_cnfd_mo,
            'chart-name'
        )

        info['local'] = False
        info['localTick'] = '\u2717'
        if 'local' in cnfm_cnfd_mo:
            info['local'] = True
            info['localTick'] = '\u2713'

        info['version'] = []
        versions_mo = self.get(
            cnfm_cnfd_mo,
            'chart-version'
        )
        for version_mo in versions_mo:
            version_info = {}
            version_info['__Output'] = {}
            version_info['version'] = self.get(
                version_mo,
                'version'
            )

            version_info['app'] = self.get(
                version_mo,
                'app-version'
            )
            if version_info['app'] == 'None':
                version_info['app'] = None

            version_info['description'] = self.get(
                version_mo,
                'description'
            )
            if version_info['description'] == 'None':
                version_info['description'] = None

            version_info['values'] = []
            values_mo = self.get(
                version_mo,
                'values:key-value'
            )
            for value_mo in values_mo:
                value_info = {}
                value_info['key'] = value_mo['key']
                value_info['value'] = None
                if 'value-str' in value_mo:
                    value_info['value'] = value_mo['value-str']
                if 'value-int' in value_mo:
                    value_info['value'] = int(value_mo['value-int'])
                if 'value-bool' in value_mo:
                    value_info['value'] = value_mo['value-bool']

                version_info['values'].append(
                    value_info
                )

            info['version'].append(
                version_info
            )

        return info

    def get_cnfm_cnfds_info(self, cache_enabled=True):
        if cache_enabled:
            if self.cnfm_cnfd is not None:
                return self.cnfm_cnfd

        managed_objects = self.get_cnfm_cnfd_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.cnfm_cnfd = []
        for managed_object in managed_objects:
            cnfm_cnfd_info = self.get_cnfm_cnfd_info(
                managed_object
            )
            self.cnfm_cnfd.append(
                cnfm_cnfd_info
            )

        return self.cnfm_cnfd

    def match_cnfm_cnfd(self, cnfm_cnfd_info, cnfm_cnfd_filter):
        if cnfm_cnfd_filter is None or len(cnfm_cnfd_filter) == 0:
            return True

        for ap_rule in cnfm_cnfd_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, cnfm_cnfd_info['name']):
                    return False

            if key == 'chart':
                key_found = True
                if not filter_helper.match_string(value, cnfm_cnfd_info['chart']):
                    return False

            if key == 'version':
                key_found = True
                found = False
                for version_info in cnfm_cnfd_info['version']:
                    if filter_helper.match_string(value, version_info['version']):
                        found = True
                        break

                if not found:
                    return False

            if not key_found:
                self.log.error(
                    'match_cnfm_cnfd',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_cnfm_cnfds(self, object_filter=None, cnfi_info=True, cache_enabled=True):
        all_cnfm_cnfds = self.get_cnfm_cnfds_info(cache_enabled=cache_enabled)
        if all_cnfm_cnfds is None:
            return None

        cnfm_cnfds = []

        for cnfm_cnfd_info in all_cnfm_cnfds:
            if not self.match_cnfm_cnfd(cnfm_cnfd_info, object_filter):
                continue

            if cnfi_info:
                for version_info in cnfm_cnfd_info['version']:
                    version_info['cnfi'] = self.get_cnfm_cnfis(
                        object_filter=[
                            'cnfd:%s' % (cnfm_cnfd_info['name']),
                            'version:%s' % (version_info['version'])
                        ],
                        plan_info=True
                    )
                    version_info['cnfi_count'] = len(
                        version_info['cnfi']
                    )
                    version_info['cnfi_ready'] = 0
                    for cnfd_cnfi_info in version_info['cnfi']:
                        if cnfd_cnfi_info['isReady']:
                            version_info['cnfi_ready'] = version_info['cnfi_ready'] + 1

                    if version_info['cnfi_count'] == 0:
                        version_info['cnfi_summary'] = '--'
                    else:
                        version_info['cnfi_summary'] = '%s/%s' % (
                            version_info['cnfi_ready'],
                            version_info['cnfi_count']
                        )
                        if version_info['cnfi_ready'] == version_info['cnfi_count']:
                            version_info['__Output']['cnfi_summary'] = 'Green'
                        else:
                            version_info['__Output']['cnfi_summary'] = 'Red'

            cnfm_cnfds.append(
                cnfm_cnfd_info
            )

        cnfm_cnfds = sorted(
            cnfm_cnfds,
            key=lambda i: i['name']
        )

        return cnfm_cnfds
