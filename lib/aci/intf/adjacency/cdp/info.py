class InterfaceAdjacencyCdpInfo():
    def __init__(self):
        self.adjacency_cdp = {}

    def get_cdp_adjacency_endpoint_info(self, managed_object):
        keys = [
            'cap',
            'devId',
            'dn',
            'duplex',
            'index',
            'name',
            'nativeVlan',
            'platId',
            'portId',
            'stQual',
            'status',
            'sysName',
            'sysObjIdL',
            'sysObjIdV',
            'ver'
        ]

        info = {}
        info['__Output'] = {}
        for key in keys:
            info[key] = None
            if key in managed_object:
                info[key] = managed_object[key]

        # "dn": "topology/pod-1/node-205/sys/cdp/inst/if-[eth1/11]/adj-1"
        info['pod_id'] = info['dn'].split('/')[1]
        info['node_id'] = info['dn'].split('/')[2]
        info['interface_id'] = info['dn'].split('if-[')[1].split(']')[0]

        (info['__Output']['faults'], info['faults']) = self.get_faults_info(
            managed_object['faultCounts']
        )

        return info

    def get_cdp_adjacency_endpoint(self, pod_id, node_id, interface_id, allow_multiple=True):
        managed_objects = self.get_adjacency_cdp_mo(
            pod_id,
            node_id
        )

        if managed_objects is None:
            return None

        info = []
        for managed_object in managed_objects:
            endpoint_info = self.get_cdp_adjacency_endpoint_info(
                managed_object
            )

            if endpoint_info['interface_id'] == interface_id:
                info.append(
                    endpoint_info
                )

        if allow_multiple:
            return info

        if len(info) == 0:
            return None

        return info[0]
