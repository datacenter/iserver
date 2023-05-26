import copy


class PolicyInterfacePortChannelAttachment():
    def __init__(self):
        self.mo_policy_interface_port_channel_attachment = None

    def initialize_policy_interface_port_channel_attachment(self):
        if self.mo_policy_interface_port_channel_attachment is not None:
            return True

        port_channel_nodes = []

        for mo_port_channel in self.mo_policy_interface_port_channel:
            if len(mo_port_channel['relnFrom']) > 0:
                mo_port_channel_name = mo_port_channel['name']

                managed_objects = self.get_managed_object(
                    'uni/infra/lacplagp-%s' % (mo_port_channel_name),
                    query='rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf'
                )
                if managed_objects is not None:
                    for item in managed_objects['imdata']:
                        if 'lacpLagPol' in item and 'children' in item['lacpLagPol']:
                            for child in item['lacpLagPol']['children']:
                                if 'pconsNodeDeployCtx' in child:
                                    info = {}
                                    info['tDn'] = mo_port_channel['dn']
                                    info['tName'] = mo_port_channel_name
                                    info['tCl'] = 'lacpLagPol'
                                    info['nodeId'] = child['pconsNodeDeployCtx']['attributes']['nodeId']
                                    port_channel_nodes.append(info)

        self.mo_policy_interface_port_channel_attachment = []

        for port_channel_node in port_channel_nodes:
            managed_objects = self.get_managed_object(
                'uni/infra/lacplagp-%s' % (port_channel_node['tName']),
                query='rsp-subtree-include=full-deployment&target-node=%s&target-path=L2IfPolToEthIf' % (port_channel_node['nodeId'])
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
                                            self.mo_policy_interface_port_channel_attachment.append(info)

        self.log.apic_mo(
            'L2IfPolToEthIf.attributes',
            self.mo_policy_interface_port_channel_attachment
        )

        return True

    def get_policy_interface_port_channel_attachments(self, managed_object):
        return self.get_policy_interface_attachment(
            managed_object,
            self.mo_policy_interface_port_channel_attachment,
            interface_type='aggr'
        )
