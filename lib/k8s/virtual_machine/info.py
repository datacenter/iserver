from lib import filter_helper


class K8sVirtualMachineInfo():
    def __init__(self):
        self.virtual_machine = None

    def get_virtual_machine_info(self, virtual_machine_mo):
        if virtual_machine_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        info['namespace'] = self.get(virtual_machine_mo, 'metadata:namespace')
        info['name'] = self.get(virtual_machine_mo, 'metadata:name')
        info['namespace_name'] = '%s/%s' % (
            info['namespace'],
            info['name']
        )

        return info

    def get_virtual_machines_info(self, cache_enabled=True):
        if cache_enabled:
            if self.virtual_machine is not None:
                return self.virtual_machine

        managed_objects = self.get_virtual_machine_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.virtual_machine = []
        for managed_object in managed_objects:
            virtual_machine_info = {}
            virtual_machine_info['info'] = self.get_virtual_machine_info(
                managed_object
            )
            virtual_machine_info['mo'] = managed_object
            self.virtual_machine.append(
                virtual_machine_info
            )

        return self.virtual_machine

    def match_virtual_machine(self, virtual_machine_info, virtual_machine_filter):
        if virtual_machine_filter is None or len(virtual_machine_filter) == 0:
            return True

        for ap_rule in virtual_machine_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if key == 'name':
                key_found = True
                if not filter_helper.match_tenant_name(value, virtual_machine_info['namespace_name']):
                    return False

            if key == 'namespace':
                key_found = True
                if not filter_helper.match_string(value, virtual_machine_info['namespace']):
                    return False

            if not key_found:
                self.log.error(
                    'match_virtual_machine',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_virtual_machines(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_virtual_machines = self.get_virtual_machines_info(cache_enabled=cache_enabled)
        if all_virtual_machines is None:
            return None

        virtual_machines = []

        for virtual_machine_info in all_virtual_machines:
            if not self.match_virtual_machine(virtual_machine_info['info'], object_filter):
                continue

            if return_mo:
                virtual_machines.append(
                    virtual_machine_info['mo']
                )
                continue

            virtual_machines.append(
                virtual_machine_info['info']
            )

        return virtual_machines

    def get_virtual_machine(self, namespace, name, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append('namespace:%s' % (namespace))
        object_filter.append('name:%s' % (name))
        instances = self.get_virtual_machines(
            object_filter=object_filter,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if instances is None or len(instances) != 1:
            return None
        return instances[0]

    def is_virtual_machine(self, namespace, name, cache_enabled=True):
        if self.get_virtual_machine(namespace, name, cache_enabled=cache_enabled) is None:
            return False
        return True
