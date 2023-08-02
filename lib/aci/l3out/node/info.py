class L3OutNodeInfo():
    def __init__(self):
        self.l3out_node = {}

    def get_l3out_node_info(self, managed_object):
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
            # "topology/pod-1/node-3301/sys/vmms-[eth1/43]"
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

    def get_l3out_node(self, tenant_name, l3out_name):
        key = '%s.%s' % (tenant_name, l3out_name)
        if key in self.l3out_node:
            return self.l3out_node[key]

        # one object or None value is expected
        nodes_mo = self.get_l3out_node_mo(tenant_name, l3out_name)
        if nodes_mo is None:
            return None

        self.l3out_node[key] = self.get_l3out_node_info(
            nodes_mo
        )

        self.log.apic_mo(
            'l3extOut.%s.info' % (key),
            self.l3out_node[key]
        )

        return self.l3out_node[key]
