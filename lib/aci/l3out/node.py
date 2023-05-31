from lib import filter_helper


class L3OutNode():
    def __init__(self):
        self.l3out_node_profile_mo = None
        self.l3out_node_profile = None

    def get_l3out_node_profile_mo(self):
        if self.l3out_node_profile_mo is not None:
            return self.l3out_node_profile_mo

        children = [
            'l3extRsNodeL3OutAtt'
        ]
        query = 'rsp-subtree=children&rsp-subtree-class=%s' % (','.join(children))
        managed_objects = self.get_class(
            'l3extLNodeP',
            query=query
        )

        if managed_objects is None:
            return None

        self.l3out_node_profile_mo = []
        for managed_object in managed_objects['imdata']:
            attributes = managed_object['l3extLNodeP']['attributes']
            for child_name in children:
                attributes[child_name] = self.get_mo_children_attributes(
                    'l3extLNodeP',
                    managed_object,
                    child_name
                )

            self.l3out_node_profile_mo.append(
                attributes
            )

        self.log.apic_mo(
            'l3extLNodeP',
            self.l3out_node_profile_mo
        )

        return self.l3out_node_profile_mo

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
        info['l3out'] = info['dn'].split('/')[2][4:]

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

    def get_l3out_node_profiles_info(self):
        if self.l3out_node_profile is not None:
            return self.l3out_node_profile

        managed_objects = self.get_l3out_node_profile_mo()
        if managed_objects is None:
            return None

        self.l3out_node_profile = []
        for managed_object in managed_objects:
            self.l3out_node_profile.append(
                self.get_l3out_node_profile_info(
                    managed_object
                )
            )

        self.log.apic_mo(
            'l3extLNodeP.info',
            self.l3out_node_profile
        )

        return self.l3out_node_profile

    def match_l3out_node_profile(self, profile_info, profile_filter):
        if profile_filter is None or len(profile_filter) == 0:
            return True

        for aepg_rule in profile_filter:
            (key, value) = aepg_rule.split(':')

            if key == 'tenant':
                if not filter_helper.match_string(value, profile_info['tenant']):
                    return False

            if key == 'l3out':
                if not filter_helper.match_string(value, profile_info['l3out']):
                    return False

        return True

    def get_l3out_node_profiles(self, profile_filter=None):
        all_profiles = self.get_l3out_node_profiles_info()
        if all_profiles is None:
            return None

        node_profiles_info = []
        for profile_info in all_profiles:
            if not self.match_l3out_node_profile(profile_info, profile_filter):
                continue

            node_profiles_info.append(
                profile_info
            )

        return node_profiles_info
