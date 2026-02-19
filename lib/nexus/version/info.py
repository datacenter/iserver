class VersionInfo():
    def __init__(self):
        self.version = None

    def get_version_info(self, version_mo):
        if version_mo is None:
            return None

        info = {}
        info['__Output'] = {}
        info['nexus_name'] = self.nexus_name

        excludeded_keys = [
            'TABLE_package_list',
            'header_str'
        ]
        for key in version_mo:
            if key not in excludeded_keys:
                info[key] = version_mo[key]

        info['uptime'] = ''
        if isinstance(info['kern_uptm_days'], int) and info['kern_uptm_days'] > 0:
            info['uptime'] = '%s days ' % (info['kern_uptm_days'])

        info['uptime'] = '%s%s:%s:%s' % (
            info['uptime'],
            info['kern_uptm_hrs'],
            info['kern_uptm_mins'],
            info['kern_uptm_secs']
        )

        info['memory_size'] = '%s%s' % (
            info['memory'],
            info['mem_type']
        )
        if info['mem_type'] == 'kB':
            if isinstance(info['memory'], int):
                info['memory_size'] = self.info_handler.convert_memory(
                    info['memory'] * 1024
                )
            if isinstance(info['memory'], str):
                info['memory_size'] = self.info_handler.convert_memory(
                    int(info['memory']) * 1024
                )

        return info

    def get_version(self, cache_enabled=True):
        version_mo = self.get_version_mo(cache_enabled=cache_enabled)
        if version_mo is None:
            self.log.error(
                'get_version',
                'Failed to get version: %s' % (self.nexus_name)
            )
            return None

        return self.get_version_info(version_mo)
