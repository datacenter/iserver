class OcpVmGetSriov():
    def __init__(self):
        pass

    def get_ocp_vm_sriov_info(self, vm_info):
        linux_handler = self.get_ocp_node_linux_handler(
            node_name=vm_info['node_name']
        )
        if linux_handler is None:
            return vm_info

        for interface_info in vm_info['interfaces']:
            interface_info['hostIf'] = {}
            if interface_info['sriovEnabled']:
                host_interface = linux_handler.get_interface(
                    interface_info['mac_address'],
                    cache=True
                )
                if host_interface is not None:
                    interface_info['hostIf']['index'] = host_interface['index']
                    interface_info['hostIf']['name'] = host_interface['name']
                    interface_info['hostIf']['flags'] = host_interface['flags']
                    interface_info['hostIf']['mtu'] = host_interface['mtu']
                    interface_info['hostIf']['state'] = host_interface['state']
                    interface_info['hostIf']['mac'] = host_interface['mac']
                    interface_info['hostIf']['vf'] = {}
                    for vf_info in host_interface['vf']:
                        if vf_info['mac'] == interface_info['mac_address']:
                            interface_info['hostIf']['vf']['index'] = vf_info['index']
                            interface_info['hostIf']['vf']['mac_address'] = vf_info['mac']
                            interface_info['hostIf']['vf']['vlan'] = vf_info['vlan']
                            interface_info['hostIf']['vf']['spoof'] = vf_info['spoof']
                            interface_info['hostIf']['vf']['link'] = vf_info['link']
                            interface_info['hostIf']['vf']['trust'] = vf_info['trust']

                    interface_info['hostIf']['numa'] = linux_handler.get_interface_numa(
                        host_interface['name']
                    )

        return vm_info
