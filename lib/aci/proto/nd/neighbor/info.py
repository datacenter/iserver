class ProtocolNdNeighborInfo():
    def __init__(self):
        pass

    def get_protocol_nd_neighbor_info(self, managed_object):
        info = {}
        info['__Output'] = {}
        for key in managed_object:
            info[key] = managed_object[key]

        # topology/pod-1/node-201/sys/nd/inst/if-[mgmt0]/adj-1
        info['interfaceId'] = info['dn'].split('if-')[1].split(']')[0][1:]
        info['__Output']['interfaceId'] = 'Yellow'

        if info['nativeVlan'] == 'unspecified':
            info['nativeVlan'] = ''

        return info

    def get_protocol_nd_neighbors_info(self, pod_id, node_id, interface_id=None):
        managed_objects = self.get_protocol_nd_neighbor_mo(pod_id, node_id)
        if managed_objects is None:
            return None

        info = []
        for managed_object in managed_objects:
            nbr_info = self.get_protocol_nd_neighbor_info(
                managed_object
            )

            if interface_id is None:
                info.append(
                    nbr_info
                )

            if interface_id is not None and nbr_info['interfaceId'] == interface_id:
                info.append(
                    nbr_info
                )

        info = sorted(
            info,
            key=lambda i: i['sysName']
        )

        return info
