import time

from lib import filter_helper
from lib import ip_helper


class OcpVmGetInfo():
    def __init__(self):
        self.virtual_machine = None

    def get_ocp_vm_cpu_info(self, vm_mo, vmi_mo):
        if vmi_mo is None:
            info = vm_mo['spec']['template']['spec']['domain']['cpu']

        if vmi_mo is not None:
            info = vmi_mo['spec']['domain']['cpu']

        return info

    def get_ocp_vm_memory_info(self, vm_mo):
        return vm_mo['spec']['template']['spec']['domain']['resources']['requests']['memory']

    def get_ocp_vm_special_label(self, vm_mo):
        try:
            label = vm_mo['spec']['template']['metadata']['labels']['special']
        except BaseException:
            label = None

        return label

    def get_ocp_vm_node_name(self, vmi_mo):
        node_name = ''
        if vmi_mo is not None:
            if 'node_name' in vmi_mo['status']:
                node_name = vmi_mo['status']['node_name']
        return node_name

    def get_ocp_vm_guest_os_info(self, vmi_mo):
        info = None
        if vmi_mo is not None:
            info = vmi_mo['status']['guest_os_info']
        return info

    def get_ocp_vm_age(self, vmi_mo):
        age = ''
        if vmi_mo is not None:
            for step in vmi_mo['status']['phase_transition_timestamps']:
                if step['phase'] == 'Running':
                    create_timestamp = self.k8s_handler.convert_timestamp(step['phase_transition_timestamp'])
                    age = self.k8s_handler.convert_age(
                        int(time.time()) - create_timestamp
                    )
        return age

    def get_ocp_vm_info(self, vm_mo, vmi_mo):
        info = {}
        info['__Output'] = {}
        info['name'] = vm_mo['metadata']['name']
        info['namespace'] = vm_mo['metadata']['namespace']
        info['namespace_name'] = '%s/%s' % (
            info['namespace'],
            info['name']
        )
        info['vm_id'] = vm_mo['metadata']['uid']
        info['special'] = self.get_ocp_vm_special_label(vm_mo)
        info['cpu'] = self.get_ocp_vm_cpu_info(vm_mo, vmi_mo)
        info['memory'] = self.get_ocp_vm_memory_info(vm_mo)
        info['disks'] = self.get_ocp_vm_disks_info(vm_mo, vmi_mo)

        info['networks'] = self.get_ocp_vm_networks_info(vm_mo, vmi_mo)
        info['interfaces'] = self.get_ocp_vm_interfaces_info(vm_mo, vmi_mo)
        info['sriov_enabled'] = self.get_ocp_vm_interfaces_sriov_enabled(
            info['interfaces']
        )
        info['sriov_count'] = self.get_ocp_vm_interfaces_sriov_count(
            info['interfaces']
        )

        info['services'] = self.get_ocp_vm_services_info(
            info['special']
        )
        info['ports'] = []
        if info['services'] is not None:
            for service in info['services']:
                service['vm_namespace_name'] = info['namespace_name']
                for port in service['ports']:
                    info['ports'].append(port)

        info['nodeName'] = self.get_ocp_vm_node_name(vmi_mo)
        info['guestOSInfo'] = self.get_ocp_vm_guest_os_info(vmi_mo)
        info['age'] = self.get_ocp_vm_age(vmi_mo)

        info['vmi_id'] = None
        info['stateTransitions'] = None
        if vmi_mo is not None:
            info['vmi_id'] = vmi_mo['metadata']['uid']
            info['stateTransitions'] = vmi_mo['status']['phase_transition_timestamps']

        info['state'] = vm_mo['status']['printable_status']

        info['ready'] = False
        info['readyTick'] = '\u2717'
        info['__Output']['readyTick'] = 'Red'

        info['liveMigration'] = False
        info['liveMigrationTick'] = '\u2717'
        info['__Output']['liveMigrationTick'] = 'Red'

        info['failures'] = []
        info['failure'] = False
        info['failureTick'] = ''

        for condition in vm_mo['status']['conditions']:
            if condition['type'] == 'Ready':
                if condition['status'] == 'True':
                    info['ready'] = True
                    info['readyTick'] = '\u2713'
                    info['__Output']['readyTick'] = 'Green'

                continue

            if condition['type'] == 'LiveMigratable':
                if condition['status'] == 'True':
                    info['ready'] = True
                    info['liveMigrationTick'] = '\u2713'
                    info['__Output']['liveMigrationTick'] = 'Green'

                continue

            if condition['type'] == 'Paused':
                continue

            if condition['type'] == 'AgentConnected':
                continue

            if condition['type'] == 'Failure':
                info['failures'].append(condition)
                info['failure'] = True
                info['failureTick'] = '\u2713'
                info['__Output']['failureTick'] = 'Red'
                continue

            self.log.error(
                'get_ocp_vm_info',
                'Unsupported condition type: %s' % (condition)
            )

        return info

    def get_ocp_vms_info(self, cache=True):
        if cache and self.virtual_machine is not None:
            return self.virtual_machine

        vms_mo = self.get_ocp_vms_mo()
        if vms_mo is None:
            return None

        vmis_mo = self.get_ocp_vmis_mo(cache=cache)
        if vmis_mo is None:
            return None

        self.virtual_machine = []
        for vm_mo in vms_mo:
            vmi_mo = self.get_ocp_vmi_mo(
                vm_mo['metadata']['namespace'],
                vm_mo['metadata']['name']
            )

            vm_info = self.get_ocp_vm_info(
                vm_mo,
                vmi_mo
            )

            self.virtual_machine.append(vm_info)

        self.log.kubevirt_mo(
            'vm.info',
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
                if not filter_helper.match_string(value, vm_info['nodeName']):
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
