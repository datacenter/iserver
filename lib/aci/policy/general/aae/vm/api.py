class PolicyGeneralAaeVmApi():
    def __init__(self):
        self.policy_global_aae_vm_mo = {}

    def get_policy_global_aae_vm_mo(self, policy_name):
        if policy_name in self.policy_global_aae_vm_mo:
            return self.policy_global_aae_vm_mo[policy_name]

        key = policy_name
        cache = self.get_object_cache(
            'infraAttEntityP.vm.%s' % (key)
        )
        if cache is not None:
            self.policy_global_aae_vm_mo[key] = cache
            self.log.apic_mo(
                'infraAttEntityP.vm.%s' % (key),
                self.policy_global_aae_vm_mo[key]
            )
            return self.policy_global_aae_vm_mo[key]

        distinguished_name = 'uni/infra/attentp-%s' % (policy_name)
        query = 'rsp-subtree-include=full-deployment&target-node=all&target-path=AttEntityPToVirtualMachines'
        managed_objects = self.get_managed_object(
            distinguished_name,
            query=query,
            node_mo=True
        )

        if managed_objects is None:
            self.log.error(
                'get_policy_global_aae_vm_mo',
                'API failed'
            )
            return None

        for managed_object in managed_objects['imdata']:
            attributes = managed_object['infraAttEntityP']['attributes']
            attributes['pconsResourceCtx'] = self.get_mo_ctlr_resource_ctx(
                'infraAttEntityP',
                managed_object
            )
            self.policy_global_aae_vm_mo[key] = attributes

        self.log.apic_mo(
            'infraAttEntityP.vm.%s' % (key),
            self.policy_global_aae_vm_mo[key]
        )

        self.set_object_cache(
            'infraAttEntityP.vm.%s' % (key),
            self.policy_global_aae_vm_mo[key]
        )

        return self.policy_global_aae_vm_mo[key]
