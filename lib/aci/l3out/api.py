class L3OutApi():
    def __init__(self):
        self.mo_l3out = None

    def initialize_l3out(self):
        if not self.initialize_l3out_node_profile():
            return False

        if self.mo_l3out is not None:
            return True

        children = [
            'bgpExtP',
            'ospfExtP',
            'eigrpExtP',
            'pimExtP',
            'l3extRsEctx',
            'l3extRsL3DomAtt'
        ]
        query = 'rsp-subtree=children&rsp-subtree-class=l3extLNodeP,l3extInstP,%s' % (','.join(children))
        managed_objects = self.get_class(
            'l3extOut',
            query=query
        )
        if managed_objects is None:
            return False

        self.mo_l3out = []
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

            self.mo_l3out.append(
                attributes
            )

        self.log.apic_mo(
            'l3extOut',
            self.mo_l3out
        )

        return True
