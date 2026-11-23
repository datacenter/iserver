from lib import filter_helper


class InterfaceTransInfo():
    def __init__(self):
        self.interface_trans = None

    def get_interface_trans_info(self, interface_mo):
        if interface_mo is None:
            return None

        info = {}
        info['__Output'] = {}
        info['nexus_name'] = self.nexus_name

        for key in interface_mo:
            info[key] = interface_mo[key]

        keys = [
            'type',
            'name',
            'partnum',
            'rev',
            'serialnum',
            'nom_bitrate',
            'ciscoid',
            'ciscoid_1',
            'cisco_part_number',
            'cisco_product_id',
            'cisco_vendor_id'
        ]
        for key in keys:
            if key not in info:
                info[key] = None

        return info

    def get_interfaces_trans_info(self, local_cache_enabled=True, cache_enabled=True):
        if local_cache_enabled:
            if self.interface_trans is not None:
                return self.interface_trans

        managed_objects = self.get_interface_trans_mo(
            local_cache_enabled=local_cache_enabled,
            cache_enabled=cache_enabled
        )
        if managed_objects is None:
            self.log.error(
                'get_interfaces_trans_info',
                'No interface neighbor managed objects: %s' % (self.nexus_name)
            )
            return None

        self.interface_trans = []
        for managed_object in managed_objects['TABLE_interface']['ROW_interface']:
            interface_info = self.get_interface_trans_info(
                managed_object
            )
            if interface_info['sfp'] != 'not applicable':
                self.interface_trans.append(
                    interface_info
                )

        return self.interface_trans

    def match_interface_trans(self, interface_info, interface_filter):
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
                    'match_interface_trans',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_interfaces_trans(self, object_filter=None, local_cache_enabled=True, cache_enabled=True):
        all_interfaces = self.get_interfaces_trans_info(
            local_cache_enabled=local_cache_enabled,
            cache_enabled=cache_enabled
        )
        if all_interfaces is None:
            self.log.error(
                'get_interfaces_trans',
                'Failed to get interfaces transceiver: %s' % (self.nexus_name)
            )
            return None

        interfaces = []

        for interface_info in all_interfaces:
            if not self.match_interface_trans(interface_info, object_filter):
                continue

            interfaces.append(
                interface_info
            )

        return interfaces
