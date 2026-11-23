from lib import filter_helper


class InterfaceStateInfo():
    def __init__(self):
        self.interface = None

    def get_interface_info(self, interface_mo):
        if interface_mo is None:
            return None

        info = {}
        info['__Output'] = {}
        info['nexus_name'] = self.nexus_name

        for key in interface_mo:
            info[key] = interface_mo[key]

        return info

    def get_interfaces_info(self, local_cache_enabled=True, cache_enabled=True):
        if local_cache_enabled:
            if self.interface is not None:
                return self.interface

        managed_objects = self.get_interface_mo(
            local_cache_enabled=local_cache_enabled,
            cache_enabled=cache_enabled
        )
        if managed_objects is None:
            self.log.error(
                'get_interfaces_info',
                'No interface neighbor managed objects: %s' % (self.nexus_name)
            )
            return None

        self.interface = []
        for managed_object in managed_objects['TABLE_interface']['ROW_interface']:
            interface_info = self.get_interface_info(
                managed_object
            )
            self.interface.append(
                interface_info
            )

        return self.interface

    def match_interface(self, interface_info, interface_filter):
        if interface_filter is None or len(interface_filter) == 0:
            return True

        for ap_rule in interface_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, interface_info['interface']):
                    return False

            if not key_found:
                self.log.error(
                    'match_interface',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_interfaces(self, object_filter=None, local_cache_enabled=True, cache_enabled=True):
        all_interfaces = self.get_interfaces_info(
            local_cache_enabled=local_cache_enabled,
            cache_enabled=cache_enabled
        )
        if all_interfaces is None:
            self.log.error(
                'get_interfaces',
                'Failed to get interface neighbors: %s' % (self.nexus_name)
            )
            return None

        interfaces = []

        for interface_info in all_interfaces:
            if not self.match_interface(interface_info, object_filter):
                continue

            interfaces.append(
                interface_info
            )

        return interfaces
