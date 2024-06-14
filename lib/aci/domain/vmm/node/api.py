class DomainVmmNodeApi():
    def __init__(self):
        self.domain_vmm_node_mo = {}

    def get_domain_vmm_node_mo(self, domain_name):
        if domain_name in self.domain_vmm_node_mo:
            return self.domain_vmm_node_mo[domain_name]

        key = domain_name
        cache = self.get_object_cache(
            'vmmDomP.%s' % (key)
        )
        if cache is not None:
            self.domain_vmm_node_mo[key] = cache
            self.log.apic_mo(
                'vmmDomP.%s' % (key),
                self.domain_vmm_node_mo[key]
            )
            return self.domain_vmm_node_mo[key]

        distinguished_name = 'uni/vmmp-VMware/dom-%s' % (domain_name)
        query = 'rsp-subtree-include=full-deployment&target-node=all&target-path=ADomPToEthIf'
        managed_objects = self.get_managed_object(
            distinguished_name,
            query=query,
            node_mo=True
        )

        if managed_objects is None:
            self.log.error(
                'get_domain_vmm_node_mo',
                'API failed'
            )
            return None

        if managed_objects['totalCount'] != '1':
            self.log.error(
                'get_domain_vmm_node_mo',
                'Unexpected object count'
            )
            return None

        for managed_object in managed_objects['imdata']:
            attributes = managed_object['vmmDomP']['attributes']
            attributes['pconsResourceCtx'] = self.get_mo_node_resource_ctx(
                'vmmDomP',
                managed_object
            )
            self.domain_vmm_node_mo[key] = attributes

        self.log.apic_mo(
            'vmmDomP.%s' % (key),
            self.domain_vmm_node_mo[key]
        )

        self.set_object_cache(
            'vmmDomP.%s' % (key),
            self.domain_vmm_node_mo[key]
        )

        return self.domain_vmm_node_mo[key]
