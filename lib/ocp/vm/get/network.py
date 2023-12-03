class OcpVmGetNetwork():
    def __init__(self):
        pass

    def get_ocp_vm_interfaces_sriov_enabled(self, interfaces_info):
        sriov_enabled = False
        for interface_info in interfaces_info:
            if 'sriov' in interface_info:
                if interface_info['sriov'] is not None:
                    sriov_enabled = True
        return sriov_enabled

    def get_ocp_vm_interfaces_sriov_count(self, interfaces_info):
        sriov_count = 0
        for interface_info in interfaces_info:
            if 'sriov' in interface_info:
                if interface_info['sriov'] is not None:
                    sriov_count = sriov_count + 1
        return sriov_count

    def get_ocp_vm_interfaces_info(self, vm_info, vmi_info):
        info = vm_info['interfaces']
        if vmi_info is not None and vmi_info['interfaces'] is not None:
            for interface in info:
                interface['ip_address'] = None
                for interface_state in vmi_info['interfaces']:
                    if interface['name'] == interface_state['name']:
                        keys = ['info_source', 'ip_address', 'ip_addresses']
                        for key in keys:
                            if key in interface_state:
                                interface[key] = interface_state[key]

        for interface in info:
            interface['info'] = ''
            interface['vlan'] = ''
            interface['resourceName'] = ''
            interface['policyName'] = ''
            interface['sriovDeviceType'] = ''
            interface['sriovNic'] = ''

            if interface['name'] == 'default':
                if 'ip_address' in interface and interface['ip_address'] is not None:
                    if interface['masquerade'] is not None:
                        interface['info'] = '%s (masq)' % (interface['ip_address'])
                    else:
                        interface['info'] = interface['ip_address']
                continue

            if 'ip_address' in interface and interface['ip_address'] is not None:
                if interface['sriov'] is not None:
                    interface['info'] = '%s (sriov)' % (interface['ip_address'])
                else:
                    interface['info'] = interface['ip_address']
                continue

            if interface['sriov'] is not None:
                interface['info'] = '%s (sriov)' % (interface['name'])
            else:
                interface['info'] = interface['name']

            if interface['multusNetworkName'] != '' and interface['sriovEnabled']:
                sriov_network_mo = self.k8s_handler.get_sriov_network(
                    interface['multusNetworkName'],
                    return_mo=True
                )
                if sriov_network_mo is not None:
                    if 'resourceName' in sriov_network_mo['spec']:
                        interface['resourceName'] = sriov_network_mo['spec']['resourceName']
                    if 'vlan' in sriov_network_mo['spec']:
                        interface['vlan'] = sriov_network_mo['spec']['vlan']

            if interface['resourceName'] is not None:
                sriov_node_policy = self.k8s_handler.get_sriov_network_node_policy_with_resource_name(
                    interface['resourceName'],
                    return_mo=True
                )

                if sriov_node_policy is not None:
                    interface['policyName'] = sriov_node_policy['metadata']['name']
                    interface['sriovDeviceType'] = sriov_node_policy['spec']['deviceType']
                    if 'pfNames' in sriov_node_policy['spec']['nicSelector']:
                        interface['sriovNic'] = sriov_node_policy['spec']['nicSelector']['pfNames']

        return info
