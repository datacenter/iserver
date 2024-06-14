from lib import ip_helper


class AddressIpv4Info():
    def __init__(self):
        self.node_address_ipv4 = {}

    def get_node_address_ipv4_info(self, managed_object):
        keys = [
            'addr',
            'dn',
            'ipv4CfgState',
            'operSt',
            'operStQual',
            'type',
            'vpcPeer'
        ]

        info = {}
        for key in keys:
            info[key] = None
            if key in managed_object:
                info[key] = managed_object[key]

        # "addr": "<ip>/32"
        info['ip'] = info['addr']
        if len(info['addr'].split('/')) == 2:
            info['ip'] = info['addr'].split('/')[0]

        # topology/pod-1/node-201/sys/ipv4/inst/dom-mgmt:inb/if-[lo18]/addr-[<ip>/32]
        info['interface'] = info['dn'].split('/')[7].split('-')[1][1:][:-1]

        return info

    def get_node_addresses_ipv4_info(self, pod_id, node_id):
        key = '%s.%s' % (
            pod_id,
            node_id
        )
        if key in self.node_address_ipv4:
            return self.node_address_ipv4[key]

        managed_objects = self.get_node_address_ipv4_mo(
            pod_id,
            node_id
        )
        if managed_objects is None:
            return None

        self.node_address_ipv4[key] = []
        for managed_object in managed_objects:
            self.node_address_ipv4[key].append(
                self.get_node_address_ipv4_info(
                    managed_object
                )
            )

        return self.node_address_ipv4[key]

    def match_node_address_ipv4(self, address_info, address_filter):
        if address_filter is None or len(address_filter) == 0:
            return True

        for ap_rule in address_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            if key == 'ip':
                if value != address_info['ip']:
                    return False

            if key == 'subnet':
                if not ip_helper.is_ipv4_in_cidr(address_info['ip'], value):
                    return False

        return True

    def get_node_address_ipv4(self, pod_id, node_id, address_filter=None):
        addresses_info = self.get_node_addresses_ipv4_info(
            pod_id,
            node_id
        )
        if addresses_info is None:
            return None

        info = []
        for address_info in addresses_info:
            if not self.match_node_address_ipv4(address_info, address_filter):
                continue

            info.append(
                address_info
            )

        return info
