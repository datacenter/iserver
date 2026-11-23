from lib import filter_helper


class K8sHostInfo():
    def __init__(self):
        self.host = None

    def get_host_info(self, host_mo):
        if host_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            host_mo
        )
        info.update(metadata_info)

        info['spec'] = self.get(host_mo, 'spec')
        info['status'] = self.get(host_mo, 'status')
        return info
    
    def get_hosts_info(self, cache_enabled=True):
        if cache_enabled:
            if self.host is not None:
                return self.host

        managed_objects = self.get_host_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.host = []
        for managed_object in managed_objects:
            host_info = {}
            host_info['info'] = self.get_host_info(
                managed_object
            )
            host_info['mo'] = managed_object
            self.host.append(
                host_info
            )

        return self.host

    def match_host(self, host_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'namespace':
                key_found = True
                if not filter_helper.match_string(value, host_info['namespace']):
                    return False

            if key == 'name':
                key_found = True
                if not filter_helper.match_namespace_name(value, '%s/%s' % (host_info['namespace'], host_info['name'])):
                    return False

            if not key_found:
                self.log.error(
                    'match_host',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_hosts(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_hosts = self.get_hosts_info(cache_enabled=cache_enabled)
        if all_hosts is None:
            return None

        hosts = []

        for host_info in all_hosts:
            if not self.match_host(host_info['info'], object_filter):
                continue

            if return_mo:
                hosts.append(
                    host_info['mo']
                )
                continue

            hosts.append(
                host_info['info']
            )

        return hosts

    def is_host(self, namespace, name, cache_enabled=True):
        if self.get_host(namespace, name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def get_host(self, namespace, name, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'namespace:%s' % (namespace)
        )
        object_filter.append(
            'name:%s' % (name)
        )
        hosts = self.get_hosts(
            object_filter=object_filter,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if hosts is None:
            return None

        if len(hosts) == 1:
            return hosts[0]

        return None
