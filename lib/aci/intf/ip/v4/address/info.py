class AddressIpv4Info():
    def __init__(self):
        pass

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

        return info

    def get_node_address_ipv4(self, pod_id, node_id):
        managed_objects = self.get_node_address_ipv4_mo(
            pod_id,
            node_id
        )
        if managed_objects is None:
            return None

        info = []
        for managed_object in managed_objects:
            info.append(
                self.get_node_address_ipv4_info(
                    managed_object
                )
            )

        return info
