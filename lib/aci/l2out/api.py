class L2OutApi():
    def __init__(self):
        self.l2out_mo = None
        self.l2out_path_mo = None

    def get_l2out_mo(self):
        if self.l2out_mo is not None:
            return self.l2out_mo

        cache = self.get_object_cache(
            'l2extOut'
        )
        if cache is not None:
            self.l2out_mo = cache
            self.log.apic_mo(
                'l2extOut',
                self.l2out_mo
            )
            return self.l2out_mo

        query = 'rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=l2extLNodeP,l2extInstP,l2extRsEBd,l2extRsL2DomAtt'
        managed_objects = self.get_class(
            'l2extOut',
            query=query
        )
        if managed_objects is None:
            self.log.error(
                'get_l2out_mo',
                'API failed'
            )
            return None

        self.l2out_mo = []
        for managed_object in managed_objects['imdata']:
            attributes = managed_object['l2extOut']['attributes']
            attributes['l2extLNodeP'] = self.get_mo_children_attributes(
                'l2extOut',
                managed_object,
                'l2extLNodeP'
            )
            attributes['l2extInstP'] = self.get_mo_children_attributes(
                'l2extOut',
                managed_object,
                'l2extInstP'
            )
            attributes['l2extRsEBd'] = self.get_mo_child_attributes(
                'l2extOut',
                managed_object,
                'l2extRsEBd'
            )
            attributes['l2extRsL2DomAtt'] = self.get_mo_child_attributes(
                'l2extOut',
                managed_object,
                'l2extRsL2DomAtt'
            )
            attributes['l2extRsPathL2OutAtt'] = self.get_mo_children_attributes(
                'l2extOut',
                managed_object,
                'l2extRsPathL2OutAtt'
            )
            attributes['faultCounts'] = self.get_mo_child_attributes(
                'l2extOut',
                managed_object,
                'faultCounts'
            )

            self.l2out_mo.append(
                attributes
            )

        self.log.apic_mo(
            'l2extOut',
            self.l2out_mo
        )

        self.set_object_cache(
            'l2extOut',
            self.l2out_mo
        )

        return self.l2out_mo

    def get_l2out_path_mo(self):
        if self.l2out_path_mo is not None:
            return self.l2out_path_mo

        cache = self.get_object_cache(
            'l2extRsPathL2OutAtt'
        )
        if cache is not None:
            self.l2out_path_mo = cache
            self.log.apic_mo(
                'l2extRsPathL2OutAtt',
                self.l2out_path_mo
            )
            return self.l2out_path_mo

        managed_objects = self.get_class(
            'l2extRsPathL2OutAtt',
            node_class=True
        )
        if managed_objects is None:
            self.log.error(
                'get_l2out_paths_mo',
                'API failed'
            )
            return None

        self.l2out_path_mo = []
        for managed_object in managed_objects['imdata']:
            attributes = managed_object['l2extRsPathL2OutAtt']['attributes']
            self.l2out_path_mo.append(
                attributes
            )

        self.log.apic_mo(
            'l2extRsPathL2OutAtt',
            self.l2out_path_mo
        )

        self.set_object_cache(
            'l2extRsPathL2OutAtt',
            self.l2out_path_mo
        )

        return self.l2out_path_mo
