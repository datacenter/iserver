class InterfacePolicyProfileInfo():
    def __init__(self):
        self.interface_policy_profile = {}

    def get_interface_policy_profile_info(self, managed_object):
        info = {}

        info['profile'] = managed_object['profile']
        info['selectors'] = []

        if managed_object['infraHPortS'] is not None:
            for selector_mo in managed_object['infraHPortS']:
                selector_info = {}
                selector_info['profile'] = selector_mo['dn'].split('/')[2][12:]
                selector_info['name'] = selector_mo['name']
                # dn:  "uni/infra/accportprof-ESX-R3DC-DVS_IntProf/hports-ESX-R3DC_ParentSel-typ-range"
                selector_info['dn'] = selector_mo['dn']
                selector_info['dn_name'] = selector_mo['dn'].split('/')[-1]
                selector_info['block'] = []
                selector_info['policy_group_type'] = None
                selector_info['policy_group_type_name'] = None
                selector_info['policy_group_name'] = None
                info['selectors'].append(
                    selector_info
                )

        if managed_object['infraRsAccBaseGrp'] is not None:
            for port_group_mo in managed_object['infraRsAccBaseGrp']:
                # dn: "uni/infra/accportprof-ESX-R3DC-DVS_IntProf/hports-ESX-R3DC_ParentSel-typ-range/portblk-3a62d357434b3409"
                port_group_selector_dn_name = port_group_mo['dn'].split('/')[3]
                for selector_info in info['selectors']:
                    if selector_info['dn_name'] == port_group_selector_dn_name:
                        if port_group_mo['tCl'] == 'infraAccPortGrp':
                            selector_info['policy_group_type'] = port_group_mo['tCl']
                            selector_info['policy_group_type_name'] = 'Access'
                            # tDn: "uni/infra/funcprof/accportgrp-ESX-R3DC-DVS_PolGrp"
                            selector_info['policy_group_name'] = port_group_mo['tDn'].split('/')[3][11:]
                            break

                        if port_group_mo['tCl'] == 'infraAccBndlGrp':
                            selector_info['policy_group_type'] = port_group_mo['tCl']
                            selector_info['policy_group_type_name'] = 'PC/VPC'
                            # "tDn": "uni/infra/funcprof/accbundle-UCSB1-FI-A_PolGrp"
                            selector_info['policy_group_name'] = port_group_mo['tDn'].split('/')[3][10:]
                            break

                        if port_group_mo['tCl'] == 'infraBrkoutPortGrp':
                            selector_info['policy_group_type'] = port_group_mo['tCl']
                            selector_info['policy_group_type_name'] = 'Breakout'
                            # 'dn': 'uni/infra/accportprof-k8s_CL2207_IntProf/hports-k8s_CL2207_brk_25g_4x_ParentIntSel-typ-range/rsaccBaseGrp'
                            selector_info['policy_group_name'] = port_group_mo['tDn'].split('/')[3][12:]
                            break

                        self.log.error(
                            'get_interface_policy_profile_info',
                            'Unsupported infraRsAccBaseGrp tCl: %s' % (port_group_mo['tCl'])
                        )

        if managed_object['infraPortBlk'] is not None:
            for port_block_mo in managed_object['infraPortBlk']:
                # dn: "uni/infra/accportprof-ESX-R3DC-DVS_IntProf/hports-ESX-R3DC_ParentSel-typ-range/portblk-4507c5cf36080774"
                port_block_selector_dn_name = port_block_mo['dn'].split('/')[3]
                for selector_info in info['selectors']:
                    if selector_info['dn_name'] == port_block_selector_dn_name:
                        block_info = {}
                        block_info['fromCard'] = int(port_block_mo['fromCard'])
                        block_info['toCard'] = int(port_block_mo['toCard'])
                        block_info['fromPort'] = int(port_block_mo['fromPort'])
                        block_info['toPort'] = int(port_block_mo['toPort'])
                        block_info['fromSubPort'] = None
                        block_info['toSubPort'] = None
                        selector_info['block'].append(
                            block_info
                        )

        if managed_object['infraSubPortBlk'] is not None:
            for port_block_mo in managed_object['infraSubPortBlk']:
                # dn: "uni/infra/accportprof-ESX-R3DC-DVS_IntProf/hports-ESX-R3DC_ParentSel-typ-range/portblk-4507c5cf36080774"
                port_block_selector_dn_name = port_block_mo['dn'].split('/')[3]
                for selector_info in info['selectors']:
                    if selector_info['dn_name'] == port_block_selector_dn_name:
                        block_info = {}
                        block_info['fromCard'] = int(port_block_mo['fromCard'])
                        block_info['toCard'] = int(port_block_mo['toCard'])
                        block_info['fromPort'] = int(port_block_mo['fromPort'])
                        block_info['toPort'] = int(port_block_mo['toPort'])
                        block_info['fromSubPort'] = int(port_block_mo['fromSubPort'])
                        block_info['toSubPort'] = int(port_block_mo['toSubPort'])
                        selector_info['block'].append(
                            block_info
                        )

        return info

    def get_interface_policy_profile(self, profile_name):
        if profile_name in self.interface_policy_profile:
            return self.interface_policy_profile[profile_name]

        profile_mo = self.get_interface_policy_profile_mo(profile_name)
        if profile_mo is None:
            return None

        self.interface_policy_profile[profile_name] = self.get_interface_policy_profile_info(profile_mo)

        self.log.apic_mo(
            'accportprof.info.%s' % (profile_name),
            self.interface_policy_profile[profile_name]
        )

        return self.interface_policy_profile[profile_name]

    def match_interface_policy_profile_selector_block(self, selector_info, interface_id):
        card_id = int(interface_id.split('/')[0])
        port_id = int(interface_id.split('/')[1])
        sub_port_id = None
        if len(interface_id.split('/')) == 3:
            sub_port_id = int(interface_id.split('/')[2])

        for block_info in selector_info['block']:
            if block_info['fromSubPort'] is None and sub_port_id is not None:
                continue

            if block_info['fromSubPort'] is not None and sub_port_id is None:
                continue

            if block_info['toCard'] < card_id < block_info['toCard']:
                return True

            if block_info['fromCard'] <= card_id <= block_info['toCard']:
                if block_info['fromCard'] == block_info['toCard']:
                    if block_info['fromPort'] == port_id == block_info['toPort']:
                        if sub_port_id is None:
                            return True

                        if block_info['fromSubPort'] <= sub_port_id <= block_info['toSubPort']:
                            return True

                    if block_info['fromPort'] <= port_id <= block_info['toPort']:
                        if sub_port_id is None:
                            return True

                        if block_info['fromSubPort'] <= sub_port_id <= block_info['toSubPort']:
                            return True

                    continue

                if block_info['fromCard'] == card_id and port_id >= block_info['fromPort']:
                    return True

                if block_info['toCard'] == card_id and port_id <= block_info['toPort']:
                    return True

        return False

    def get_interface_policy_profile_selectors(self, profile_name, interface_id):
        profile_info = self.get_interface_policy_profile(profile_name)
        if profile_info is None:
            return None

        for selector_info in profile_info['selectors']:
            if self.match_interface_policy_profile_selector_block(selector_info, interface_id):
                return selector_info

        return None
