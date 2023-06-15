from lib import filter_helper


class OcpVmGetVmi():
    def __init__(self):
        self.vmi_mo = None

    def is_ocp_vmi_mo(self, namespace, name):
        if self.get_ocp_vmi_mo(namespace, name) is None:
            return False
        return True

    def match_ocp_vmi_mo(self, vmi_mo, vm_filter):
        if vm_filter is None or len(vm_filter) == 0:
            return True

        for ap_rule in vm_filter:
            (key, value) = ap_rule.split(':')

            key_found = False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, vmi_mo['metadata']['name']):
                    return False

            if key == 'namespace':
                key_found = True
                if not filter_helper.match_string(value, vmi_mo['metadata']['namespace']):
                    return False

            if not key_found:
                self.log.error(
                    'match_ocp_vmi_mo',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_ocp_vmis_mo(self, vm_filter=None, cache=True):
        if not cache or self.vmi_mo is None:
            self.vmi_mo = self.kubevirt_handler.list_virtual_machine_instance_for_all_namespaces()

        if self.vmi_mo is None:
            return None

        vmis_mo = []
        for vmi_mo in self.vmi_mo:
            if not self.match_ocp_vmi_mo(vmi_mo, vm_filter):
                continue

            vmis_mo.append(
                vmi_mo
            )

        return vmis_mo

    def get_ocp_vmi_mo(self, namespace, name, cache=True):
        vm_filter = []
        vm_filter.append('namespace:%s' % (namespace))
        vm_filter.append('name:%s' % (name))

        vmis_mo = self.get_ocp_vmis_mo(
            vm_filter=vm_filter,
            cache=cache
        )
        if vmis_mo is not None and len(vmis_mo) == 1:
            return vmis_mo[0]

        return None
