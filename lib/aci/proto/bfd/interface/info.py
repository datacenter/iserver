import copy


class ProtocolBfdInterfaceInfo():
    def __init__(self):
        self.bfd_interfaces = {}

    def add_protocol_bfd_interface_session_info(self, interfaces, sessions, remove_no_sessions=False):
        for interface in interfaces:
            interface['sessionUp'] = 0
            interface['sessionCount'] = 0

            for session in sessions:
                if session['ifId'] == interface['id']:
                    if session['up']:
                        interface['sessionUp'] = interface['sessionUp'] + 1
                    interface['sessionCount'] = interface['sessionCount'] + 1

            interface['sessionSummary'] = '%s/%s' % (
                interface['sessionUp'],
                interface['sessionCount']
            )

            if interface['sessionUp'] == interface['sessionCount']:
                interface['__Output']['sessionSummary'] = 'Green'
            else:
                interface['__Output']['sessionSummary'] = 'Red'

        if remove_no_sessions:
            new_interfaces = []
            for interface in interfaces:
                if interface['sessionCount'] > 0:
                    new_interfaces.append(
                        interface
                    )

            interfaces = copy.deepcopy(new_interfaces)

        return interfaces

    def get_protocol_bfd_interface_info(self, managed_object):
        info = {}
        info['__Output'] = {}
        for key in managed_object:
            info[key] = managed_object[key]

        info['__Output']['id'] = 'Yellow'

        if info['adminSt'] == 'enabled':
            info['__Output']['adminSt'] = 'Green'
        else:
            info['__Output']['adminSt'] = 'Red'

        return info

    def get_protocol_bfd_interfaces_info(self, pod_id, node_id):
        key = '%s.%s' % (pod_id, node_id)
        if key in self.bfd_interfaces:
            return self.bfd_interfaces[key]

        bfd_interfaces_mo = self.get_protocol_bfd_interfaces_mo(pod_id, node_id)
        if bfd_interfaces_mo is not None:
            self.bfd_interfaces[key] = []
            for bfd_interface_mo in bfd_interfaces_mo:
                self.bfd_interfaces[key].append(
                    self.get_protocol_bfd_interface_info(
                        bfd_interface_mo
                    )
                )

        self.log.apic_mo(
            'bfd.interface.info.%s' % (key),
            self.bfd_interfaces[key]
        )

        return self.bfd_interfaces[key]

    def match_protocol_bfd_interface(self, bfd_interface_info, bfd_interface_filter):
        if bfd_interface_filter is None or len(bfd_interface_filter) == 0:
            return True

        for ap_rule in bfd_interface_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])
            # if key == 'name':
            #     if not filter_helper.match_string(value, bfd_interface_info['domain_name']):
            #         return False

            # if key == 'mac':
            #     if not filter_helper.match_mac(value, bfd_interface_info['mac']):
            #         return False

            # if key == 'ip':
            #     if not filter_helper.match_string(value, bfd_interface_info['ip']):
            #         return False

            # if key == 'subnet':
            #     if not ip_helper.is_ipv4_in_cidr(bfd_interface_info['ip'], value):
            #         return False

        return True

    def get_protocol_bfd_interfaces(self, pod_id, node_id, bfd_interface_filter=None):
        all_bfd_interfaces = self.get_protocol_bfd_interfaces_info(pod_id, node_id)
        if all_bfd_interfaces is None:
            return None

        bfd_interfaces = []

        for bfd_interface_info in all_bfd_interfaces:
            if not self.match_protocol_bfd_interface(bfd_interface_info, bfd_interface_filter):
                continue

            bfd_interfaces.append(
                bfd_interface_info
            )

        bfd_interfaces = sorted(
            bfd_interfaces,
            key=lambda i: i['id']
        )

        return bfd_interfaces
