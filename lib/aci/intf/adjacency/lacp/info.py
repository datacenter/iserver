class InterfaceAdjacencyLacpInfo():
    def __init__(self):
        self.adjacency_lacp = {}

    def get_lacp_adjacency_endpoint_info(self, managed_object):
        keys = [
            'activityFlags',
            'dn',
            'key',
            'name',
            'port',
            'portPrio',
            'status',
            'sysId',
            'sysPrio'
        ]

        info = {}
        for key in keys:
            info[key] = None
            if key in managed_object:
                info[key] = managed_object[key]

        return info

    def get_lacp_adjacency_endpoint(self, pod_id, node_id, interface_id, allow_multiple=True):
        managed_objects = self.get_adjacency_lacp_mo(
            pod_id,
            node_id,
            interface_id
        )

        if managed_objects is None:
            return None

        info = []
        for managed_object in managed_objects:
            endpoint_info = self.get_lacp_adjacency_endpoint_info(
                managed_object
            )
            endpoint_info['pod_id'] = pod_id
            endpoint_info['node_id'] = node_id
            endpoint_info['port_id'] = interface_id

            info.append(
                endpoint_info
            )

        if allow_multiple:
            return info

        if len(info) == 0:
            return None

        return info[0]
