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
        info['__Output'] = {}
        for key in keys:
            info[key] = None
            if key in managed_object:
                info[key] = managed_object[key]

        # "dn": "topology/pod-1/node-205/sys/lacp/inst/if-[eth1/27]/adj"
        info['apic'] = self.apic_name
        info['pod_id'] = info['dn'].split('/')[1]
        info['node_id'] = info['dn'].split('/')[2]
        info['interface_id'] = info['dn'].split('if-[')[1].split(']')[0]

        (info['__Output']['faults'], info['faults']) = self.get_faults_info(
            managed_object['faultCounts']
        )

        return info

    def get_lacp_adjacency_endpoints_info(self, pod_id, node_id):
        key = '%s.%s' % (
            pod_id,
            node_id
        )
        if key in self.adjacency_lacp:
            return self.adjacency_lacp[key]

        managed_objects = self.get_adjacency_lacp_mo(
            pod_id,
            node_id
        )
        if managed_objects is None:
            return None

        self.adjacency_lacp[key] = []
        for managed_object in managed_objects:
            self.adjacency_lacp[key].append(
                self.get_lacp_adjacency_endpoint_info(
                    managed_object
                )
            )

        return self.adjacency_lacp[key]

    def get_lacp_adjacency_endpoint(self, pod_id, node_id, interface_id, allow_multiple=True):
        endpoints_info = self.get_lacp_adjacency_endpoints_info(pod_id, node_id)
        if endpoints_info is None:
            return None

        info = []
        for endpoint_info in endpoints_info:
            if interface_id == endpoint_info['interface_id']:
                info.append(
                    endpoint_info
                )

        if allow_multiple:
            return info

        if len(info) == 0:
            return None

        return info[0]
