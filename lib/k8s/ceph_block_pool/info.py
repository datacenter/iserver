from lib import filter_helper


class K8sCephBlockPoolInfo():
    def __init__(self):
        self.ceph_block_pool = None

    def get_ceph_block_pool_info(self, ceph_block_pool_mo):
        if ceph_block_pool_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            ceph_block_pool_mo
        )
        info.update(metadata_info)

        info['spec'] = self.get(ceph_block_pool_mo, 'spec')
        info['status'] = self.get(ceph_block_pool_mo, 'status')

        info['phase'] = self.get(ceph_block_pool_mo, 'status:phase')
        if info['phase'] is not None and info['phase'].lower() == 'ready':
            info['ready'] = True
            info['readyTick'] = '\u2713'
            info['__Output']['phase'] = 'Green'
            info['__Output']['readyTick'] = 'Green'
        else:
            info['ready'] = False
            info['readyTick'] = '\u2717'
            info['__Output']['phase'] = 'Red'
            info['__Output']['readyTick'] = 'Red'

        info['pool_id'] = self.get(ceph_block_pool_mo, 'status:poolID')
        info['failure_domain'] = self.get(ceph_block_pool_mo, 'status:info:failureDomain')
        info['type'] = self.get(ceph_block_pool_mo, 'status:info:type')

        return info

    def get_ceph_block_pools_info(self, cache_enabled=True):
        if cache_enabled:
            if self.ceph_block_pool is not None:
                return self.ceph_block_pool

        managed_objects = self.get_ceph_block_pool_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.ceph_block_pool = []
        for managed_object in managed_objects:
            info = {}
            info['info'] = self.get_ceph_block_pool_info(
                managed_object
            )
            info['mo'] = managed_object
            self.ceph_block_pool.append(
                info
            )

        return self.ceph_block_pool

    def match_ceph_block_pool(self, object_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'namespace':
                key_found = True
                if not filter_helper.match_string(value, object_info['namespace']):
                    return False

            if key == 'name':
                key_found = True
                if not filter_helper.match_namespace_name(value, '%s/%s' % (object_info['namespace'], object_info['name'])):
                    return False

            if not key_found:
                self.log.error(
                    'match_ceph_block_pool',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_ceph_block_pools(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_objects_infos = self.get_ceph_block_pools_info(cache_enabled=cache_enabled)
        if all_objects_infos is None:
            return None

        object_infos = []

        for object_info in all_objects_infos:
            if not self.match_ceph_block_pool(object_info['info'], object_filter):
                continue

            if return_mo:
                object_infos.append(
                    object_info['mo']
                )
                continue

            object_infos.append(
                object_info['info']
            )

        return object_infos

    def is_ceph_block_pool(self, namespace, name, cache_enabled=True):
        if self.get_ceph_block_pool(namespace, name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def get_ceph_block_pool(self, namespace, name, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'namespace:%s' % (namespace)
        )
        object_filter.append(
            'name:%s' % (name)
        )
        objects_info = self.get_ceph_block_pools(
            object_filter=object_filter,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if objects_info is None:
            return None

        if len(objects_info) == 1:
            return objects_info[0]

        return None
