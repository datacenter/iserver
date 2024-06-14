from lib import filter_helper


class NsoCnfmDeviceInfo():
    def __init__(self):
        self.cnfm_device = None

    def get_cnfm_device_info(self, device_name, cnfm_device_mo):
        if cnfm_device_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        info['name'] = device_name

        info['status_code'] = []
        codes_mo = self.get(
            cnfm_device_mo['core-fp-common-status-codes:status-codes'],
            'core-function-pack'
        )[0]
        for code_mo in codes_mo['status-code']:
            info['status_code'].append(
                code_mo
            )

        info['cluster'] = []
        clusters_mo = None
        if 'k8s-cnfm:clusters' in cnfm_device_mo:
            clusters_mo = self.get(
                cnfm_device_mo['k8s-cnfm:clusters'],
                'cluster'
            )

        if clusters_mo is not None:
            for cluster_mo in clusters_mo:
                cluster_info = {}
                cluster_info['__Output'] = {}
                cluster_info['name'] = cluster_mo['name']
                cluster_config = self.get(
                    cluster_mo,
                    'config'
                )
                if cluster_config is not None:
                    cluster_info['type'] = 'KubeConfig'
                    cluster_info['access'] = None
                    cluster_info['namespace'] = None

                if cluster_config is None:
                    cluster_info['type'] = 'ServiceAccount'
                    cluster_info['access'] = self.get(
                        cluster_mo,
                        'namespace-access'
                    )
                    cluster_info['namespace'] = []
                    if cluster_info['access'] == 'selective':
                        namespaces_mo = self.get(
                            cluster_mo,
                            'namespace'
                        )
                        if namespaces_mo is not None:
                            for namespace_mo in namespaces_mo:
                                cluster_info['namespace'].append(
                                    namespace_mo['name']
                                )

                info['cluster'].append(
                    cluster_info
                )

            info['cluster_count'] = len(info['cluster'])

        return info

    def get_cnfm_devices_info(self, cache_enabled=True):
        if cache_enabled:
            if self.cnfm_device is not None:
                return self.cnfm_device

        devices = self.get_devices(
            object_filter=['type:cnfm']
        )
        if devices is None:
            return None

        self.cnfm_device = []
        for device in devices:
            managed_object = self.get_cnfm_device_mo(device['name'], cache_enabled=cache_enabled)
            if managed_object is None:
                continue

            self.cnfm_device.append(
                self.get_cnfm_device_info(
                    device['name'],
                    managed_object
                )
            )

        return self.cnfm_device

    def match_cnfm_device(self, cnfm_device_info, cnfm_device_filter):
        if cnfm_device_filter is None or len(cnfm_device_filter) == 0:
            return True

        for ap_rule in cnfm_device_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, cnfm_device_info['name']):
                    return False

            if not key_found:
                self.log.error(
                    'match_cnfm_device',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_cnfm_devices(self, object_filter=None, cnfi_info=False, device_info=False, cache_enabled=True):
        all_cnfm_devices = self.get_cnfm_devices_info(cache_enabled=cache_enabled)
        if all_cnfm_devices is None:
            return None

        cnfm_devices = []

        for cnfm_device_info in all_cnfm_devices:
            if not self.match_cnfm_device(cnfm_device_info, object_filter):
                continue

            cnfm_device_info['device'] = self.get_device(
                cnfm_device_info['name'],
                sync_info=device_info,
                cache_enabled=cache_enabled
            )

            if cnfi_info:
                cnfm_device_info['cnfi_count'] = 0
                cnfm_device_info['cnfi_ready'] = 0
                for cluster_info in cnfm_device_info['cluster']:
                    cluster_info['cnfi'] = self.get_cnfm_cnfis(
                        object_filter=[
                            'device:%s' % (cnfm_device_info['name']),
                            'cluster:%s' % (cluster_info['name'])
                        ],
                        plan_info=True
                    )

                    cluster_info['cnfi_count'] = len(
                        cluster_info['cnfi']
                    )
                    cluster_info['cnfi_ready'] = 0
                    for cnfd_cnfi_info in cluster_info['cnfi']:
                        if cnfd_cnfi_info['isReady']:
                            cluster_info['cnfi_ready'] = cluster_info['cnfi_ready'] + 1

                    if cluster_info['cnfi_count'] == 0:
                        cluster_info['cnfi_summary'] = '--'
                    else:
                        cluster_info['cnfi_summary'] = '%s/%s' % (
                            cluster_info['cnfi_ready'],
                            cluster_info['cnfi_count']
                        )
                        if cluster_info['cnfi_ready'] == cluster_info['cnfi_count']:
                            cluster_info['__Output']['cnfi_summary'] = 'Green'
                        else:
                            cluster_info['__Output']['cnfi_summary'] = 'Red'

                    cnfm_device_info['cnfi_count'] = cnfm_device_info['cnfi_count'] + cluster_info['cnfi_count']
                    cnfm_device_info['cnfi_ready'] = cnfm_device_info['cnfi_ready'] + cluster_info['cnfi_ready']

                if cnfm_device_info['cnfi_count'] == 0:
                    cnfm_device_info['cnfi_summary'] = '--'
                else:
                    cnfm_device_info['cnfi_summary'] = '%s/%s' % (
                        cnfm_device_info['cnfi_ready'],
                        cnfm_device_info['cnfi_count']
                    )
                    if cnfm_device_info['cnfi_ready'] == cnfm_device_info['cnfi_count']:
                        cnfm_device_info['__Output']['cnfi_summary'] = 'Green'
                    else:
                        cnfm_device_info['__Output']['cnfi_summary'] = 'Red'

            cnfm_devices.append(
                cnfm_device_info
            )

        return cnfm_devices
