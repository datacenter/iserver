class OcpVmGetDay0():
    def __init__(self):
        pass

    def is_ocp_dv_vm_day0(self, namespace, name, cache=True):
        dvs_mo = self.get_ocp_dv_vm_day0(
            namespace,
            name,
            cache=cache
        )
        if dvs_mo is None:
            return False
        return True

    def get_ocp_dv_vm_day0(self, namespace, name, cache=True):
        if not self.get_ocp_dvs(cache=cache):
            return None

        for dv_mo in self.dvs:
            if dv_mo['metadata']['namespace'] == namespace and dv_mo['metadata']['name'] == name:
                return dv_mo

        return None
