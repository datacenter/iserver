from lib import filter_helper


class EndpointVmmVmInfo():
    def __init__(self):
        self.endpoint_vmm_vm = None

    def get_endpoint_vmm_vm_info(self, managed_object):
        info = {}
        info['__Output'] = {}

        keys = [
            'cfgdOs',
            'dn',
            'name',
            'oid',
            'os',
            'state'
        ]
        for key in keys:
            info[key] = None
            if key in managed_object:
                info[key] = managed_object[key]

        info['vmm'] = info['dn'].split('[')[1].split(']')[0]

        if info['state'] == 'poweredOn':
            info['__Output']['state'] = 'Green'
        else:
            info['__Output']['state'] = 'Red'

        return info

    def get_endpoints_vmm_vm_info(self):
        if self.endpoint_vmm_vm is not None:
            return self.endpoint_vmm_vm

        managed_objects = self.get_endpoint_vmm_vm_mo()
        if managed_objects is None:
            return None

        self.endpoint_vmm_vm = []
        for managed_object in managed_objects:
            self.endpoint_vmm_vm.append(
                self.get_endpoint_vmm_vm_info(
                    managed_object
                )
            )

        self.log.apic_mo(
            'compVm.info',
            self.endpoint_vmm_vm
        )

        return self.endpoint_vmm_vm

    def match_endpoint_vmm_vm(self, vm_info, vm_filter):
        if vm_filter is None or len(vm_filter) == 0:
            return True

        for rule in vm_filter:
            key = rule.split(':')[0]
            value = ':'.join(rule.split(':')[1:])

            if key == 'dn':
                if not filter_helper.match_string(value, vm_info['dn']):
                    return False

        return True

    def get_endpoint_vmm_vm(self, vm_filter=None, expected_single=False):
        all_vms = self.get_endpoints_vmm_vm_info()

        vms = []

        for vm_info in all_vms:
            if self.match_endpoint_vmm_vm(vm_info, vm_filter):
                vms.append(
                    vm_info
                )

        if expected_single:
            if len(vms) == 0:
                return None

            if len(vms) == 1:
                return vms[0]

            self.log.error(
                'get_endpoint_vmm_vm',
                'Expected single result'
            )
            return None

        return vms
