from lib import filter_helper


class K8sVirtualMachinePoolInfo():
    def __init__(self):
        self.virtual_machine_pool = None

    def get_virtual_machine_pool_info(self, virtual_machine_pool_mo):
        if virtual_machine_pool_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            virtual_machine_pool_mo
        )
        info.update(metadata_info)

        return info

    def get_virtual_machine_pools_info(self, cache_enabled=True):
        if cache_enabled:
            if self.virtual_machine_pool is not None:
                return self.virtual_machine_pool

        managed_objects = self.get_virtual_machine_pool_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.virtual_machine_pool = []
        for managed_object in managed_objects:
            virtual_machine_pool_info = {}
            virtual_machine_pool_info['info'] = self.get_virtual_machine_pool_info(
                managed_object
            )
            virtual_machine_pool_info['mo'] = managed_object
            self.virtual_machine_pool.append(
                virtual_machine_pool_info
            )

        return self.virtual_machine_pool

    def match_virtual_machine_pool(self, virtual_machine_pool_info, virtual_machine_pool_filter):
        if virtual_machine_pool_filter is None or len(virtual_machine_pool_filter) == 0:
            return True

        for ap_rule in virtual_machine_pool_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if not key_found:
                self.log.error(
                    'match_virtual_machine_pool',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_virtual_machine_pools(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_virtual_machine_pools = self.get_virtual_machine_pools_info(cache_enabled=cache_enabled)
        if all_virtual_machine_pools is None:
            return None

        virtual_machine_pools = []

        for virtual_machine_pool_info in all_virtual_machine_pools:
            if not self.match_virtual_machine_pool(virtual_machine_pool_info['info'], object_filter):
                continue

            if return_mo:
                virtual_machine_pools.append(
                    virtual_machine_pool_info['mo']
                )
                continue

            virtual_machine_pools.append(
                virtual_machine_pool_info['info']
            )

        return virtual_machine_pools
