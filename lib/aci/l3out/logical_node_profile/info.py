from lib import filter_helper


class L3OutLogicalNodeProfileInfo():
    def __init__(self):
        self.l3out_logical_node_profile = None

    def get_l3out_logical_node_profile_configured_node_info(self, managed_objects):
        # https://<apic>/model-doc/#/objects/l3extRsNodeL3OutAtt/overview
        info = []
        for managed_object in managed_objects:
            node_info = {}
            node_info['rtrId'] = managed_object['rtrId']
            node_info['rtrIdLoopBack'] = managed_object['rtrIdLoopBack']
            node_info['podId'] = managed_object['tDn'].split('/')[1].split('-')[1]
            node_info['nodeId'] = managed_object['tDn'].split('/')[2].split('-')[1]
            if managed_object['tDn'].split('/')[0] == 'topology':
                node_info['nodeDn'] = '/'.join(managed_object['tDn'].split('/')[1:])
            else:
                node_info['nodeDn'] = managed_object['tDn']

            node_info['nodeT'] = '%s (%s)' % (
                node_info['nodeDn'],
                node_info['rtrId']
            )
            info.append(
                node_info
            )

        info = sorted(
            info,
            key=lambda i: i['nodeT']
        )

        return info

    def get_l3out_logical_node_profile_bgp_peer_info(self, managed_objects, bgp_asn_objects, bgp_local_asn_objects):
        info = []
        for managed_object in managed_objects:
            # https://<apic>/model-doc/#/objects/bgpPeerP/overview
            # Dn Format
            # [0]: uni/tn-{name}/out-{name}/lnodep-{name}/lifp-{name}/vlifp-[{nodeDn}]-[{encap}]/peerP-[{addr}]
            # [1]: uni/tn-{name}/out-{name}/lnodep-{name}/lifp-{name}/rspathL3OutAtt-[{tDn}]/peerP-[{addr}]
            # [2]: uni/tn-{name}/out-{name}/lnodep-{name}/peerP-[{addr}]
            # Examples
            # dn: /uni/tn-common/out-Infra_L3out/lnodep-Infra_L3out_LNP/lifp-Infra_L3out_LIfP/rspathL3OutAtt-[topology/pod-1/paths-2205/pathep-[eth1/25]]/peerP-[<ip>]
            # dn: /uni/tn-NSO_testvf/out-VNF_PRIVATE/lnodep-RIGHT/lifp-Floating_SVI/vlifp-[topology/pod-1/node-2206]-[vlan-936]/peerP-[<ip>/29]
            # dn: uni/tn-vEPC_demo/out-ACC_L3out/lnodep-ACC-L3out_LNP/peerP-[<ip>/32]
            keys = [
                'addr',
                'addrTCtrl',
                'adminSt',
                'allowedSelfAsCnt',
                'capability',
                'connectivityType',
                'ctrl',
                'ctrlExt',
                'dn',
                'peerCtrl',
                'privateASctrl',
                'sessionT',
                'ttl',
                'weight'
            ]

            bgp_peer_info = {}
            bgp_peer_info['__Output'] = {}

            for key in keys:
                bgp_peer_info[key] = None
                if key in managed_object:
                    bgp_peer_info[key] = managed_object[key]

            if bgp_peer_info['adminSt'] == 'enabled':
                bgp_peer_info['__Output']['enabledTick'] = 'Green'
                bgp_peer_info['enabled'] = True
                bgp_peer_info['enabledTick'] = '\u2713'
            else:
                bgp_peer_info['__Output']['enabledTick'] = 'Red'
                bgp_peer_info['enabled'] = True
                bgp_peer_info['enabledTick'] = '\u2713'

            if bgp_peer_info['peerCtrl'] == 'bfd':
                bgp_peer_info['isBfd'] = True
                bgp_peer_info['isBfdTick'] = '\u2713'
            else:
                bgp_peer_info['isBfd'] = False
                bgp_peer_info['isBfdTick'] = '\u2717'

            if len(managed_object['dn'].split('/peerP-[')[0].split('/')) == 4:
                bgp_peer_info['logical_interface_profile'] = None
                bgp_peer_info['type'] = 'loopback'
                bgp_peer_info['path'] = 'loopback'

            if len(managed_object['dn'].split('/rspathL3OutAtt-[')) == 2:
                bgp_peer_info['logical_interface_profile'] = managed_object['dn'].split('/')[4][5:]
                bgp_peer_info['type'] = 'rspathL3OutAtt'
                bgp_peer_info['path'] = managed_object['dn'].split('/rspathL3OutAtt-[')[1].split('/peerP-')[0][:-1]
                if bgp_peer_info['path'].split('/')[0] == 'topology':
                    bgp_peer_info['path'] = '/'.join(bgp_peer_info['path'].split('/')[1:])
                bgp_peer_info['path'] = bgp_peer_info['path'].replace('/pathep-[', ' ')
                bgp_peer_info['path'] = bgp_peer_info['path'].replace('[', '')
                bgp_peer_info['path'] = bgp_peer_info['path'].replace(']', '')
                bgp_peer_info['path'] = bgp_peer_info['path'].replace('protpaths', 'nodes')
                bgp_peer_info['path'] = bgp_peer_info['path'].replace('paths', 'node')

            if len(managed_object['dn'].split('/vlifp-[')) == 2:
                bgp_peer_info['logical_interface_profile'] = managed_object['dn'].split('/')[4][5:]
                bgp_peer_info['type'] = 'vlifp'
                bgp_peer_info['path'] = managed_object['dn'].split('/vlifp-[')[1].split('/peerP-')[0]
                if bgp_peer_info['path'].split('/')[0] == 'topology':
                    bgp_peer_info['path'] = '/'.join(bgp_peer_info['path'].split('/')[1:])
                bgp_peer_info['path'] = bgp_peer_info['path'].replace(']-[vlan-', ' vlan-')
                bgp_peer_info['path'] = bgp_peer_info['path'].replace('[', '')
                bgp_peer_info['path'] = bgp_peer_info['path'].replace(']', '')
                bgp_peer_info['path'] = bgp_peer_info['path'].replace('protpaths', 'nodes')
                bgp_peer_info['path'] = bgp_peer_info['path'].replace('paths', 'node')

            bgp_peer_info['asn'] = None
            bgp_peer_info['local_asn'] = None

            for item in bgp_asn_objects:
                if item['dn'] == '%s/as' % (managed_object['dn']):
                    bgp_peer_info['asn'] = item['asn']
                    break

            for item in bgp_local_asn_objects:
                if item['dn'] == '%s/localasn' % (managed_object['dn']):
                    bgp_peer_info['local_asn'] = item['localAsn']
                    break

            info.append(
                bgp_peer_info
            )

        return info

    def get_l3out_logical_node_profile_info(self, managed_object):
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

        info['configured_node'] = self.get_l3out_logical_node_profile_configured_node_info(
            managed_object['l3extRsNodeL3OutAtt']
        )

        info['bgp_peer_connectivity_profile'] = self.get_l3out_logical_node_profile_bgp_peer_info(
            managed_object['bgpPeerP'],
            managed_object['bgpAsP'],
            managed_object['bgpLocalAsnP']
        )

        return info

    def get_l3out_logical_node_profiles_info(self):
        if self.l3out_logical_node_profile is not None:
            return self.l3out_logical_node_profile

        managed_objects = self.get_l3out_logical_node_profile_mo()
        if managed_objects is None:
            return None

        self.l3out_logical_node_profile = []
        for managed_object in managed_objects:
            self.l3out_logical_node_profile.append(
                self.get_l3out_logical_node_profile_info(
                    managed_object
                )
            )

        self.log.apic_mo(
            'l3extLNodeP.info',
            self.l3out_logical_node_profile
        )

        return self.l3out_logical_node_profile

    def match_l3out_logical_node_profile(self, profile_info, profile_filter):
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

    def get_l3out_logical_node_profiles(self, profile_filter=None):
        all_profiles = self.get_l3out_logical_node_profiles_info()
        if all_profiles is None:
            return None

        node_profiles_info = []
        for profile_info in all_profiles:
            if not self.match_l3out_logical_node_profile(profile_info, profile_filter):
                continue

            node_profiles_info.append(
                profile_info
            )

        return node_profiles_info
