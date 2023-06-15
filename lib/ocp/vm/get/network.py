class OcpVmGetNetwork():
    def __init__(self):
        pass

    def get_ocp_vm_networks_info(self, vm_mo, vmi_mo):
        return vm_mo['spec']['template']['spec']['networks']

    def get_ocp_vm_interfaces_sriov_enabled(self, interfaces_info):
        sriov_enabled = False
        for interface_info in interfaces_info:
            if interface_info['sriov'] is not None:
                sriov_enabled = True
        return sriov_enabled

    def get_ocp_vm_interfaces_sriov_count(self, interfaces_info):
        sriov_count = 0
        for interface_info in interfaces_info:
            if interface_info['sriov'] is not None:
                sriov_count = sriov_count + 1
        return sriov_count

    def get_ocp_vm_interfaces_info(self, vm_mo, vmi_mo):
        interfaces = vm_mo['spec']['template']['spec']['domain']['devices']['interfaces']

        if vmi_mo is not None:
            if 'interfaces' in vmi_mo['status'] and vmi_mo['status']['interfaces'] is not None:
                for interface in interfaces:
                    for interface_state in vmi_mo['status']['interfaces']:
                        if interface['name'] == interface_state['name']:
                            keys = ['info_source', 'ip_address', 'ip_addresses']
                            for key in keys:
                                if key in interface_state:
                                    interface[key] = interface_state[key]

        networks = self.get_ocp_vm_networks_info(vm_mo, vmi_mo)
        for interface in interfaces:
            interface['__Output'] = {}
            interface['info'] = ''
            interface['masqueradeTick'] = ''
            interface['sriovEnabled'] = False
            interface['sriovTick'] = ''
            interface['podTick'] = ''
            interface['multusTick'] = ''
            interface['multusNetworkName'] = ''
            interface['vlan'] = ''
            interface['resourceName'] = ''
            interface['policyName'] = ''
            interface['sriovDeviceType'] = ''
            interface['sriovNic'] = ''

            if networks is not None:
                for network in networks:
                    if interface['name'] == network['name']:
                        if network['multus'] is not None:
                            interface['multusTick'] = '\u2713'
                            interface['__Output']['multusTick'] = 'Green'
                            if network['multus']['network_name'] is not None:
                                interface['multusNetworkName'] = network['multus']['network_name']

                        if network['multus'] is None:
                            if network['pod'] is not None:
                                interface['podTick'] = '\u2713'
                                interface['__Output']['podTick'] = 'Green'

            if interface['name'] == 'default':
                if interface['masquerade'] is not None:
                    interface['info'] = '%s (masq)' % (interface['ip_address'])
                    interface['masqueradeTick'] = '\u2713'
                    interface['__Output']['masqueradeTick'] = 'Green'
                else:
                    interface['info'] = interface['ip_address']
                continue

            if interface['ip_address'] is not None:
                if interface['sriov'] is not None:
                    interface['sriovTick'] = '\u2713'
                    interface['__Output']['sriovTick'] = 'Green'
                    interface['sriovEnabled'] = True
                    interface['info'] = '%s (sriov)' % (interface['ip_address'])
                else:
                    interface['info'] = interface['ip_address']
                continue

            if interface['sriov'] is not None:
                interface['sriovTick'] = '\u2713'
                interface['__Output']['sriovTick'] = 'Green'
                interface['sriovEnabled'] = True
                interface['info'] = '%s (sriov)' % (interface['name'])
            else:
                interface['info'] = interface['name']

            if interface['multusNetworkName'] != '' and interface['sriovEnabled']:
                sriov_network_mo = self.get_ocp_sriov_network(
                    'openshift-sriov-network-operator',
                    interface['multusNetworkName']
                )
                if sriov_network_mo is not None:
                    if 'resourceName' in sriov_network_mo['spec']:
                        interface['resourceName'] = sriov_network_mo['spec']['resourceName']
                    if 'vlan' in sriov_network_mo['spec']:
                        interface['vlan'] = sriov_network_mo['spec']['vlan']

            if interface['resourceName'] is not None:
                sriov_node_policy = self.get_ocp_sriov_network_node_policy_with_resource_name(
                    interface['resourceName']
                )

                if sriov_node_policy is not None:
                    interface['policyName'] = sriov_node_policy['metadata']['name']
                    interface['sriovDeviceType'] = sriov_node_policy['spec']['deviceType']
                    if 'pfNames' in sriov_node_policy['spec']['nicSelector']:
                        interface['sriovNic'] = sriov_node_policy['spec']['nicSelector']['pfNames']

        return interfaces
