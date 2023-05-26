class AddressIpv6Info():
    def __init__(self):
        pass

    def get_node_address_ipv6_info(self, managed_object):
        keys = [
            'addr',
            'dn',
            'ipv6CfgState',
            'operSt',
            'operStQual',
            'type',
            'vpcPeer'
        ]

        info = {}
        for key in keys:
            info[key] = managed_object[key]

        return info

    def get_node_address_ipv6(self, pod_id, node_id):
        managed_objects = self.get_node_address_ipv6_mo(
            pod_id,
            node_id
        )
        if managed_objects is None:
            return None

        info = []
        for managed_object in managed_objects:
            info.append(
                self.get_node_address_ipv6_info(
                    managed_object
                )
            )

        return info
