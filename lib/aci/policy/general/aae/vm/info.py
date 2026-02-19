class PolicyGeneralAaeVmInfo():
    def __init__(self):
        self.policy_global_aae_vm = {}

    def get_policy_global_aae_vm_info(self, managed_object):
        return managed_object['pconsResourceCtx']

    def get_policy_global_aae_vm(self, domain_name):
        if domain_name in self.policy_global_aae_vm:
            return self.policy_global_aae_vm[domain_name]

        # one object or None value is expected
        domain_nodes_mo = self.get_policy_global_aae_vm_mo(domain_name)
        if domain_nodes_mo is None:
            return None

        self.policy_global_aae_vm[domain_name] = self.get_policy_global_aae_vm_info(
            domain_nodes_mo
        )

        self.log.apic_mo(
            'infraAttEntityP.vm.%s.info' % (domain_name),
            self.policy_global_aae_vm[domain_name]
        )

        return self.policy_global_aae_vm[domain_name]
