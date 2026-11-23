from lib import filter_helper


class InterfaceBriefInfo():
    def __init__(self):
        self.interface_brief = None

    def get_interface_brief_info(self, interface_brief_mo):
        if interface_brief_mo is None:
            return None

        info = {}
        info['__Output'] = {}
        info['nexus_name'] = self.nexus_name

        for key in interface_brief_mo:
            info[key] = interface_brief_mo[key]

        info['type'] = None

        if info['interface'].startswith('mgmt'):
            info['type'] = 'mgmt'
            if info['state'] == 'up':
                info['__Output']['state'] = 'Green'
            else:
                info['__Output']['state'] = 'Red'

        if info['interface'].startswith('Ethernet'):
            info['type'] = 'eth'
            if 'portchan' not in info:
                info['portchan'] = None
            if info['state'] == 'up':
                info['__Output']['state'] = 'Green'
            else:
                info['__Output']['state'] = 'Red'
            if 'state_rsn_desc' not in info:
                info['state_rsn_desc'] = None

        if info['interface'].startswith('port-channel'):
            info['type'] = 'pc'
            info['interface'] = 'Po%s' % (info['interface'].split('port-channel')[1])
            if info['state'] == 'up':
                info['__Output']['state'] = 'Green'
            else:
                info['__Output']['state'] = 'Red'
            if 'proto' not in info:
                info['proto'] = None

        if info['interface'].startswith('Vlan'):
            info['type'] = 'vlan'
            if info['svi_admin_state'] == 'up':
                info['__Output']['svi_admin_state'] = 'Green'
            else:
                info['__Output']['svi_admin_state'] = 'Red'
            if 'svi_rsn_desc' not in info:
                info['svi_rsn_desc'] = None

        return info

    def get_interfaces_brief_info(self, local_cache_enabled=True, cache_enabled=True):
        if local_cache_enabled:
            if self.interface_brief is not None:
                return self.interface_brief

        managed_objects = self.get_interface_brief_mo(
            local_cache_enabled=local_cache_enabled,
            cache_enabled=cache_enabled
        )
        if managed_objects is None:
            self.log.error(
                'get_interfaces_brief_info',
                'No interface neighbor managed objects: %s' % (self.nexus_name)
            )
            return None

        self.interface_brief = []
        for managed_object in managed_objects['TABLE_interface']['ROW_interface']:
            interface_brief_info = self.get_interface_brief_info(
                managed_object
            )
            self.interface_brief.append(
                interface_brief_info
            )

        return self.interface_brief

    def match_interface_brief(self, interface_brief_info, interface_brief_filter):
        if interface_brief_filter is None or len(interface_brief_filter) == 0:
            return True

        for ap_rule in interface_brief_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, interface_brief_info['interface']):
                    return False

            if not key_found:
                self.log.error(
                    'match_interface_brief',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_interfaces_brief(self, object_filter=None, local_cache_enabled=True, cache_enabled=True):
        all_interfaces = self.get_interfaces_brief_info(
            local_cache_enabled=local_cache_enabled,
            cache_enabled=cache_enabled
        )
        if all_interfaces is None:
            self.log.error(
                'get_interfaces_brief',
                'Failed to get interfaces brief: %s' % (self.nexus_name)
            )
            return None

        interfaces = []

        for interface_info in all_interfaces:
            if not self.match_interface_brief(interface_info, object_filter):
                continue

            interfaces.append(
                interface_info
            )

        return interfaces
