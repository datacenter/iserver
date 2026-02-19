from lib import filter_helper


class K8sLeaseInfo():
    def __init__(self):
        self.lease = None

    def get_lease_info(self, lease_mo):
        if lease_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            lease_mo
        )
        info.update(metadata_info)

        info['spec'] = self.get(lease_mo, 'spec')
        info['status'] = self.get(lease_mo, 'status')
        info['identity'] = self.get(lease_mo, 'spec:holderIdentity')
        return info
    
    def get_leases_info(self, cache_enabled=True):
        if cache_enabled:
            if self.lease is not None:
                return self.lease

        managed_objects = self.get_lease_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.lease = []
        for managed_object in managed_objects:
            lease_info = {}
            lease_info['info'] = self.get_lease_info(
                managed_object
            )
            lease_info['mo'] = managed_object
            self.lease.append(
                lease_info
            )

        return self.lease

    def match_lease(self, lease_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'namespace':
                key_found = True
                if not filter_helper.match_string(value, lease_info['namespace']):
                    return False

            if key == 'name':
                key_found = True
                if not filter_helper.match_namespace_name(value, '%s/%s' % (lease_info['namespace'], lease_info['name'])):
                    return False

            if not key_found:
                self.log.error(
                    'match_lease',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_leases(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_leases = self.get_leases_info(cache_enabled=cache_enabled)
        if all_leases is None:
            return None

        leases = []

        for lease_info in all_leases:
            if not self.match_lease(lease_info['info'], object_filter):
                continue

            if return_mo:
                leases.append(
                    lease_info['mo']
                )
                continue

            leases.append(
                lease_info['info']
            )

        return leases

    def is_lease(self, namespace, name, cache_enabled=True, optimized=False):
        if optimized:
            if self.get_lease_optimized(namespace, name, cache_enabled=cache_enabled) is None:
                return False
            return True

        if self.get_lease(namespace, name, cache_enabled=cache_enabled) is None:
            return False
        
        return True

    def get_lease_optimized(self, namespace, name, return_mo=False, cache_enabled=True):
        lease_mo = self.get_lease_mo(
            namespace=namespace, 
            name=name, 
            cache_enabled=cache_enabled
        )
        if return_mo:
            return lease_mo
        
        return self.get_lease_info(lease_mo)
    
    def get_lease(self, namespace, name, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'namespace:%s' % (namespace)
        )
        object_filter.append(
            'name:%s' % (name)
        )
        leases = self.get_leases(
            object_filter=object_filter,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if leases is None:
            return None

        if len(leases) == 1:
            return leases[0]

        return None
