class L3OutApi():
    def __init__(self):
        self.l3out_mo = None

    def get_l3out_mo(self):
        if self.l3out_mo is not None:
            return self.l3out_mo

        cache = self.get_object_cache(
            'l3extOut'
        )
        if cache is not None:
            self.l3out_mo = cache
            self.log.apic_mo(
                'l3extOut',
                self.l3out_mo
            )
            return self.l3out_mo

        children = [
            'bgpExtP',
            'ospfExtP',
            'eigrpExtP',
            'pimExtP',
            'l3extRsEctx',
            'l3extRsL3DomAtt'
        ]
        query = 'rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=l3extLNodeP,l3extInstP,%s' % (','.join(children))
        managed_objects = self.get_class(
            'l3extOut',
            query=query
        )
        if managed_objects is None:
            return None

        self.l3out_mo = []
        for managed_object in managed_objects['imdata']:
            attributes = managed_object['l3extOut']['attributes']
            attributes['l3extLNodeP'] = self.get_mo_children_attributes(
                'l3extOut',
                managed_object,
                'l3extLNodeP'
            )
            attributes['l3extInstP'] = self.get_mo_children_attributes(
                'l3extOut',
                managed_object,
                'l3extInstP'
            )
            for child_name in children:
                attributes[child_name] = self.get_mo_child_attributes(
                    'l3extOut',
                    managed_object,
                    child_name
                )

            attributes['faultCounts'] = self.get_mo_child_attributes(
                'l3extOut',
                managed_object,
                'faultCounts'
            )

            self.l3out_mo.append(
                attributes
            )

        self.log.apic_mo(
            'l3extOut',
            self.l3out_mo
        )

        self.set_object_cache(
            'l3extOut',
            self.l3out_mo
        )

        return self.l3out_mo
