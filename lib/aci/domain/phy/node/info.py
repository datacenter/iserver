class DomainPhyNodeInfo():
    def __init__(self):
        self.domain_phy_node = {}

    def get_domain_phy_node_info(self, managed_object):
        info = {}
        info['__Output'] = {}
        info['name'] = managed_object['name']

        node = {}
        info['interface'] = []
        for item in managed_object['pconsResourceCtx']:
            node_name = self.get_node_name(
                item['nodeId']
            )

            if node_name not in node:
                node[node_name] = {}
                node[node_name]['node_id'] = item['nodeId']
                node[node_name]['interfaces'] = 0

            port_info = {}
            port_info['__Output'] = {}
            port_info['pod_id'] = item['ctxDn'].split('/')[1].split('-')[1]
            port_info['node_id'] = item['nodeId']
            port_info['node_name'] = self.get_node_name(
                item['nodeId']
            )
            port_info['intf_type'] = item['ctxClass']
            # "topology/pod-1/node-2201/sys/phys-[eth1/43]"
            port_info['intf_name'] = item['ctxDn'].split('[')[1].split(']')[0]
            info['interface'].append(
                port_info
            )

            node[node_name]['interfaces'] = node[node_name]['interfaces'] + 1

        info['node'] = []
        for key in node:
            node_info = {}
            node_info['id'] = node[key]['node_id']
            node_info['name'] = key
            node_info['interfaces'] = node[key]['interfaces']
            info['node'].append(
                node_info
            )

        info['node'] = sorted(
            info['node'],
            key=lambda i: i['name']
        )

        info['interface'] = sorted(
            info['interface'],
            key=lambda i: (
                i['node_name'],
                i['intf_name']
            )
        )

        return info

    def get_domain_phy_node(self, domain_name):
        if domain_name in self.domain_phy_node:
            return self.domain_phy_node[domain_name]

        # one object or None value is expected
        domain_nodes_mo = self.get_domain_phy_node_mo(domain_name)
        if domain_nodes_mo is None:
            return None

        self.domain_phy_node[domain_name] = self.get_domain_phy_node_info(
            domain_nodes_mo
        )

        self.log.apic_mo(
            'physDomP.%s.info' % (domain_name),
            self.domain_phy_node[domain_name]
        )

        return self.domain_phy_node[domain_name]
