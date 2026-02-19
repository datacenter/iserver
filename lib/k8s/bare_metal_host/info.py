from lib import filter_helper


class K8sBareMetalHostInfo():
    def __init__(self):
        self.bare_metal_host = None

    def get_bare_metal_host_info(self, bare_metal_host_mo):
        if bare_metal_host_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            bare_metal_host_mo
        )
        info.update(metadata_info)

        info['spec'] = self.get(bare_metal_host_mo, 'spec')
        info['status'] = self.get(bare_metal_host_mo, 'status')
        
        info['info'] = {}
        info['info']['status'] = self.get(bare_metal_host_mo, 'status:operationalStatus')
        if info['info']['status'] == 'error':
            info['info']['status'] = self.get(bare_metal_host_mo, 'status:errorType')
            
        return info

    def get_bare_metal_hosts_info(self, cache_enabled=True):
        if cache_enabled:
            if self.bare_metal_host is not None:
                return self.bare_metal_host

        managed_objects = self.get_bare_metal_host_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.bare_metal_host = []
        for managed_object in managed_objects:
            bare_metal_host_info = {}
            bare_metal_host_info['info'] = self.get_bare_metal_host_info(
                managed_object
            )
            bare_metal_host_info['mo'] = managed_object
            self.bare_metal_host.append(
                bare_metal_host_info
            )

        return self.bare_metal_host

    def match_bare_metal_host(self, bare_metal_host_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'namespace':
                key_found = True
                if not filter_helper.match_string(value, bare_metal_host_info['namespace']):
                    return False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, bare_metal_host_info['name']):
                    return False

            if not key_found:
                self.log.error(
                    'match_bare_metal_host',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_bare_metal_hosts(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_bare_metal_hosts = self.get_bare_metal_hosts_info(cache_enabled=cache_enabled)
        if all_bare_metal_hosts is None:
            return None

        bare_metal_hosts = []

        for bare_metal_host_info in all_bare_metal_hosts:
            if not self.match_bare_metal_host(bare_metal_host_info['info'], object_filter):
                continue

            if return_mo:
                bare_metal_hosts.append(
                    bare_metal_host_info['mo']
                )
                continue

            bare_metal_hosts.append(
                bare_metal_host_info['info']
            )

        return bare_metal_hosts

    def is_bare_metal_host(self, namespace, name, cache_enabled=True):
        if self.get_bare_metal_host(namespace, name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def get_bare_metal_host(self, namespace, name, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'namespace:%s' % (namespace)
        )
        object_filter.append(
            'name:%s' % (name)
        )
        bare_metal_hosts = self.get_bare_metal_hosts(
            object_filter=object_filter,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if bare_metal_hosts is None:
            return None

        if len(bare_metal_hosts) == 1:
            return bare_metal_hosts[0]

        return None
