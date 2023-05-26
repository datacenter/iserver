import time


class OcpVmInfo():
    def __init__(self):
        pass

    def get_ocp_vm_info(self, vm_mo, vmi_mo):
        info = {}
        info['__Output'] = {}
        info['name'] = vm_mo['metadata']['name']
        info['namespace'] = vm_mo['metadata']['namespace']
        info['vm_id'] = vm_mo['metadata']['uid']

        try:
            info['special'] = vm_mo['spec']['template']['metadata']['labels']['special']
        except BaseException:
            info['special'] = None

        info['memory'] = vm_mo['spec']['template']['spec']['domain']['resources']['requests']['memory']

        info['disks'] = vm_mo['spec']['template']['spec']['domain']['devices']['disks']
        for disk in info['disks']:
            disk['type'] = self.get_ocp_vm_disk_type(disk)
            for volume in vm_mo['spec']['template']['spec']['volumes']:
                if volume['name'] == disk['name']:
                    disk['volume'] = self.get_ocp_vm_disk_volume_spec_info(volume)

        info['interfaces'] = vm_mo['spec']['template']['spec']['domain']['devices']['interfaces']
        info['networks'] = vm_mo['spec']['template']['spec']['networks']
        info['vmi_id'] = None
        info['nodeName'] = ''
        info['guestOSInfo'] = None
        info['stateTransitions'] = None
        info['age'] = ''

        if vmi_mo is None:
            info['cpu'] = vm_mo['spec']['template']['spec']['domain']['cpu']
            for disk in info['disks']:
                disk['info'] = '%s' % (
                    disk['name']
                )

        if vmi_mo is not None:
            info['cpu'] = vmi_mo['spec']['domain']['cpu']

            for step in vmi_mo['status']['phase_transition_timestamps']:
                if step['phase'] == 'Running':
                    info['creationTimestamp'] = self.k8s_handler.convert_timestamp(step['phase_transition_timestamp'])
                    info['age'] = self.k8s_handler.convert_age(
                        int(time.time()) - info['creationTimestamp']
                    )

            info['vmi_id'] = vmi_mo['metadata']['uid']

            if 'node_name' in vmi_mo['status']:
                info['nodeName'] = vmi_mo['status']['node_name']

            info['guestOSInfo'] = vmi_mo['status']['guest_os_info']

            info['stateTransitions'] = vmi_mo['status']['phase_transition_timestamps']

            if 'volume_status' in vmi_mo['status'] and vmi_mo['status']['volume_status'] is not None:
                for volume_status in vmi_mo['status']['volume_status']:
                    for disk in info['disks']:
                        if volume_status['name'] == disk['name']:
                            keys = ['persistent_volume_claim_info', 'target']
                            for key in keys:
                                if key in volume_status:
                                    disk[key] = volume_status[key]

                        try:
                            disk['info'] = '%s/%s - %s' % (
                                disk['name'],
                                disk['target'],
                                disk['persistent_volume_claim_info']['capacity']['storage']
                            )
                        except BaseException:
                            disk['info'] = ''

            if 'interfaces' in vmi_mo['status'] and vmi_mo['status']['interfaces'] is not None:
                for interface in info['interfaces']:
                    for interface_state in vmi_mo['status']['interfaces']:
                        if interface['name'] == interface_state['name']:
                            keys = ['info_source', 'ip_address', 'ip_addresses']
                            for key in keys:
                                if key in interface_state:
                                    interface[key] = interface_state[key]

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

    def get_ocp_vms_info(self, name=None, namespace=None):
        vms = self.get_ocp_vms()
        if vms is None:
            return None

        vmis = self.get_ocp_vmis()
        if vmis is None:
            return None

        vms_info = []
        for vm_mo in vms:
            if name is not None and vm_mo['metadata']['name'] != name:
                continue

            if namespace is not None and vm_mo['metadata']['namespace'] != namespace:
                continue

            vmi_mo = None
            for vmi_mo_obj in vmis:
                if vm_mo['metadata']['name'] == vmi_mo_obj['metadata']['name']:
                    if vm_mo['metadata']['namespace'] == vmi_mo_obj['metadata']['namespace']:
                        vmi_mo = vmi_mo_obj
                        break

            vm_info = self.get_ocp_vm_info(
                vm_mo,
                vmi_mo
            )

            vms_info.append(vm_info)

        self.log.kubevirt_mo(
            'vm_info',
            vms_info
        )

        if name is not None and namespace is not None:
            if len(vms_info) == 0:
                return None

            return vms_info[0]

        return vms_info

    def print_ocp_vm_base_info(self, info, stream='default'):
        order = [
            'namespace',
            'name',
            'nodeName',
            'cpu.cores',
            'memory',
            'state',
            'readyTick',
            'failureTick',
            'liveMigrationTick',
            'age'
        ]

        headers = [
            'Namespace',
            'Name',
            'Node',
            'CPU',
            'Memory',
            'State',
            'Ready',
            'Failure',
            'LM',
            'Age'
        ]

        self.my_output.dictionary(
            info,
            title='OCP Virtual Machine',
            underline=True,
            prefix="- ",
            justify=True,
            keys=order,
            title_keys=headers,
            stream=stream
        )

    def print_ocp_vm_info(self, info, stream='default'):
        self.print_ocp_vm_base_info(info, stream=stream)

        if len(info['failures']) > 0:
            for failure in info['failures']:
                self.my_output.default(
                    'Failure: %s' % (failure['reason']),
                    before_newline=True
                )
                self.my_output.default(
                    failure['message']
                )

    def print_ocp_vms_info(self, info):
        order = [
            'namespace',
            'name',
            'nodeName',
            'cpu.cores',
            'memory',
            'disks.info',
            'interfaces.ip_address',
            'state',
            'readyTick',
            'failureTick',
            'liveMigrationTick',
            'age'
        ]

        headers = [
            'Namespace',
            'Name',
            'Node',
            'CPU',
            'Memory',
            'Disks',
            'Interfaces',
            'State',
            'Ready',
            'Failure',
            'LM',
            'Age'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['disks', 'interfaces']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True
        )
