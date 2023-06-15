import copy


class PolicyInterfacePortChannelAttachmentApi():
    def __init__(self):
        self.policy_interface_port_channel_attachment_mo = None
        self.policy_interface_port_channel_nodes = None

    def get_policy_interface_port_channel_attachment_mo(self):
        if self.policy_interface_port_channel_attachment_mo is not None:
            return self.policy_interface_port_channel_attachment_mo

        cache = self.get_object_cache(
            'L2IfPolToEthIf'
        )
        if cache is not None:
            self.policy_interface_port_channel_attachment_mo = cache
            self.log.apic_mo(
                'L2IfPolToEthIf',
                self.policy_interface_port_channel_attachment_mo
            )
            return self.policy_interface_port_channel_attachment_mo

        self.policy_interface_port_channel_attachment_mo = []
        self.policy_interface_port_channel_nodes = []

        for port_channel_info in self.policy_interface_port_channel:
            port_channel_name = port_channel_info['name']
            managed_objects = self.get_managed_object(
                'uni/infra/lacplagp-%s' % (port_channel_name),
                query='rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf'
            )
            if managed_objects is not None:
                for item in managed_objects['imdata']:
                    if 'lacpLagPol' in item and 'children' in item['lacpLagPol']:
                        for child in item['lacpLagPol']['children']:
                            if 'pconsNodeDeployCtx' in child:
                                info = {}
                                info['tDn'] = port_channel_info['dn']
                                info['tName'] = port_channel_name
                                info['tCl'] = 'lacpLagPol'
                                info['nodeId'] = child['pconsNodeDeployCtx']['attributes']['nodeId']
                                info['profiles'] = []
                                if 'children' in child['pconsNodeDeployCtx']:
                                    for subchild in child['pconsNodeDeployCtx']['children']:
                                        if 'pconsDependencyCtx' in subchild:
                                            profile = {}
                                            profile['class'] = subchild['pconsDependencyCtx']['attributes']['ctxClass']
                                            profile['dn'] = subchild['pconsDependencyCtx']['attributes']['ctxDn']
                                            info['profiles'].append(
                                                profile
                                            )

                                self.policy_interface_port_channel_nodes.append(info)

        self.log.apic_mo(
            'L2IfPolToEthIf.nodes',
            self.policy_interface_port_channel_nodes
        )

        for port_channel_node in self.policy_interface_port_channel_nodes:
            managed_objects = self.get_managed_object(
                'uni/infra/lacplagp-%s' % (port_channel_node['tName']),
                query='rsp-subtree-include=full-deployment&target-node=%s&target-path=L2IfPolToEthIf' % (port_channel_node['nodeId'])
            )
            self.log.apic_mo(
                'L2IfPolToEthIf.%s.%s' % (port_channel_node['nodeId'], port_channel_node['tName']),
                managed_objects
            )
            if managed_objects is not None:
                for item in managed_objects['imdata']:
                    if 'lacpLagPol' in item and 'children' in item['lacpLagPol']:
                        for child in item['lacpLagPol']['children']:
                            if 'pconsNodeDeployCtx' in child:
                                if 'children' in child['pconsNodeDeployCtx']:
                                    for deploy_child in child['pconsNodeDeployCtx']['children']:
                                        if 'pconsResourceCtx' in deploy_child:
                                            info = copy.deepcopy(port_channel_node)
                                            info['dn'] = deploy_child['pconsResourceCtx']['attributes']['ctxDn']
                                            self.policy_interface_port_channel_attachment_mo.append(info)

        self.log.apic_mo(
            'L2IfPolToEthIf',
            self.policy_interface_port_channel_attachment_mo
        )

        self.set_object_cache(
            'L2IfPolToEthIf',
            self.policy_interface_port_channel_attachment_mo
        )

        return self.policy_interface_port_channel_attachment_mo
