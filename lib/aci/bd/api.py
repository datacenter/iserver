class BridgeDomainApi():
    def __init__(self):
        self.bridge_domain_mo = None

    def get_bridge_domains_mo(self):
        if self.bridge_domain_mo is not None:
            return self.bridge_domain_mo

        cache = self.get_object_cache(
            'fvBD'
        )
        if cache is not None:
            self.bridge_domain_mo = cache
            self.log.apic_mo(
                'fvBD',
                self.bridge_domain_mo
            )
            return self.bridge_domain_mo

        query = 'rsp-subtree=children&rsp-subtree-include=health,fault-count'

        # fvRsCtx
        # fvRsBdToEpRet
        # fvRsIgmpsn
        # fvRsMldsn
        # fvRsBDToNdP
        # fvRsBDToOut
        # fvRtLIfCtxToBD
        # fvSubnet
        # fvRtEPpInfoToBD
        # fvRtBDDefToBD

        children = [
            'fvRsCtx',
            'fvRsBdToEpRet',
            'fvRsIgmpsn',
            'fvRsMldsn',
            'fvRsBDToOut',
            'fvSubnet'
        ]
        for child in children:
            query = '%s&rsp-subtree-class=%s' % (query, child)

        managed_objects = self.get_class(
            'fvBD',
            query=query
        )
        if managed_objects is None:
            self.log.error(
                'get_bridge_domains_mo',
                'API failed'
            )
            return None

        self.bridge_domain_mo = []

        for managed_object in managed_objects['imdata']:
            attributes = managed_object['fvBD']['attributes']
            attributes['fvSubnet'] = self.get_mo_children_attributes(
                'fvBD',
                managed_object,
                'fvSubnet'
            )
            attributes['fvRsBDToOut'] = self.get_mo_children_attributes(
                'fvBD',
                managed_object,
                'fvRsBDToOut'
            )
            attributes['fvRsCtx'] = self.get_mo_child_attributes(
                'fvBD',
                managed_object,
                'fvRsCtx'
            )
            attributes['fvRsMldsn'] = self.get_mo_child_attributes(
                'fvBD',
                managed_object,
                'fvRsMldsn'
            )
            attributes['fvRsIgmpsn'] = self.get_mo_child_attributes(
                'fvBD',
                managed_object,
                'fvRsIgmpsn'
            )
            attributes['fvRsBdToEpRet'] = self.get_mo_child_attributes(
                'fvBD',
                managed_object,
                'fvRsBdToEpRet'
            )
            attributes['healthInst'] = self.get_mo_child_attributes(
                'fvBD',
                managed_object,
                'healthInst'
            )
            attributes['faultCounts'] = self.get_mo_child_attributes(
                'fvBD',
                managed_object,
                'faultCounts'
            )
            self.bridge_domain_mo.append(
                attributes
            )

        self.set_object_cache(
            'fvBD',
            self.bridge_domain_mo
        )

        return self.bridge_domain_mo
