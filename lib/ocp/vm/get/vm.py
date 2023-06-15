from lib import filter_helper


class OcpVmGetVm():
    def __init__(self):
        self.vm_mo = None

    def is_ocp_vm_mo(self, vm_namespace, vm_name, cache=True):
        if self.get_ocp_vm_mo(vm_namespace, vm_name, cache=cache) is None:
            return False
        return True

    def match_ocp_vm_mo(self, vm_mo, vm_filter):
        if vm_filter is None or len(vm_filter) == 0:
            return True

        for ap_rule in vm_filter:
            (key, value) = ap_rule.split(':')

            key_found = False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, vm_mo['metadata']['name']):
                    return False

            if key == 'namespace':
                key_found = True
                if not filter_helper.match_string(value, vm_mo['metadata']['namespace']):
                    return False

            if not key_found:
                self.log.error(
                    'match_ocp_vm_mo',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_ocp_vms_mo(self, vm_filter=None, cache=True):
        if not cache or self.vm_mo is None:
            self.vm_mo = self.kubevirt_handler.list_virtual_machine_for_all_namespaces()

        if self.vm_mo is None:
            return None

        vms_mo = []
        for vm_mo in self.vm_mo:
            if not self.match_ocp_vm_mo(vm_mo, vm_filter):
                continue

            vms_mo.append(
                vm_mo
            )

        return vms_mo

    def get_ocp_vm_mo(self, vm_namespace, vm_name, cache=True):
        vm_filter = []
        vm_filter.append('namespace:%s' % (vm_namespace))
        vm_filter.append('name:%s' % (vm_name))

        vms_mo = self.get_ocp_vms_mo(
            vm_filter=vm_filter,
            cache=cache
        )
        if vms_mo is not None and len(vms_mo) == 1:
            return vms_mo[0]

        return None
