from lib import filter_helper


class NsoCnfmCnfiInfo():
    def __init__(self):
        self.cnfm_cnfi = None

    def get_cnfm_cnfi_info(self, cnfm_cnfi_mo):
        if cnfm_cnfi_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        info['namespace'] = self.get(
            cnfm_cnfi_mo,
            'namespace'
        )

        info['name'] = self.get(
            cnfm_cnfi_mo,
            'name'
        )

        info['namespace_name'] = '%s/%s' % (
            info['namespace'],
            info['name']
        )

        info['cnfd'] = self.get(
            cnfm_cnfi_mo,
            'cnfd'
        )

        info['version'] = self.get(
            cnfm_cnfi_mo,
            'chart-version'
        )

        info['values'] = []
        values_mo = self.get(
            cnfm_cnfi_mo,
            'values:key-value',
            on_error=[],
            on_none=[]
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

            info['values'].append(
                value_info
            )

        info['custom_values'] = len(info['values'])

        if info['custom_values'] == 0:
            info['cnfd_version'] = '%s:%s' % (
                info['cnfd'],
                info['version']
            )
        else:
            info['cnfd_version'] = '%s:%s (%s)' % (
                info['cnfd'],
                info['version'],
                info['custom_values']
            )

        info['device'] = self.get(
            cnfm_cnfi_mo,
            'device'
        )

        info['cluster'] = self.get(
            cnfm_cnfi_mo,
            'cluster'
        )

        info['device_cluster'] = '%s:%s' % (
            info['device'],
            info['cluster']
        )

        info['onboard'] = False
        info['onboardTick'] = '\u2717'
        info['authgroup'] = None

        onboard_mo = self.get(
            cnfm_cnfi_mo,
            'onboard'
        )
        if onboard_mo is not None:
            info['onboard'] = True
            info['onboardTick'] = '\u2713'
            info['authgroup'] = self.get(
                onboard_mo,
                'authgroup'
            )

        return info

    def get_cnfm_cnfis_info(self, cache_enabled=True):
        if cache_enabled:
            if self.cnfm_cnfi is not None:
                return self.cnfm_cnfi

        managed_objects = self.get_cnfm_cnfi_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.cnfm_cnfi = []
        for managed_object in managed_objects:
            cnfm_cnfi_info = self.get_cnfm_cnfi_info(
                managed_object
            )
            self.cnfm_cnfi.append(
                cnfm_cnfi_info
            )

        return self.cnfm_cnfi

    def match_cnfm_cnfi(self, cnfm_cnfi_info, cnfm_cnfi_filter):
        if cnfm_cnfi_filter is None or len(cnfm_cnfi_filter) == 0:
            return True

        for ap_rule in cnfm_cnfi_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if key == 'namespace':
                key_found = True
                if not filter_helper.match_string(value, cnfm_cnfi_info['namespace']):
                    return False

            if key == 'name':
                key_found = True
                if not filter_helper.match_namespace_name(
                    value,
                    '%s/%s' % (
                        cnfm_cnfi_info['namespace'],
                        cnfm_cnfi_info['name']
                    )
                ):
                    return False

            if key == 'cluster':
                key_found = True
                if not filter_helper.match_string(value, cnfm_cnfi_info['cluster']):
                    return False

            if key == 'cnfd':
                key_found = True
                if not filter_helper.match_string(value, cnfm_cnfi_info['cnfd']):
                    return False

            if key == 'version':
                key_found = True
                if not filter_helper.match_string(value, cnfm_cnfi_info['version']):
                    return False

            if key == 'device':
                key_found = True
                if not filter_helper.match_string(value, cnfm_cnfi_info['device']):
                    return False

            if not key_found:
                self.log.error(
                    'match_cnfm_cnfi',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_cnfm_cnfis(self, object_filter=None, cnfd_info=False, plan_info=False, result_info=False, device_info=False, cache_enabled=True):
        all_cnfm_cnfis = self.get_cnfm_cnfis_info(cache_enabled=cache_enabled)
        if all_cnfm_cnfis is None:
            return None

        cnfm_cnfis = []

        for cnfm_cnfi_info in all_cnfm_cnfis:
            if not self.match_cnfm_cnfi(cnfm_cnfi_info, object_filter):
                continue

            if cnfd_info:
                cnfi_cnfd_info = self.get_cnfm_cnfd(
                    object_filter=[
                        'name:%s' % (cnfm_cnfi_info['cnfd']),
                        'version:%s' % (cnfm_cnfi_info['version'])
                    ],
                    cache_enabled=cache_enabled
                )
                if cnfi_cnfd_info is None or len(cnfi_cnfd_info) != 1:
                    self.log.error(
                        'get_cnfm_cnfis',
                        'Failed to cnfd for cnfi: %s' % (
                            cnfm_cnfi_info['name']
                        )
                    )
                    cnfm_cnfi_info['cnfd'] = None
                else:
                    cnfm_cnfi_info['cnfd'] = cnfi_cnfd_info[0]

            if plan_info:
                cnfm_cnfi_info['plan'] = None
                cnfm_cnfi_info['ready'] = None

                cnfm_cnfi_plan_info = self.get_cnfm_plan(
                    cnfm_cnfi_info['name'],
                    cache_enabled=cache_enabled
                )
                if cnfm_cnfi_plan_info is not None:
                    cnfm_cnfi_info['plan'] = cnfm_cnfi_plan_info['component']
                    cnfm_cnfi_info['ready'] = cnfm_cnfi_plan_info['ready']

                    cnfm_cnfi_info['isReady'] = False
                    if cnfm_cnfi_info['ready'] is not None:
                        cnfm_cnfi_info['isReady'] = True
                        for ready_info in cnfm_cnfi_info['ready']:
                            cnfm_cnfi_info['isReady'] = cnfm_cnfi_info['isReady'] and ready_info['ready']

                    if cnfm_cnfi_info['isReady']:
                        cnfm_cnfi_info['readyTick'] = '\u2713'
                        cnfm_cnfi_info['__Output']['readyTick'] = 'Green'
                    else:
                        cnfm_cnfi_info['readyTick'] = '\u2717'
                        cnfm_cnfi_info['__Output']['readyTick'] = 'Red'

            if result_info:
                cnfm_cnfi_result = self.get_cnfm_result(
                    cnfm_cnfi_info['name'],
                    cache_enabled=cache_enabled
                )
                for key in ['alive', 'aliveTick', 'k8s', 'vmi', 'pod', 'replicaset', 'deployment', 'service']:
                    cnfm_cnfi_info[key] = cnfm_cnfi_result[key]

                for key in cnfm_cnfi_result['__Output']:
                    cnfm_cnfi_info['__Output'][key] = cnfm_cnfi_result['__Output'][key]

            if device_info:
                cnfm_cnfi_info['deviceTick'] = '--'
                cnfm_cnfi_info['deviceSyncTick'] = '--'
                if cnfm_cnfi_info['onboard']:
                    cnfm_cnfi_info['deviceTick'] = '\u2717'
                    cnfm_cnfi_info['__Output']['deviceTick'] = 'Red'
                    cnfm_cnfi_info['deviceSyncTick'] = '\u2717'
                    cnfm_cnfi_info['__Output']['deviceSyncTick'] = 'Red'
                    cnfm_cnfi_info['onboardDevice'] = self.get_device(
                        cnfm_cnfi_info['name'],
                        sync_info=True,
                        cache_enabled=cache_enabled
                    )
                    if cnfm_cnfi_info['onboardDevice'] is not None:
                        cnfm_cnfi_info['deviceTick'] = '\u2713'
                        cnfm_cnfi_info['__Output']['deviceTick'] = 'Green'
                        if cnfm_cnfi_info['onboardDevice']['sync']:
                            cnfm_cnfi_info['deviceSyncTick'] = '\u2713'
                            cnfm_cnfi_info['__Output']['deviceSyncTick'] = 'Green'

            cnfm_cnfis.append(
                cnfm_cnfi_info
            )

        cnfm_cnfis = sorted(
            cnfm_cnfis,
            key=lambda i: (
                i['namespace'],
                i['name']
            )
        )

        return cnfm_cnfis
