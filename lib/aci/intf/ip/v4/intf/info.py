class InterfaceIpv4Info():
    def __init__(self):
        pass

    def get_node_interface_ipv4_info(self, managed_object):
        keys = [
            'adminSt',
            'dn',
            'donorIf',
            'id',
            'mode',
            'name',
            'status'
        ]

        info = {}
        for key in keys:
            info[key] = managed_object[key]

        return info

    def get_node_interface_ipv4(self, pod_id, node_id):
        managed_objects = self.get_node_interface_ipv4_mo(
            pod_id,
            node_id
        )
        if managed_objects is None:
            return None

        info = []
        for managed_object in managed_objects:
            info.append(
                self.get_node_interface_ipv4_info(
                    managed_object
                )
            )

        return info
