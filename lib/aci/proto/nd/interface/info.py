import copy


class ProtocolNdInterfaceInfo():
    def __init__(self):
        pass

    def get_nd_active_interface_count(self, interfaces):
        count = 0
        for interface in interfaces:
            if 'neighborCount' in interface and interface['neighborCount'] > 0:
                count = count + 1
        return count

    def add_protocol_nd_interface_neighbor_info(self, interfaces, neighbors, remove_no_neighbors=False):
        for interface in interfaces:
            interface['neighborCount'] = 0
            interface_neighbors = []

            for neighbor in neighbors:
                if neighbor['interfaceId'] == interface['id']:
                    interface['neighborCount'] = interface['neighborCount'] + 1
                    interface_neighbors.append(
                        neighbor['sysName']
                    )

            interface['neighborList'] = ', '.join(interface_neighbors)

        if remove_no_neighbors:
            new_interfaces = []
            for interface in interfaces:
                if interface['neighborCount'] > 0:
                    new_interfaces.append(
                        interface
                    )

            interfaces = copy.deepcopy(new_interfaces)

        return interfaces

    def get_protocol_nd_interface_info(self, managed_object):
        info = {}
        info['__Output'] = {}
        for key in managed_object:
            if key == 'ndIfStats':
                stats_info = self.get_protocol_nd_interface_stats_info(managed_object[key])
                for stats_key in stats_info:
                    if stats_key == '__Output':
                        for stats_output_key in stats_info['__Output']:
                            info['__Output'][stats_output_key] = stats_info['__Output'][stats_output_key]
                        continue
                    info[stats_key] = stats_info[stats_key]

                continue

            info[key] = managed_object[key]

        info['pod_node_name'] = '%s/%s' % (
            info['dn'].split('/')[1],
            self.get_node_name(
                info['dn'].split('/')[2].split('-')[1]
            )
        )

        # topology/pod-1/node-201/sys/nd/inst/dom-cvim4a:cvim4a_VRF/if-[vlan161]
        info['domainName'] = info['dn'].split('/')[6][4:]

        info['__Output']['id'] = 'Yellow'
        if info['adminSt'] == 'enabled':
            info['__Output']['adminSt'] = 'Green'
        else:
            info['__Output']['adminSt'] = 'Red'

        return info

    def get_protocol_nd_interfaces_info(self, pod_id, node_id, interface_id=None):
        managed_objects = self.get_protocol_nd_interface_mo(pod_id, node_id)

        info = []
        for managed_object in managed_objects:
            nd_interface_info = self.get_protocol_nd_interface_info(
                managed_object
            )

            if interface_id is None:
                info.append(
                    nd_interface_info
                )

            if interface_id is not None and nd_interface_info['id'] == interface_id:
                return nd_interface_info

        info = sorted(
            info,
            key=lambda i: (
                i['domainName'],
                i['id']
            )
        )

        return info
