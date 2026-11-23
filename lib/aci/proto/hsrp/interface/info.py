from lib import filter_helper


class ProtocolHsrpInterfaceInfo():
    def __init__(self):
        self.hsrp_interfaces = {}

    def get_protocol_hsrp_interface_info(self, managed_object):
        info = {}
        info['__Output'] = {}
        for key in managed_object:
            if key == 'stats':
                info[key] = self.get_protocol_hsrp_interface_stats_info(managed_object[key])
                info['stats'] = self.my_output.merge_output(
                    info['stats']
                )
            else:
                info[key] = managed_object[key]

        info['pod_node_name'] = '%s/%s' % (
            info['dn'].split('/')[1],
            self.get_node_name(
                info['dn'].split('/')[2].split('-')[1]
            )
        )

        info['domainName'] = info['dn'].split('/')[6][4:]

        info['__Output']['id'] = 'Yellow'
        if info['adminSt'] == 'enabled':
            info['__Output']['adminSt'] = 'Green'
        else:
            info['__Output']['adminSt'] = 'Red'

        return info

    def get_protocol_hsrp_interfaces_info(self, pod_id, node_id):
        key = '%s.%s' % (pod_id, node_id)
        if key in self.hsrp_interfaces:
            return self.hsrp_interfaces[key]

        hsrp_interfaces_mo = self.get_protocol_hsrp_interfaces_mo(pod_id, node_id)
        if hsrp_interfaces_mo is not None:
            self.hsrp_interfaces[key] = []
            for hsrp_interface_mo in hsrp_interfaces_mo:
                self.hsrp_interfaces[key].append(
                    self.get_protocol_hsrp_interface_info(
                        hsrp_interface_mo
                    )
                )

        self.log.apic_mo(
            'hsrpIf.info.%s' % (key),
            self.hsrp_interfaces[key]
        )

        return self.hsrp_interfaces[key]

    def match_protocol_hsrp_interface(self, hsrp_interface_info, hsrp_interface_filter):
        if hsrp_interface_filter is None or len(hsrp_interface_filter) == 0:
            return True

        for ap_rule in hsrp_interface_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            if key == 'interface':
                if not filter_helper.match_string(value, hsrp_interface_info['id']):
                    return False

        return True

    def get_protocol_hsrp_interfaces(self, pod_id, node_id, hsrp_interface_filter=None):
        all_hsrp_interfaces = self.get_protocol_hsrp_interfaces_info(pod_id, node_id)
        if all_hsrp_interfaces is None:
            return None

        hsrp_interfaces = []

        for hsrp_interface_info in all_hsrp_interfaces:
            if not self.match_protocol_hsrp_interface(hsrp_interface_info, hsrp_interface_filter):
                continue

            hsrp_interfaces.append(
                hsrp_interface_info
            )

        hsrp_interfaces = sorted(
            hsrp_interfaces,
            key=lambda i: i['id']
        )

        return hsrp_interfaces
