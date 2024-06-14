from lib.xd import aci


class OcpVmGetFabric():
    def __init__(self):
        self.fabric_handler = None

    def load_ocp_vm_fabric_handlers(self, fabric_hints):
        if self.fabric_handler is not None:
            return

        self.fabric_handler = []
        for fabric_hint in fabric_hints:
            if fabric_hint['type'] == 'aci':
                aci_handler = aci.get_aci_handler(
                    fabric_hint['controller'],
                    log_id=self.log_id
                )
                if aci_handler is None:
                    self.log.error(
                        'get_ocp_vm_fabric_handlers',
                        'Failed to get aci handler: %s' % (fabric_hint['controller'])
                    )
                    continue

                handler = {}
                handler['type'] = 'aci'
                handler['controller'] = fabric_hint['controller']
                handler['handler'] = aci_handler
                self.fabric_handler.append(
                    handler
                )

    def get_ocp_vm_aci_endpoint_info(self, interface_info, apic_name, endpoint_info):
        fabric_info = {}
        fabric_info['__Output'] = {}
        fabric_info['name'] = interface_info['name']
        fabric_info['sriovTick'] = interface_info['sriovTick']
        fabric_info['__Output']['sriovTick'] = interface_info['__Output']['sriovTick']
        fabric_info['type'] = 'aci'
        fabric_info['controller'] = apic_name
        fabric_info['type_controller'] = '%s:%s' % (
            fabric_info['type'],
            fabric_info['controller']
        )
        fabric_info['encap'] = endpoint_info['encap']
        fabric_info['mac'] = endpoint_info['mac']
        fabric_info['vrfTenant'] = endpoint_info['vrfTenant']
        fabric_info['vrfCtx'] = endpoint_info['vrfName']

        fabric_info['ip'] = []
        for fv_ip in endpoint_info['fvIp']:
            fabric_info['ip'].append(fv_ip['addr'])
        fabric_info['ips'] = ','.join(fabric_info['ip'])

        fabric_info['interface'] = []
        interfaces = []
        for fabric_interface_info in endpoint_info['fabric']:
            fabric_info['interface'].append(fabric_interface_info)
            interfaces.append(fabric_interface_info['ep'])
        fabric_info['interfaces'] = ','.join(interfaces)

        return fabric_info

    def get_ocp_vm_fabric_info(self, vm_info):
        vm_info['fabric'] = []
        for interface_info in vm_info['interfaces']:
            if interface_info['sriovEnabled']:
                for fabric_handler in self.fabric_handler:
                    if fabric_handler['type'] == 'aci':
                        endpoint_filter = ['mac:%s' % interface_info['mac_address']]
                        endpoints = fabric_handler['handler'].get_endpoints(
                            endpoint_filter=endpoint_filter,
                            fabric_info=True
                        )
                        if endpoints is not None:
                            for endpoint_info in endpoints:
                                fabric_info = self.get_ocp_vm_aci_endpoint_info(
                                    interface_info,
                                    fabric_handler['controller'],
                                    endpoint_info
                                )
                                vm_info['fabric'].append(
                                    fabric_info
                                )

        return vm_info
