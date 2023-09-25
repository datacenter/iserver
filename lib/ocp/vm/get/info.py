from lib import filter_helper
from lib import ip_helper


class OcpVmGetInfo():
    def __init__(self):
        self.virtual_machine = None

    def get_ocp_vm_info(self, vm_info, vmi_info):
        info = {}
        info['__Output'] = {}

        vm_keys = [
            'namespace',
            'name',
            'namespace_name',
            'vm_id',
            'special',
            'cpu',
            'memory',
            'state',
            'networks',
            'ready',
            'readyTick',
            'liveMigration',
            'liveMigrationTick',
            'failures',
            'failure',
            'failureTick'
        ]
        for vm_key in vm_keys:
            info[vm_key] = vm_info[vm_key]

        for key in vm_info['__Output']:
            info['__Output'][key] = vm_info['__Output'][key]

        vmi_keys = [
            'vmi_id',
            'cpu',
            'node_name',
            'guest_os_info',
            'state_transitions',
            'age'
        ]
        for vmi_key in vmi_keys:
            if vmi_key not in info:
                info[vmi_key] = None

            if vmi_info is not None:
                info[vmi_key] = vmi_info[vmi_key]

        if vmi_info is not None:
            for key in vmi_info['__Output']:
                info['__Output'][key] = vmi_info['__Output'][key]

        info['disks'] = self.get_ocp_vm_disks_info(vm_info, vmi_info)
        info['interfaces'] = self.get_ocp_vm_interfaces_info(vm_info, vmi_info)
        info['sriov_enabled'] = self.get_ocp_vm_interfaces_sriov_enabled(
            info['interfaces']
        )
        info['sriov_count'] = self.get_ocp_vm_interfaces_sriov_count(
            info['interfaces']
        )

        info['services'] = self.k8s_handler.get_services(
            object_filter=['special:%s' % (info['special'])]
        )

        info['ports'] = []
        if info['services'] is not None:
            for service in info['services']:
                service['vm_namespace_name'] = info['namespace_name']
                for port in service['port']:
                    info['ports'].append(port)

        return info

    def get_ocp_vms_info(self, cache=True):
        if cache and self.virtual_machine is not None:
            return self.virtual_machine

        vms_info = self.kubevirt_handler.get_virtual_machines(
            cache_enabled=cache
        )
        if vms_info is None:
            return None

        self.virtual_machine = []
        for vm_info in vms_info:
            vmi_info = self.kubevirt_handler.get_virtual_machine_instance(
                vm_info['namespace'],
                vm_info['name'],
                cache_enabled=cache
            )

            ocp_vm_info = self.get_ocp_vm_info(
                vm_info,
                vmi_info
            )

            self.virtual_machine.append(ocp_vm_info)

        self.log.kubevirt_mo(
            'ocp.vm.info',
            self.virtual_machine
        )

        return self.virtual_machine

    def match_ocp_vm(self, vm_info, vm_filter):
        if vm_filter is None or len(vm_filter) == 0:
            return True

        for ap_rule in vm_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, vm_info['name']):
                    return False

            if key == 'namespace':
                key_found = True
                if not filter_helper.match_string(value, vm_info['namespace']):
                    return False

            if key == 'node':
                key_found = True
                if not filter_helper.match_string(value, vm_info['node_name']):
                    return False

            if key == 'sriov':
                key_found = True
                if value == 'enabled' and not vm_info['sriov_enabled']:
                    return False

                if value == 'disabled' and vm_info['sriov_enabled']:
                    return False

            if key == 'mac':
                key_found = True
                found = False
                for interface_info in vm_info['interfaces']:
                    if ip_helper.is_mac_match(value, interface_info['mac_address']):
                        found = True
                        break

                if not found:
                    return False

            if key == 'multus_network':
                key_found = True
                found = False
                for interface_info in vm_info['interfaces']:
                    if filter_helper.match_string(value, interface_info['multusNetworkName']):
                        found = True
                        break

                if not found:
                    return False

            if not key_found:
                self.log.error(
                    'match_ocp_vm',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_ocp_vms(self, vm_filter=None, csi_info=False, sriov_info=False, fabric_info=False, bgp_info=False, fabric_hint=None, cache=True):
        all_vms = self.get_ocp_vms_info(cache=cache)
        if all_vms is None:
            return None

        if fabric_hint is not None:
            self.load_ocp_vm_fabric_handlers(fabric_hint)

        vms = []
        for vm_info in all_vms:
            if not self.match_ocp_vm(vm_info, vm_filter=vm_filter):
                continue

            if csi_info:
                vm_info = self.get_ocp_vm_disks_csi_info(vm_info)

            if sriov_info:
                vm_info = self.get_ocp_vm_sriov_info(vm_info)

            if fabric_info or bgp_info:
                vm_info = self.get_ocp_vm_fabric_info(vm_info)

            if bgp_info:
                vm_info = self.get_ocp_vm_bgp_info(vm_info)

            vms.append(
                vm_info
            )

        vms = sorted(
            vms,
            key=lambda i: (
                i['namespace'],
                i['name']
            )
        )

        return vms
