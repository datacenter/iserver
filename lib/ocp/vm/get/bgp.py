class OcpVmGetBgp():
    def __init__(self):
        pass

    def get_ocp_vm_bgp_neighbor_info(self, fabric_info, bgp_neighbor):
        bgp_neighbor_info = {}
        bgp_neighbor_info['__Output'] = {}
        bgp_neighbor_info['name'] = fabric_info['name']
        bgp_neighbor_info['sriovTick'] = fabric_info['sriovTick']
        bgp_neighbor_info['__Output']['sriovTick'] = fabric_info['__Output']['sriovTick']
        bgp_neighbor_info['type'] = fabric_info['type']
        bgp_neighbor_info['controller'] = fabric_info['controller']
        bgp_neighbor_info['type_controller'] = '%s:%s' % (
            bgp_neighbor_info['type'],
            bgp_neighbor_info['controller']
        )
        bgp_neighbor_info['pod_node_name'] = bgp_neighbor['pod_node_name']
        bgp_neighbor_info['bgpDomainName'] = bgp_neighbor['bgpDomainName']
        bgp_neighbor_info['asn'] = bgp_neighbor['asn']
        bgp_neighbor_info['addr'] = bgp_neighbor['state']['addr']
        bgp_neighbor_info['nbrType'] = bgp_neighbor['state']['type']
        bgp_neighbor_info['state'] = bgp_neighbor['state']['operSt']
        bgp_neighbor_info['paths'] = bgp_neighbor['state']['af-ipv4-ucast']['acceptedPaths']

        return bgp_neighbor_info

    def get_ocp_vm_bgp_info(self, vm_info):
        if self.fabric_handler is None:
            self.log.error(
                'get_ocp_vm_bgp_info',
                'Fabric info should be collected first'
            )
            return vm_info

        vm_info['bgp'] = []
        for interface_info in vm_info['interfaces']:
            if not interface_info['sriovEnabled']:
                continue

            for fabric_info in vm_info['fabric']:
                if fabric_info['name'] != interface_info['name']:
                    continue

                my_fabric_handler = None
                for fabric_handler in self.fabric_handler:
                    if fabric_handler['type'] == fabric_info['type']:
                        if fabric_handler['controller'] == fabric_info['controller']:
                            my_fabric_handler = fabric_handler['handler']

                if my_fabric_handler is None:
                    continue

                for fabric_interface_info in fabric_info['interface']:
                    for ip_address in fabric_info['ip']:
                        bgp_filter = []
                        bgp_filter.append(
                            'vrf:%s:%s' % (
                                fabric_info['vrfTenant'],
                                fabric_info['vrfCtx']
                            )
                        )
                        bgp_filter.append('nbp-ip:%s' % (ip_address))

                        node_bgp_info = my_fabric_handler.get_protocol_bgp(
                            fabric_interface_info['pod_id'],
                            fabric_interface_info['node_id'],
                            bgp_filter=bgp_filter
                        )
                        if node_bgp_info is not None:
                            if 'neighbors' in node_bgp_info:
                                for bgp_neighbor in node_bgp_info['neighbors']:
                                    if bgp_neighbor['state']['addr'] == ip_address:
                                        bgp_neighbor_info = self.get_ocp_vm_bgp_neighbor_info(
                                            fabric_info,
                                            bgp_neighbor
                                        )
                                        vm_info['bgp'].append(
                                            bgp_neighbor_info
                                        )

        return vm_info
