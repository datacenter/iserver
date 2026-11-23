from lib import filter_helper


class L3OutLogicalNodeProfileApi():
    def __init__(self):
        self.l3out_logical_node_profile_mo = None

    def get_l3out_logical_node_profile_mo(self):
        if self.l3out_logical_node_profile_mo is not None:
            return self.l3out_logical_node_profile_mo

        cache = self.get_object_cache(
            'l3extLNodeP'
        )
        if cache is not None:
            self.l3out_logical_node_profile_mo = cache
            self.log.apic_mo(
                'l3extLNodeP',
                self.l3out_logical_node_profile_mo
            )
            return self.l3out_logical_node_profile_mo

        children = [
            'l3extRsNodeL3OutAtt',
            'l3extLIfP'
        ]
        query = 'rsp-subtree=children&rsp-subtree-class=%s' % (','.join(children))
        managed_objects = self.get_class(
            'l3extLNodeP',
            query=query
        )
        if managed_objects is None:
            return None

        node_children = [
            'bgpLocalAsnP',
            'bgpAsP',
            'ospfIfP',
            'eigrpIfP',
            'bgpPeerP',
            'bfdIfP',
            'bfdMhIfP',
            'hsrpIfP',
            'dhcpLbl'
        ]
        node_query = 'target-subtree-class=%s&query-target=subtree' % (','.join(node_children))
        node_managed_objects = self.get_class(
            'l3extLNodeP',
            query=node_query,
            node_class=True
        )
        if node_managed_objects is None:
            return None

        self.l3out_logical_node_profile_mo = []
        for managed_object in managed_objects['imdata']:
            attributes = managed_object['l3extLNodeP']['attributes']
            for child_name in children:
                attributes[child_name] = self.get_mo_children_attributes(
                    'l3extLNodeP',
                    managed_object,
                    child_name
                )

            for node_child_name in node_children:
                attributes[node_child_name] = []
                for node_managed_object in node_managed_objects['imdata']:
                    if node_child_name in node_managed_object:
                        if node_managed_object[node_child_name]['attributes']['dn'].startswith(attributes['dn']):
                            attributes[node_child_name].append(
                                node_managed_object[node_child_name]['attributes']
                            )

            self.l3out_logical_node_profile_mo.append(
                attributes
            )

        self.log.apic_mo(
            'l3extLNodeP',
            self.l3out_logical_node_profile_mo
        )

        self.set_object_cache(
            'l3extLNodeP',
            self.l3out_logical_node_profile_mo
        )

        return self.l3out_logical_node_profile_mo
