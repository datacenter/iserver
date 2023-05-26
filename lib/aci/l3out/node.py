class L3OutNode():
    def __init__(self):
        self.mo_l3out_node_profile = None

    def initialize_l3out_node_profile(self):
        if self.mo_l3out_node_profile is not None:
            return True

        children = [
            'l3extRsNodeL3OutAtt'
        ]
        query = 'rsp-subtree=children&rsp-subtree-class=%s' % (','.join(children))
        managed_objects = self.get_class(
            'l3extLNodeP',
            query=query
        )

        if managed_objects is None:
            return False

        self.mo_l3out_node_profile = []
        for managed_object in managed_objects['imdata']:
            attributes = managed_object['l3extLNodeP']['attributes']
            for child_name in children:
                attributes[child_name] = self.get_mo_children_attributes(
                    'l3extLNodeP',
                    managed_object,
                    child_name
                )

            self.mo_l3out_node_profile.append(
                attributes
            )

        self.log.apic_mo(
            'l3extLNodeP',
            self.mo_l3out_node_profile
        )

        return True

    def get_l3out_node_profile_info(self, managed_object):
        keys = [
            'descr',
            'dn',
            'name',
            'targetDscp',
            'userdom'
        ]

        info = {}
        info['__Output'] = {}

        for key in keys:
            info[key] = None
            if key in managed_object:
                info[key] = managed_object[key]

        # Dn format
        # uni/tn-SPIN_InnoLab/out-Calico_L3Out/lnodep-Calico_L3Out_nodeProfile
        info['tenant'] = info['dn'].split('/')[1][3:]
        info['l3out'] = info['dn'].split('/')[2][5:]

        info['nodes'] = []
        for item in managed_object['l3extRsNodeL3OutAtt']:
            node_info = {}
            node_info['rtrId'] = item['rtrId']
            node_info['rtrIdLoopBack'] = item['rtrIdLoopBack']
            node_info['podId'] = item['tDn'].split('/')[1].split('-')[1]
            node_info['nodeId'] = item['tDn'].split('/')[2].split('-')[1]
            node_info['nodeDn'] = item['tDn']
            info['nodes'].append(
                node_info
            )

        return info

    def get_l3out_node_profiles_info(self, tenant_name, l3out_name):
        node_profiles_info = []
        for mo_l3out_node_profile in self.mo_l3out_node_profile:
            if tenant_name == mo_l3out_node_profile['dn'].split('/')[1][3:]:
                if l3out_name == mo_l3out_node_profile['dn'].split('/')[2][4:]:
                    node_profiles_info.append(
                        self.get_l3out_node_profile_info(
                            mo_l3out_node_profile
                        )
                    )
        return node_profiles_info
